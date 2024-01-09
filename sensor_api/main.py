import datetime

from fastapi import FastAPI

from sensor import Sensor

app = FastAPI()

# sample request : http://127.0.0.1:8000/?year=2000&day=5&hour=13&month=3

@app.get('/')
async def root(year: int = None, month: int = None, day: int = None, hour: int = None):
    if year is None or month is None or day is None or hour is None:
        return "Some field is none, consider filling them all"
    print(f'year: {year}, month: {month}, day: {day}')
    return {"visiteurs": Sensor(5000).get_visitor_count(datetime.date(year, month, day), hour)}
