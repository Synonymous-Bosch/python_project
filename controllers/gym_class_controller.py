from flask import Blueprint, Flask, redirect, render_template, request

from models.gym_class import Gym_class
import repositories.gym_class_repository as gym_class_repository

gym_class_blueprint = Blueprint("gym_class", __name__)