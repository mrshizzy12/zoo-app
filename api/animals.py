from flask import Blueprint, abort
from apifairy import body, response
from apifairy.decorators import other_responses

from api import db
from api.models import Animal, Enclosure
from api.schemas import AnimalSchema, EmptySchema


animals = Blueprint('animals', __name__)
animal_schema = AnimalSchema()
animals_schema = AnimalSchema(many=True)


@animals.route('/animal', methods=['POST'])
@body(animal_schema)
@response(animal_schema, 201)
def add_animal(args):
    """Register a new Animal"""
    animal = Animal(**args)
    db.session.add(animal)
    db.session.commit()
    return animal
    

@animals.route('/animal/<int:id>', methods=['GET'])
@response(animal_schema)
@other_responses({404: 'Animal not found'})
def get_animal(id: int):
    """Retrieve an animal by id"""
    return Animal.query.get_or_404(id)
    
    
@animals.route('/animal/<int:id>', methods=['DELETE'])
@response(EmptySchema, status_code=204, 
          description="Animal deleted successfully.")
@other_responses({404: 'Animal not found'})
def delete_animal(id: int):
    """Delete animal from database"""
    animal = Animal.query.get_or_404(id)
    db.session.delete(animal)
    db.session.commit()
    return {}
    
    
@animals.route('/animals/<int:id>/feed', methods=['POST'])
@response(animal_schema)
@other_responses({404: 'Animal not found'})
def feed_animal(id: int):
    """Feed animal"""
    animal = Animal.query.get_or_404(id)
    animal.feed()
    db.session.commit()
    return animal    
   
    
@animals.route('/animals', methods=['GET'])
@response(animals_schema)
def get_all_animals():
    """Retrieve all animals"""
    return Animal.query.all()
    
    
@animals.route('/animal/<int:id>/vet', methods=['POST'])
@response(animal_schema)
@other_responses({404: 'Animal not found'})
def vet_animal(id: int):
    """Vet animal"""
    animal = Animal.query.get_or_404(id)
    animal.vet()
    db.session.commit()
    return animal    
    
    
@animals.route('/animal/<int:id>/home/<int:enclosure_id>', methods=['POST'])
@response(animals_schema)
@other_responses({404: 'Animal not found'})
def assign_enclosure(id: int, enclosure_id: int):
    """Assign animal to an enclosure"""
    animal = Animal.query.get_or_404(id)
    enclosure = Enclosure.query.get_or_404(enclosure_id)
    enclosure.animals.append(animal)
    
    db.session.commit()
    return enclosure.animals.all()
    
    
@animals.route('/animal/birth', methods=['POST'])
def animal_birth():
    ...
    
    
@animals.route('/animal/death', methods=['POST'])
def animal_death():
    ...
    
    
@animals.route('/animals/stat', methods=['GET'])
def animal_stat():
    ...