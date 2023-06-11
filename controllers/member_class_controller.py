from flask import Blueprint, Flask, redirect, render_template, request

from models.gym_class import Gym_class
from models.member import Member
from models.member_class import Member_class
from repositories import gym_class_repository, member_repository, member_class_repository

member_class_blueprint = Blueprint("member_class", __name__)