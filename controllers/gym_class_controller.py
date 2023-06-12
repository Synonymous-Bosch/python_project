from flask import Blueprint, Flask, redirect, render_template, request

from models.gym_class import Gym_class
import repositories.gym_class_repository as gym_class_repository

gym_class_blueprint = Blueprint("gym_classes", __name__)

# INDEX
@gym_class_blueprint.route("/gym_classes")
def gym_class():
    gym_classes = gym_class_repository.select_all()
    return render_template("gym_classes/index.html", gym_classes=gym_classes)


# NEW
@gym_class_blueprint.route("/gym_classes/new")
def new_gym_class():
    return render_template("gym_classes/new.html")


# CREATE
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


# EDIT
@gym_class_blueprint.route("/gym_classes/<id>/edit")
def edit_gym_class(id):
    gym_class = gym_class_repository.select(id)
    return render_template('gym_classes/edit.html', gym_class=gym_class)


# UPDATE
@gym_class_blueprint.route("/gym_classes/<id>", methods=["POST"])
def update_gym_classes(id):
    name = request.form["name"]
    date = request.form["date"]
    start_time = request.form["start_time"]
    duration = request.form["duration"]
    max_capacity = request.form["max_capacity"]
    active = request.form["active"]
    gym_class = Gym_class(name, date, start_time, duration, max_capacity, active, id)
    gym_class_repository.update(gym_class)
    return redirect("/gym_classes")


# DELETE
@gym_class_blueprint.route("/gym_classes/<id>/delete", methods=["POST"])
def delete_gym_class(id):
    gym_class_repository.delete(id)
    return redirect("/gym_classes")

