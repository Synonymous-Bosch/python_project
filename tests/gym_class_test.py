import unittest
import datetime

from models.gym_class import Gym_class
from repositories import gym_class_repository

class TestGym_class(unittest.TestCase):
    def setUp(self):
        self.gym_class1 = Gym_class(name="Pump It", date=datetime.date(year=2023, month=6, day=15), start_time=datetime.time(hour=12, minute=00), duration=60, max_capacity=12)

    def test_gym_class_has_name(self):
        self.assertEqual("Pump It", self.gym_class1.name)

    def test_gym_class_has_date(self):
        self.assertEqual("2023-06-15", str(self.gym_class1.date))

    def test_gym_class_has_start_time(self):
        self.assertEqual("12:00", self.gym_class1.start_time.strftime("%H:%M"))

    def test_gym_class_has_duration(self):
        self.assertEqual(60, self.gym_class1.duration)

    def test_gym_class_has_max_capacity(self):
        self.assertEqual(12, self.gym_class1.max_capacity)

    def test_add_gym_class_to_table(self):
        gym_class_repository.delete_all()
        gym_class_repository.save(self.gym_class1)
        result = gym_class_repository.select_all()
        self.assertEqual("Pump It", result[0].name)
