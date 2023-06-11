import pdb
import datetime

from models.gym_class import Gym_class
from models.member import Member
from models.member_class import Member_class

import repositories.gym_class_repository as gym_class_repository
import repositories.member_repository as member_repository
import repositories.member_class_repository as member_class_repository

member_class_repository.delete_all()
gym_class_repository.delete_all()
member_repository.delete_all()

member1 = Member(name="Peter Cushing", date_of_birth=datetime.date(year=1913, month=5, day=26), premium=True)
member_repository.save(member1)

members = member_repository.select_all()

pdb.set_trace()