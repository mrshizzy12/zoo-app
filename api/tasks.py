from flask import Blueprint, abort

from api import db


tasks = Blueprint('tasks', __name__)


@tasks.route('/tasks/cleaning/', methods=['GET'])
def generate_cleaning_plan():
    ...
    
    
@tasks.route('/tasks/medical/', methods=['GET'])
def generate_medical_plan():
    ...
    

@tasks.route('/tasks/feeding/', methods=['GET'])
def generate_feeding_planS():
    ...