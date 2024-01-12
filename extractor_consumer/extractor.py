import os.path
import sys
import datetime

import requests
import pandas as pd

OUTPUT_FOLDER = "data/raw"


def main():
    if len(sys.argv) != 2:
        print("Usage: extractor.py date")
        exit(1)

    try:
        working_date = datetime.datetime.strptime(sys.argv[1], "%Y-%m-%d").date()
    except ValueError:
        print("La date saisi en entrée n'a pas le format correct, format attendu : YY-MM-DD")
        exit(2)

    print(f"Hello world {working_date}")

    today_date = datetime.date.today()
    delta = datetime.timedelta(days=1)
    data = []
    while working_date < today_date:
        for hour in range(24):
            api_response = requests.get("http://127.0.0.1:8000",
                                        params={'year': working_date.year,
                                                'month': working_date.month,
                                                'day': working_date.day,
                                                'hour': hour})
            visitor_count = api_response.json()['visiteurs']
            current_row = (working_date, hour, visitor_count)
            data.append(current_row)

        working_date += delta

    df = (pd.DataFrame(data, columns=['date', 'hour', 'visitors'])
          .assign(month=lambda df_: df_['date'].map(lambda x: f"{x.month}_{x.year}"))
          .assign(unite="visiteurs")
          .assign(id_magasin=None)
          .merge(pd.DataFrame(["capteur_titouan", "capteur_arnaud", "capteur_alexis"], columns=["id_capteur"]),
                 how="cross")
          )
    unique_months = df.month.unique()

    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)

    for working_month in unique_months:
        sample_month_data = df.copy().query(f"month == '{working_month}'").reset_index(drop=True).drop(columns="month")
        sample_month_data.to_csv(f"{OUTPUT_FOLDER}/data_{working_month}.csv", index=False)


if __name__ == "__main__":
    main()
