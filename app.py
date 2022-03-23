from random import random
from flask import Flask, jsonify
from flask_restx import Api, Resource
from utils import (ZooJsonEncoder, animal_parser,
                   enclosure_parser, employee_parser)
from flask_cors import CORS
import models

zoo = models.Zoo()

app = Flask(__name__)
app.json_encoder = ZooJsonEncoder

api = Api(app, title='Zoo API', description='A zoo management API.', default_label='Zoo')

cors = CORS(app)


@api.route('/add_animal')
class AddAnimal(Resource):
   
    @api.doc(parser=animal_parser)
    def post(self):
        """
            Summary:
                add an animal
            
            Returns:
                _dict_: returns a single animal
        """
        args = animal_parser.parse_args()
        animal = models.Animal(**args)
        zoo.add_animal(animal)
        return jsonify(animal)
    
    
@api.route('/enclosure/<enclosure_id>/animal/<animal_id>')
@api.doc(params={'enclosure_id': 'Enclosure ID', 'animal_id': 'Animal ID'})
class GetAnimal(Resource):
    def post(self, enclosure_id: str, animal_id: str):
        """
            Summary:
                Add an animal to an enclosure
            
        
            Args:
                enclosure_id (str): enclosure ID
                animal_id (str): animal ID 
        """
        enclosure = zoo.get_enclosure(enclosure_id)
        if enclosure:
            animal = zoo.get_animal(animal_id)
            if animal:
                enclosure.add_animal(animal)
                return {'success': f'Animal with ID {animal_id} added to enclosure {enclosure_id}.'}
            else:
                return {'404': f'Animal with ID {animal_id} not found.'}
        else:
            return {'404': f'Enclosure with ID {enclosure_id} not found.'}
        
    def get(self, enclosure_id: str, animal_id: str):
        """
            Summary:
                Get an animal from enclosure
            
        
            Args:
                enclosure_id (str): enclosure ID
                animal_id (str): animal ID
                
            Returns:
                _dict_: returns an animal object
        """
        enclosure = zoo.get_enclosure(enclosure_id)
        if enclosure:
            animal = enclosure.get_animal(animal_id)
            if animal:
                return jsonify(animal)
            else:
                return {'404': f'Animal with ID {animal_id} not found.'}
        else:
            return {'404': f'Enclosure with ID {enclosure_id} not found.'}
        
    def delete(self, enclosure_id: str, animal_id: str):
        """
            Summary:
                Delete animal from enclosure

            Args:
                enclosure_id (str): enclosure ID
                animal_id (str): animal ID

            Returns:
                _dict_: returns a success message
        """
        enclosure = zoo.get_enclosure(enclosure_id)
        if enclosure:
            animal = enclosure.get_animal(animal_id)
            if animal:
                enclosure.remove_animal(animal)
                return {'success': f'Animal with ID {animal_id} was removed.'}
            else:
                return {'404': f'Animal with ID {animal_id} not found.'}
        else:
            return {'404': f'Enclosure with ID {enclosure_id} not found.'}



@api.route('/animals')
class GetAllAnimals(Resource):
    def get(self):
        """
            Summary:
                Get all animals in the zoo
                
            Returns:
                list: returns a list of animals in the zoo
        """
        return jsonify(zoo.animals)



@api.route('/enclosure/<enclosure_id>/animal/<animal_id>/feed')
@api.doc(params={'enclosure_id': 'Enclosure ID', 'animal_id': 'Animal ID'})
class FeedAnimal(Resource):
    def post(self, enclosure_id: str, animal_id: str):
        """
            Summary:
                Feed an animal from enclosure
                
            Args:
                enclosure_id: a string ID for getting an enclosure
                animal_id: a string ID for getting an animal 
        """
        enclosure = zoo.get_enclosure(enclosure_id)
        if enclosure:
            animal = enclosure.get_animal(animal_id)
            if animal:
                animal.feed()
                return jsonify(animal)
            else:
                return {'404': f'Animal with ID {animal_id} not found.'}
        else:
            return {'404': f'Enclosure with ID {enclosure_id} not found.'}


@api.route('/add_enclosure')
class AddEnclosure(Resource):
    @api.doc(parser=enclosure_parser)
    def post(self):
        """
            Summery:
                Add an enclosure to the zoo
                
            Returns:
                dict: returns an enclosure object
        """
        args = enclosure_parser.parse_args()
        enclosure = models.Enclosure(**args)
        zoo.add_enclosure(enclosure)
        return jsonify(enclosure)


@api.route('/enclosure/<id>/clean')
@api.doc(params={'id': 'Enclosure ID'})
class CleanEnclosure(Resource):
    def post(self, id: str):
        """
            Summary:
                Clean enclosure
                
            Args:
                id (str): enclosure ID
                
            Returns:
                dict: returns an enclosure object
        """
        enclosure = zoo.get_enclosure(id)
        if enclosure:
           enclosure.clean()
           return jsonify(enclosure)



