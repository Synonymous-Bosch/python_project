import unittest
import datetime

from models.gym_class import Gym_class
from models.member import Member
from models.member_class import Member_class

class TestMember_class(unittest.TestCase):
    def setUp(self):

        self.member1 = Member(name="Peter Cushing", date_of_birth=datetime.date(year=1913, month=5, day=26), premium=True)

        self.gym_class1 = Gym_class(name="Pump It Better", date=datetime.date(year=2023, month=6, day=15), start_time=datetime.time(hour=12, minute=00), duration=60, max_capacity=12)

        self.member_class1 = Member_class(self.gym_class1, self.member1)

    def test_member_class_has_member(self):
        self.assertEqual("Peter Cushing", self.member_class1.member.name)

    def test_member_class_has_class(self):
        self.assertEqual("Pump It Better", self.member_class1.gym_class.name)