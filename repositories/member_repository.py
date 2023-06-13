from db.run_sql import run_sql
import datetime

from models.member import Member
from models.gym_class import Gym_class

def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)

def select_all():
    members = []
    sql = "SELECT * FROM members"
    results = run_sql(sql)
    if results:
        for row in results:
            date_of_birth = datetime.date.strftime(row["date_of_birth"], '%d-%m-%Y')
            member = Member(row["name"], date_of_birth, row["premium"], row["active"], row["id"])
            members.append(member)
    members.sort(key=lambda x: x.id)
    return members

def save(member):
    sql = "INSERT INTO members (name, date_of_birth, premium, active) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [member.name, str(member.date_of_birth), member.premium, member.active]
    results = run_sql(sql, values)
    id = results[0]['id']
    member.id = id

def select(id):
    sql = "SELECT * FROM members WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        date_of_birth = datetime.date.strftime(result["date_of_birth"], '%Y-%m-%d')
        member = Member(result["name"], date_of_birth, result["premium"], result["active"], result["id"])
    return member

def delete(id):
    sql = "DELETE FROM members WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(member):
    sql = "UPDATE members SET (name, date_of_birth, premium, active) = (%s, %s, %s, %s) WHERE id = %s"
    values = [member.name, str(member.date_of_birth), member.premium, member.active, member.id]
    run_sql(sql, values)

def show_classes(member):
    gym_classes = []
    sql = "SELECT gym_classes.* FROM gym_classes INNER JOIN members_gym_classes ON members_gym_classes.gym_class_id = gym_classes.id WHERE member_id = %s"
    values = [member.id]
    results = run_sql(sql, values)

    for row in results:
        gym_class = Gym_class(row["name"], row["date"], row["start_time"], row["duration"], row["max_capacity"], row["active"], row["id"])
        gym_classes.append(gym_class)   
    return gym_classes


    