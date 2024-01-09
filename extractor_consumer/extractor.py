import sys
import datetime
import requests


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

    api_response = requests.get("http://127.0.0.1:8000",
                                params={'year': working_date.year,
                                        'month': working_date.month,
                                        'day': working_date.day,
                                        'hour': 23})
    print(api_response.json())


if __name__ == "__main__":
    main()
