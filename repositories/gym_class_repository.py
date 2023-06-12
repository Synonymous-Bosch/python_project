from db.run_sql import run_sql
import pdb
import datetime
from models.gym_class import Gym_class

def delete_all():
    sql = "DELETE FROM gym_classes"
    run_sql(sql)

def select_all():
    gym_classes = []
    # pdb.set_trace()
    sql = "SELECT * FROM gym_classes"
    results = run_sql(sql)
    for row in results:
        gym_class = Gym_class(row["name"], row["date"], row["start_time"], row["duration"], row["max_capacity"], row["active"], row["id"])
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
        gym_class = Gym_class(result["name"], result["date"], result["start_time"], result["duration"], result["max_capacity"], result["active"], result["id"])
    return gym_class

def delete(id):
    sql = "DELETE FROM gym_classes WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(gym_class):
    sql = "UPDATE gym_classes SET (name, date, start_time, duration, max_capacity, active) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [gym_class.name, str(gym_class.date), str(gym_class.start_time), gym_class.duration, gym_class.max_capacity, gym_class.active, gym_class.id]
    run_sql(sql, values)