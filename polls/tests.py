import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question

class QuestionModelTests(TestCase):
    def test_was_published_recently_with_twodays_past(self):
        time = timezone.now() - datetime.timedelta(days=2)
        twodays_past_question = Question(pub_date=time)
        self.assertIs(twodays_past_question.was_published_recently(), False)

    def test_was_published_recently_with_yesterday(self):
        time = timezone.now() - datetime.timedelta(days=1)
        yesterday_question = Question(pub_date=time)
        self.assertIs(yesterday_question.was_published_recently(), True)

    def test_was_published_recently_with_today(self):
        time = timezone.now()
        today_question = Question(pub_date=time)
        self.assertIs(today_question.was_published_recently(), True)

    def test_was_published_recently_with_tomorrow(self):
        time = timezone.now() + datetime.timedelta(days=1)
        tomorrow_question = Question(pub_date=time)
        self.assertIs(tomorrow_question.was_published_recently(), False)

    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)
