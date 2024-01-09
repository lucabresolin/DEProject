import sys
import datetime

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


if __name__ == "__main__":
    main()
