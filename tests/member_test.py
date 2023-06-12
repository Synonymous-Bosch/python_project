import unittest
import datetime

from models.member import Member
from repositories import member_repository, gym_class_repository, member_class_repository

class TestMember(unittest.TestCase):
    def setUp(self):
        self.member1 = Member(name="Peter Cushing", date_of_birth=datetime.date(year=1913, month=5, day=26), premium=True)

    def test_member_has_name(self):
        self.assertEqual("Peter Cushing", self.member1.name)

    def test_member_has_date_of_birth(self):
        self.assertEqual("1913-05-26", str(self.member1.date_of_birth))

    def test_member_has_premium(self):
        self.assertEqual(True, self.member1.premium)

    def test_add_member_to_members(self):
        member_repository.delete_all()
        member_repository.save(self.member1)
        result = member_repository.select_all()
        self.assertEqual("Peter Cushing", result[0].name)