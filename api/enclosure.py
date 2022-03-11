from flask import Blueprint, abort
from apifairy import body, response
from apifairy.decorators import other_responses


from api import db
from api.models import Enclosure
from api.schemas import EnclosureSchema, EmptySchema, AnimalSchema


enclosure = Blueprint('enclosure', __name__)
enclosure_schema = EnclosureSchema()
enclosures_schema = EnclosureSchema(many=True)

animals_schema = AnimalSchema(many=True)



@enclosure.route('/enclosure', methods=['POST'])
@body(enclosure_schema)
@response(enclosure_schema, 201)
def add_enclosure(args):
    """Add a new enclosure"""
    enclosure = Enclosure(**args)
    db.session.add(enclosure)
    db.session.commit()
    return enclosure
    
    
@enclosure.route('/enclosures', methods=['GET'])
@response(enclosures_schema)
def get_all_enclosure():
    """Get all enclosure"""
    return Enclosure.query.all()
    
    
@enclosure.route('/enclosures/<int:id>/clean', methods=['POST'])
@response(enclosure_schema)
@other_responses({404: 'Enclosure not found'})
def clean_enclosure(id: int):
    """Clean enclosure"""
    enclosure = Enclosure.query.get_or_404(id)
    enclosure.clean_up()
    db.session.commit()
    return enclosure
    

@enclosure.route('/enclosures/<int:id>/animals', methods=['GET'])
@response(animals_schema)
@other_responses({404: 'Enclosure not found'})
def get_enclosure_animals(id: int):
    """Get all animals in enclosure"""
    enclosure = Enclosure.query.get_or_404(id)
    return enclosure.animals.all()
    
    
@enclosure.route('/enclosures/<int:id>/animals', methods=['DELETE'])
def delete_enclosure(id: int):
    ...