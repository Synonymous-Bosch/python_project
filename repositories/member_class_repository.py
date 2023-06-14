from db.run_sql import run_sql
import datetime
import pdb

from models.member import Member
from models.gym_class import Gym_class
from models.member_class import Member_class

from repositories import gym_class_repository, member_repository

def delete_all():
    sql = "DELETE FROM members_gym_classes"
    run_sql(sql)

# Return list of all member_class objects. Not currently used.
def select_all():
    members_gym_classes = []
    sql = "SELECT * FROM members_gym_classes"
    results = run_sql(sql)
    for row in results:
        gym_class = gym_class_repository.select(row["gym_class_id"])
        member = member_repository.select(row["member_id"])
        member_gym_class = Member_class(gym_class, member, row["id"])
        members_gym_classes.append(member_gym_class)

    return members_gym_classes


def save(member_class):
    members_in_class = gym_class_repository.show_members(member_class.gym_class)
    # Classes from 17:30 are for premium customers only. Conditional determines whether class is after premium time.
    premium_class = False
    if member_class.gym_class.start_time >= datetime.time(hour=17, minute=30):
        premium_class = True
    # Conditional determines whether member has access to class
    if member_class.member.premium or premium_class == False:
        # Conditional determines whether class has capacity
        if member_class.gym_class.max_capacity > len(members_in_class):
            sql = "INSERT INTO members_gym_classes (gym_class_id, member_id) VALUES (%s, %s) RETURNING id"
            values = [member_class.gym_class.id, member_class.member.id]
            results = run_sql(sql, values)
            id = results[0]['id']
            member_class.id = id
    # return messages currently not used. Ideally would implement a pop-up to notify that registration failed.
        else: 
            return "Class is full!"
    else: 
        return "Class is for premium customers only"
    
# Select member_class from table by id
def select(id):
    sql = "SELECT * FROM members_gym_classes WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        # Create member_class python object and return
        result = results[0]
        gym_class = gym_class_repository.select(result['gym_class_id'])
        member = member_repository.select(result['member_id'])
        member_gym_class = Member_class(gym_class, member, result["id"])
    return member_gym_class

# Delete object by member_id and gym_class_id. Uses select_for_delete function to locate a single instance to avoid deletion of all duplicate class registrations.
def delete(member_id, gym_class_id):
    member_gym_class = select_for_delete(member_id, gym_class_id)
    sql = "DELETE FROM members_gym_classes WHERE id = %s"
    values = [member_gym_class.id]
    run_sql(sql, values)

# update class registration object. Not currently used.
def update(member_gym_class):
    sql = "UPDATE members SET (gym_class_id, member_id)  = (%s, %s) WHERE id = %s"
    values = [member_gym_class.gym_class.id, member_gym_class.member.id, member_gym_class.id]
    run_sql(sql, values)

# Used as part of delete class registration function. Identifies single member_gym_class object for deletion.
def select_for_delete(member_id, gym_class_id):
    sql = "SELECT * FROM members_gym_classes WHERE member_id = %s AND gym_class_id = %s"
    values = [member_id, gym_class_id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        gym_class = gym_class_repository.select(result['gym_class_id'])
        member = member_repository.select(result['member_id'])
        member_gym_class = Member_class(gym_class, member, result["id"])
    return member_gym_class