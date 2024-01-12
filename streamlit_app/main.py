import streamlit as st
import duckdb
import os
import pandas as pd
import plotly.express as px


def main():
    #duckdb.read_parquet("processed.parquet")
    print(os.getcwd())

    data = pd.read_parquet("data/processed")

    option = st.selectbox(
        'Quel capteur souhaitez-vous étudier',
        duckdb.sql("SELECT DISTINCT id_capteur FROM data").to_df())

    working_data = duckdb.sql(f"SELECT * FROM data WHERE id_capteur = '{option}'").to_df()
    st.write(working_data)

    fig = px.line(working_data, x="date", y="visitors")

    st.plotly_chart(fig)

    return 8


if __name__ == "__main__":
    main()