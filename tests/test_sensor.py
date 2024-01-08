import math
import random
import unittest
import datetime

from src.sensor import Sensor


def random_date():
    return datetime.date(random.randint(1000, 2040),
                         random.randint(1, 12),
                         random.randint(1, 28))


def random_hour():
    return random.randint(0, 23)


class TestSensor(unittest.TestCase):

    #prend en compte les erreurs crées exprès
    def test_seed_enforced_and_positive(self):
        seed = math.ceil(random.random() * 1000)
        sensor = Sensor(seed)
        count = 0
        ITERATION = 1000
        for k in range(ITERATION):
            day = random_date()
            hour = random_hour()

            visitor_count = sensor.get_visitor_count(day, hour)
            if visitor_count is not None:
                count += visitor_count

        mean = count / ITERATION
        self.assertLess(mean, seed)
        self.assertGreater(mean, 0)

    # ne prend pas en compte les erreurs, le test ne passe pas
    def test_consistence(self):
        ITERATION = 1000
        for k in range(ITERATION):
            with self.subTest(i=k):
                seed = math.ceil(random.random() * 1000)
                sensor = Sensor(seed)
                day = random_date()
                hour = random_hour()

                visitor_count = sensor.get_visitor_count(day, hour)
                second_visitor_count = sensor.get_visitor_count(day, hour)
                self.assertEquals(visitor_count, second_visitor_count)


if __name__ == '__main__':
    unittest.main()