@api.route('/enclosure/<id>/animals')
@api.doc(params={'id': 'Enclosure ID'})
class GetEnclosureAnimals(Resource):
    def get(self, id: str):
        """
            Summary:
                Get all animal in an enclosure
            
            Args:
                id (str): a string ID for getting an enclosure

            Returns:
                list: a list of all animals in an enclosure
        """
        enclosure = zoo.get_enclosure(id)
        if enclosure:
           return jsonify(enclosure.animals)


@api.route('/enclosure/<id>/delete')
@api.doc(params={'id': 'Enclosure ID'})
class Deleteclosure(Resource):
    def delete(self, id: str):
        """
            Summary:
                Delete an enclosure
                
            Args:
                id (str): enclosure ID
                
            Returns:
                dict: returns a success message
        """
        enclosure = zoo.get_enclosure(id)
        if enclosure:
            new_enclosure = random([i for i in zoo.enclosures if i.id != id])
            if new_enclosure:
                for animal in enclosure.animals:
                    new_enclosure.animals.append(animal)
            else:
                return {"Error": "no new enclosure found."}
            zoo.remove_enclosure(enclosure)
            return {'success': 'Enclosure deleted'}
        else:
            return {'404': f'Enclosure with ID {id} not found.'}
            


@api.route('/add_employee')
class AddEmployee(Resource):
    @api.doc(parser=employee_parser)
    def post(self):
        """
            Summary:
                add an employee
                
            Returns:
                dict: returns a single employee
        """
        args = employee_parser.parse_args()
        employee = models.Employee(**args)
        zoo.add_employee(employee)
        return jsonify(employee)


@api.route('/employee/<employee_id>/care/<animal_id>/')
class AssignEmployeeAnimal(Resource):
    def post(self, employee_id: str, animal_id: str):
        """
            Summary:
                Assign an animal to an employee
            
            Args:
                employee_id (str): employee ID
                animal_id (str): animal ID

            Returns:
                dict: returns a single employee object.
        """
        employee = zoo.get_employee(employee_id)
        if employee:
            animal = zoo.get_animal(animal_id)
            if animal:
                employee.add_animal(animal)
                return jsonify(employee)
            else:
                return {'404': f'Animal with ID {animal_id} not found.'}
        else:
            return {'404': f'Employee with ID {employee_id} not found.'}


@api.route('/employee/<id>/delete')
@api.doc(params={'id': 'Employee ID'})
class DeleteEmployee(Resource):
    def delete(self, id: str):
        """
            Summary:
                Delete an employee
                
            Args:
                id (str): employee ID
                
            Returns:
                dict: returns a success message
        """
        employee = zoo.get_employee(id)
        if employee:
            new_employee = random([i for i in zoo.employees if i.id != id])
            if new_employee:
                for animal in employee.animals_in_care:
                    new_employee.animals_in_care.append(animal)
            else:
                return {'Error': 'no new employee found.'}
            zoo.remove_employee(employee)
            return {'success': 'Employee deleted'}
        else:
            return {'404': f'Employee with ID {id} not found.'}
        
    
@api.route('/employess/stats')
class GetEmployeeStats(Resource):
    def get(self):
        """
            Summary:
                Get all employee stats

            Returns:
                _list_: Returns a lsit of employee stats 
        """
        employee_stats = [e.stat() for e in zoo.employees]
        if employee_stats:
            return jsonify(employee_stats)
        else:
            return {'404': 'there are no current employees'}



@api.route('/tasks/feeding')
class FeedingSchedule(Resource):
    def get(self):
        """
            Summary:
                Get all animals to be feed
                
            Returns:
                _list_: returns a list of animals
        """
        data: list = []
        animals = [a for a in zoo.animals if a.feeding_schedule == True]
        
        for a in animals:
            c = {'animal': a.name, 'employee': random([em.name for em in zoo.employees])}
            data.append(c)
        return jsonify(data)


@api.route('/tasks/cleaning')
class CleaningSchedule(Resource):
    def get(self):
        """
            Summary:
                Get all enclosures to be cleaned
                
            Returns:
                _list_: returns a list of enclosures
        """
        data: list = []
        enclosures = [e for e in zoo.enclosures if e.cleaning_schedule == True]
        
        for e in enclosures:
            c = {'enclosure': e.name, 'cleaner': random([em.name for em in zoo.employees])}
            data.append(c)
        return jsonify(data)
    
    
@api.route('/tasks/medical')
class MedicalSchedule(Resource):
    def get(self):
        """
            Summary:
                Get all animals to be medicated
                
            Returns:
                _list_: returns a list of animals
        """
        animals = [a for a in zoo.animals if a.medical_schedule == True]
        
        if animals:
            return jsonify(animals)
        else:
            return {'404': 'no animals to be medicated.'}
    
    
    

if __name__ == '__main__':
    app.run(debug=True)