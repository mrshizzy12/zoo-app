from api import db
import random
from datetime import datetime




class Animal(db.Model):
    __tablename__ = 'animals'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    age = db.Column(db.Integer, nullable=True)
    species_name = db.Column(db.String(50), nullable=False)
    common_name = db.Column(db.String(50), nullable=False)
    time_fed = db.Column(db.DateTime, default=datetime.utcnow)
    check_up = db.Column(db.DateTime, default=datetime.utcnow)
    Employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'))
    Enclosure_id = db.Column(db.Integer, db.ForeignKey('enclosures.id'))
    
    
    def __repr__(self):
        return '<Animal {}>'.format(self.species_name)
    
    
    def feed(self):
        self.time_fed = datetime.utcnow()
    
       
    def vet(self):
        self.check_up = datetime.utcnow()
        
        
    
class Enclosure(db.Model):
    __tablename__ = 'enclosures'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    area_sq = db.Column(db.String(50), nullable=True)
    last_clean = db.Column(db.DateTime, default=datetime.utcnow)
    animals = db.relationship('Animal', backref='enclosure', lazy='dynamic')
    
    def clean_up(self):
        self.last_clean = datetime.utcnow()
    
    
    def __repr__(self):
        return '<Enclosure {}>'.format(self.name)
    
    
class Employee(db.Model):
    __tablename__ = 'employees'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(100), nullable=True)
    animals = db.relationship('Animal', backref='employee', lazy='dynamic')
   
    
    def reassign(self):
        for animal in self.animals:
            employee = random.choice(Employee.query.all())
            employee.animals.append(animal)
            
            db.session.commit()
            
    
    def __repr__(self):
        return '<Employee {}>'.format(self.name)