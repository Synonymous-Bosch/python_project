from flask import Blueprint, Flask, redirect, render_template, request

from models.gym_class import Gym_class
from models.member import Member
from models.member_class import Member_class
from repositories import gym_class_repository, member_repository, member_class_repository

member_class_blueprint = Blueprint("member_class", __name__)

# INDEX
@member_class_blueprint.route("/members_classes")
def member_class():
    member_class = member_class_repository.select_all()
    return render_template("members_classes/index.html", member_class=member_class)


# # NEW
@member_class_blueprint.route("/members_classes/new")
def new_member_class():
    return render_template("members_classes/new.html")


# # CREATE
@member_class_blueprint.route("/members_classes", methods=["POST"])
def create_member_class():
    gym_class_id = request.form["class_id"]
    member_id = request.form["member_id"]
    new_member_class = Member_class(gym_class_id, member_id)
    member_class_repository.save(new_member_class)
    return redirect("/members_classes")


# # EDIT
@member_class_blueprint.route("/members_classes/<id>/edit")
def edit_member_class(id):
    member_class = member_class_repository.select(id)
    return render_template('members_classes/edit.html', member_class=member_class)


# # UPDATE
@member_class_blueprint.route("/members_classes/<id>", methods=["POST"])
def update_member_class(id):
    gym_class_id = request.form["gym_class_id"]
    member_id = request.form["member_id"]
    member_class = Member_class(gym_class_id, member_id, id)
    member_class_repository.update(member_class)
    return redirect("/members_classes")


# # DELETE
@member_class_blueprint.route("/members_classes/<id>/delete", methods=["POST"])
def delete_member_class(id):
    member_class_repository.delete(id)
    return redirect("/members_classes")