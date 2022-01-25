import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Schedule


# Schedule Model Tests
class ScheduleModelTests(TestCase):

    def test_race_in_future(self):
        """
        is_upcoming_soon() returns True for races that have not yet occurred
        """
        future_day_and_time = timezone.now() + datetime.timedelta(days=20)
        future_date = future_day_and_time.date()
        future_race = Schedule(date=future_date)
        self.assertIs(future_race.is_upcoming_soon(), True)

    def test_race_in_past(self):
        """
        is_upcoming_soon() returns False for races that have already occurred
        """
        past_day_and_time = timezone.now() - datetime.timedelta(days=1)
        past_date = past_day_and_time.date()
        past_race = Schedule(date=past_date)
        self.assertIs(past_race.is_upcoming_soon(), False)
