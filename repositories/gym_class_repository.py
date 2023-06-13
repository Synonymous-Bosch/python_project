from db.run_sql import run_sql
import pdb
import datetime
from datetime import date
from models.gym_class import Gym_class
from models.member import Member

def delete_all():
    sql = "DELETE FROM gym_classes"
    run_sql(sql)

def select_all():
    gym_classes = []
    # pdb.set_trace()
    today = datetime.date.today()
    sql = "SELECT * FROM gym_classes WHERE active = True AND date >= %s"
    values = [today]
    results = run_sql(sql, values)
    for row in results:
        date = datetime.date.strftime(row["date"], '%d-%m-%Y')
        gym_class = Gym_class(row["name"], date, row["start_time"], row["duration"], row["max_capacity"], row["active"], row["id"])
        gym_classes.append(gym_class)
    gym_classes.sort(key=lambda x: x.date)
    return gym_classes

def select_all_inactive():
    gym_classes = []
    # pdb.set_trace()
    sql = "SELECT * FROM gym_classes WHERE active = False"
    results = run_sql(sql)
    for row in results:
        date = datetime.date.strftime(row["date"], '%d-%m-%Y')
        gym_class = Gym_class(row["name"], date, row["start_time"], row["duration"], row["max_capacity"], row["active"], row["id"])
        gym_classes.append(gym_class)
    gym_classes.sort(key=lambda x: x.date)
    return gym_classes

def save(gym_class):
    sql = "INSERT INTO gym_classes (name, date, start_time, duration, max_capacity, active) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id"
    values = [gym_class.name, gym_class.date, gym_class.start_time, gym_class.duration, gym_class.max_capacity, gym_class.active]
    results = run_sql(sql, values)
    id = results[0]['id']
    gym_class.id = id

def select(id):
    # pdb.set_trace()
    sql = "SELECT * FROM gym_classes WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        date = datetime.date.strftime(result["date"], '%d-%m-%Y')
        gym_class = Gym_class(result["name"], date, result["start_time"], result["duration"], result["max_capacity"], result["active"], result["id"])
    return gym_class

def delete(id):
    sql = "DELETE FROM gym_classes WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(gym_class):
    sql = "UPDATE gym_classes SET (name, date, start_time, duration, max_capacity, active) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [gym_class.name, gym_class.date, gym_class.start_time, gym_class.duration, gym_class.max_capacity, gym_class.active, gym_class.id]
    run_sql(sql, values)

def show_members(gym_class):
    members = []
    sql = "SELECT members.* FROM members INNER JOIN members_gym_classes ON members_gym_classes.member_id = members.id WHERE gym_class_id = %s"
    values = [gym_class.id]
    results = run_sql(sql, values)

    for row in results:
        member = Member(row["name"], row["date_of_birth"], row["premium"], row["active"], row["id"])
        members.append(member)   
    return members