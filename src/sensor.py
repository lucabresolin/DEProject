import datetime
import random

def is_valid_hour(hour):
    return isinstance(hour, int) and 0 <= hour <= 23


def is_work_hours(hour):
    return 8 <= hour <= 19  # journée


def is_work_day_of_week(day):
    return day.weekday() == 6  # dimanche


def is_valid_day(day):
    return isinstance(day, datetime.date)


class Sensor:
    def __init__(self, seed) -> None:
        self.seed = seed

    def get_visitor_count(self, day, hour):
        if not is_valid_day(day) or not is_valid_hour(hour):
            return None

        activity_multiplier = 1.0 if is_work_hours(hour) or is_work_day_of_week(day) else 0.2
        output = activity_multiplier * (day.day * 31 + hour * 24 + hour * day.month * 365) % self.seed
        if random.random() < 0.01:
            if random.choice((True, False)):
                return None
            else:
                return output * self.seed * (-1) ** random.choice((1, 2))

        return output


a = Sensor(6700)
todate = datetime.date.today()

print(a.get_visitor_count(todate, 23), a.get_visitor_count(todate, 16))
