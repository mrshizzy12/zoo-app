from json import JSONEncoder
from datetime import date
from flask_restx import reqparse

class ZooJsonEncoder(JSONEncoder):
    
    def default(self, obj):
        try:
            if isinstance(obj, date):
                return obj.isoformat()
            iterable = iter(obj)
        except TypeError as e:
            ...
        else:
            return list(iterable)
        return obj.__dict__

# Animal parser   
animal_parser = reqparse.RequestParser()
animal_parser.add_argument('species', type=str, required=True, help='The scientific name of the animal.')
animal_parser.add_argument('common_name', type=str, required=True, help='The common name of the animal.')
animal_parser.add_argument('age', type=int, required=True, help='The age of the animal.')

# Enclosure parser
enclosure_parser = reqparse.RequestParser()
enclosure_parser.add_argument('name', type=str, required=True, help='The name of the enclosure.')
enclosure_parser.add_argument('space', type=str, required=True, help='The information about available space (in sq. meters)..')

# Employee parser
employee_parser = reqparse.RequestParser()
employee_parser.add_argument('name', type=str, required=True, help='The name of the employee.')
employee_parser.add_argument('address', type=str, required=True, help='The address of the employee.')