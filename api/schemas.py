from marshmallow import (validate, validates, 
            validates_schema, ValidationError, post_dump)
from api import ma, db
from api.models import Animal, Enclosure, Employee



class EmptySchema(ma.Schema):
    pass


class AnimalSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Animal
        include_fk = True
        ordered = True
        
    id = ma.auto_field(dump_only=True)
    age = ma.auto_field(required=True)
    species_name = ma.auto_field(required=True, 
                                 validate=validate.Length(min=3, max=50))
    common_name = ma.auto_field(required=True, 
                                 validate=validate.Length(min=3, max=50))
    time_fed = ma.auto_field(dump_only=True)
    check_up = ma.auto_field(dump_only=True)
    
    
    @post_dump
    def fix_datetimes(self, data, **kwargs):
        data['time_fed'] += 'Z'
        data['check_up'] += 'Z'
        return data
    

class EnclosureSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Enclosure
        ordered = True
        
    id = ma.auto_field(dump_only=True)
    name = ma.auto_field(required=True,
                         validate=validate.Length(min=3, max=100))
    area_sq = ma.auto_field(required=True, 
                                 validate=validate.Length(min=3, max=50))
    last_clean = ma.auto_field(dump_only=True)
    
    
    @post_dump
    def fix_datetimes(self, data, **kwargs):
        data['last_clean'] += 'Z'
        return data