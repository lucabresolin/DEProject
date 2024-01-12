import streamlit as st
import duckdb
import os
import pandas as pd


def main():
    #duckdb.read_parquet("processed.parquet")
    print(os.getcwd())

    data = pd.read_parquet("data/processed")

    option = st.selectbox(
        'Quel capteur souhaitez-vous étudier',
        duckdb.sql("SELECT DISTINCT id_capteur FROM data").to_df())

    return 8


if __name__ == "__main__":
    main()