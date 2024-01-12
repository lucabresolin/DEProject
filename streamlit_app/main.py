import streamlit as st
import duckdb
import os
import pandas as pd
import plotly.express as px


def main():
    #duckdb.read_parquet("processed.parquet")
    print(os.getcwd())

    data = pd.read_parquet("data/processed")

    # Using "with" notation
    with st.sidebar:
        option = st.selectbox(
            'Quel capteur souhaitez-vous étudier',
            duckdb.sql("SELECT DISTINCT id_capteur FROM data").to_df())

        aggregation_level = st.radio(
            "Choisissez un niveau d'aggrégation",
            ("Mensuel", "Hebdomadaire", "Journalier")[::-1]
        )

    data = duckdb.sql(f"SELECT * FROM data WHERE id_capteur = '{option}'").to_df()
    if aggregation_level == "Journalier":
        working_data = data
    elif aggregation_level == "Hebdomadaire":
        working_data = duckdb.sql(f"""
        SELECT  FIRST(date) as date,
         SUM(visitors) AS visitors, FIRST(unite),FIRST(id_capteur),
          AVG(moyenne_roulante) AS moyenne_roulante, AVG(pct_change) 
        FROM data 
        GROUP BY YEARWEEK(strptime(date, '%Y-%m-%d')) ORDER BY date""").to_df()
    elif aggregation_level == "Mensuel":
        working_data = duckdb.sql(f"""
        SELECT  YEAR(strptime(first(date), '%Y-%m-%d')) || '-' || MONTH(strptime(first(date), '%Y-%m-%d')) as date,
         SUM(visitors) AS visitors, FIRST(unite),FIRST(id_capteur),
          AVG(moyenne_roulante) AS moyenne_roulante, AVG(pct_change) 
        FROM data 
        GROUP BY MONTH(strptime(date, '%Y-%m-%d'))""").to_df()


    st.write(working_data)

    fig = px.line(working_data, x="date", y="visitors")
    figMoyh = px.line(working_data, x="date", y="moyenne_roulante")

    st.plotly_chart(fig)
    st.plotly_chart(figMoyh)

    return 8


if __name__ == "__main__":
    main()