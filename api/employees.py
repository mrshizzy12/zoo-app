from flask import Blueprint, abort

from api import db


employee = Blueprint('employee', __name__)


@employee.route('/employee', methods=['POST'])
def add_employee():
    ...
    

@employee.route('/employee/<int:id>/care/<int:animal_id>/', methods=['POST'])
def assign_animal_employee(id, animal_id):
    ...
    

@employee.route('/employee/<int:id>/care/animals', methods=['GET'])
def get_employee_animals(int:id):
    ...
    
    
@employee.route('/employee/stats', methods=['GET'])
def get_employee_animals(int:id):
    ...
    
    
@employee.route('/employee/<int:id>', methods=['DELETE'])
def delete_employee(int:id):
    ...