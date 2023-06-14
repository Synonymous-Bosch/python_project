from flask import Blueprint, Flask, redirect, render_template, request

from models.member import Member
from models.member_class import Member_class
import repositories.member_repository as member_repository
import repositories.gym_class_repository as gym_class_repository
import repositories.member_class_repository as member_class_repository

members_blueprint = Blueprint("members", __name__)

# Index page to show all members
@members_blueprint.route("/members")
def members():
    members = member_repository.select_all()
    return render_template("members/index.html", members=members)


# New member creation page
@members_blueprint.route("/members/new")
def new_member():
    return render_template("members/new.html")


# Create new member object
@members_blueprint.route("/members", methods=["POST"])
def create_members():
    name = request.form["name"]
    date_of_birth = request.form["date_of_birth"]
    premium = request.form["premium"]
    new_member = Member(name, date_of_birth, premium)
    member_repository.save(new_member)
    return redirect("/members")


# Edit member object page
@members_blueprint.route("/members/<id>/edit")
def edit_member(id):
    member = member_repository.select(id)
    return render_template('members/edit.html', member=member)


# Update member object details
@members_blueprint.route("/members/<id>", methods=["POST"])
def update_member(id):
    name = request.form["name"]
    date_of_birth = request.form["date_of_birth"]
    premium = request.form["premium"]
    active = request.form["active"]
    member = Member(name, date_of_birth, premium, active, id)
    member_repository.update(member)
    return redirect("/members")


# Delete member object
@members_blueprint.route("/members/<id>/delete", methods=["POST"])
def delete_member(id):
    member_repository.delete(id)
    return redirect("/members")

# Show classes specific member has registered to
@members_blueprint.route("/members/<id>/show_classes")
def show_classes_by_member(id):
    member = member_repository.select(id)
    classes = member_repository.show_classes(member)
    new_classes = gym_class_repository.select_all()
    return render_template('members/show_classes.html', classes=classes, member=member, new_classes=new_classes)


