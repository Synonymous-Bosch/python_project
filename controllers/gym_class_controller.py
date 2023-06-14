from flask import Blueprint, Flask, redirect, render_template, request
import pdb
import datetime
from models.gym_class import Gym_class
import repositories.gym_class_repository as gym_class_repository

gym_class_blueprint = Blueprint("gym_classes", __name__)

# Index page
@gym_class_blueprint.route("/gym_classes")
def gym_class():
    gym_classes = gym_class_repository.select_all()
    inactive_classes = gym_class_repository.select_all_inactive()
    return render_template("gym_classes/index.html", gym_classes=gym_classes, inactive_classes = inactive_classes)


# Add a new class
@gym_class_blueprint.route("/gym_classes/new")
def new_gym_class():
    return render_template("gym_classes/new.html")


# Create class
@gym_class_blueprint.route("/gym_classes", methods=["POST"])
def create_gym_class():
    name = request.form["name"]
    date = request.form["date"]
    start_time = request.form["start_time"]
    duration = request.form["duration"]
    max_capacity = request.form["max_capacity"]
    new_gym_class = Gym_class(name, date, start_time, duration, max_capacity)
    gym_class_repository.save(new_gym_class)
    return redirect("/gym_classes")


# Edit class page
@gym_class_blueprint.route("/gym_classes/<id>/edit")
def edit_gym_class(id):
    gym_class = gym_class_repository.select(id)
    return render_template('gym_classes/edit.html', gym_class=gym_class)


# Update class object
@gym_class_blueprint.route("/gym_classes/<id>", methods=["POST"])
def update_gym_classes(id):
    name = request.form["name"]
    date = request.form["date"]
    # Date field doesn't auto-populate at this time. Added conditional to ensure update doesn't fail if user doesn't select date.
    if date == '':
        date =  gym_class_repository.select(id).date
        date = datetime.datetime.strptime(date, '%d-%m-%Y')
    start_time = request.form["start_time"]
    duration = request.form["duration"]
    max_capacity = request.form["max_capacity"]
    active = request.form["active"]
    gym_class = Gym_class(name, date, start_time, duration, max_capacity, active, id)
    gym_class_repository.update(gym_class)
    return redirect("/gym_classes")


# Delete class object
@gym_class_blueprint.route("/gym_classes/<id>/delete", methods=["POST"])
def delete_gym_class(id):
    gym_class_repository.delete(id)
    return redirect("/gym_classes")

# Show members by class
@gym_class_blueprint.route("/gym_class/<id>/show_members")
def show_classes_by_member(id):
    gym_class = gym_class_repository.select(id)
    members = gym_class_repository.show_members(gym_class)
    return render_template('gym_classes/show_members.html', members=members, gym_class=gym_class)