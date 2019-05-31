from flask import Blueprint
from flask import wtforms
auth = Blueprint('auth',__name__)
from . import views,forms