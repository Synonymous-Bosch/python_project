from db.run_sql import run_sql
import datetime

from models.member import Member

def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)

def select_all():
    members = []
    sql = "SELECT * FROM members"
    results = run_sql(sql)
    for row in results:
        date_of_birth = datetime.date.strftime(row["date_of_birth"], '%Y-%m-%d')
        member = Member(row["name"], date_of_birth, row["premium"], row["active"], row["id"])
        members.append(member)
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


    