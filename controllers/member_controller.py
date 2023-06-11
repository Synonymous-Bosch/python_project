from flask import Blueprint, Flask, redirect, render_template, request

from models.member import Member
import repositories.member_repository as member_repository

members_blueprint = Blueprint("members", __name__)

# INDEX
@members_blueprint.route("/members")
def memnbers():
    members = member_repository.select_all()
    return render_template("members/index.html", members=members)


# NEW
@members_blueprint.route("/members/new")
def new_member():
    return render_template("members/new.html")


# CREATE
@members_blueprint.route("/members", methods=["POST"])
def create_members():
    name = request.form["name"]
    date_of_birth = request.form["date_of_birth"]
    premium = request.form["premium"]
    new_member = Member(name, date_of_birth, premium)
    member_repository.save(new_member)
    return redirect("/humans")


# # EDIT



# # UPDATE



# # DELETE
