import uuid
from datetime import datetime

    
class Animal:
    def __init__(self, species: str, common_name: str, age: int) -> None:
        self.id = str(uuid.uuid4())
        self.species = species
        self.common_name = common_name
        self.age = age
        self.feeding_record: list = []
        self.medical_record: list = []
        #self.enclosure = None
        #self.care_taker = None
        
    def feed(self) -> None:
        self.feeding_record.append(datetime.now())
        
    def vet(self) -> None:
        self.medical_record.append(datetime.now())
        
    def medical_schedule(self):
        now = datetime.now()
        last_medical_date = self.medical_record.pop()
        if last_medical_date:
            next_medical_date = (now - last_medical_date)
            if next_medical_date >= 30:
                return True
            else:
                return False
    
    def feeding_schedule(self):
        now = datetime.now()
        last_feeding_date = self.medical_record.pop()
        if last_feeding_date:
            next_feeding_date = (now - last_feeding_date)
            if next_feeding_date >= 1:
                return True
            else:
                return False 
    
    
class Enclosure:
    def __init__(self, name: str, space: str) -> None:
        self.id = str(uuid.uuid4())
        self.name = name
        self.space = space
        self.animals: list = []
        self.clean_record: list = []
        
    def add_animal(self, animal: str) -> None:
        self.animals.append(animal)
        
    def remove_animal(self, animal: str) -> None:
        self.animals.remove(animal)
        
    def clean(self) -> None:
        self.clean_record.append(datetime.now())
    
    def cleaning_schedule(self):
        now = datetime.now()
        last_clean_date = self.clean_record.pop()
        if last_clean_date:
            next_clean_date = (now - last_clean_date)
            if next_clean_date >= 2:
                return True
            else:
                return False 
        
    def get_animal(self, id: str):
        for animal in self.animals:
            if animal.id == id:
                return animal
            else:
                return
            
            
class Employee:
    def __init__(self, name: str, address: str) -> None:
        self.id = str(uuid.uuid4())
        self.name = name
        self.address = address
        self.animals_in_care: list = []
        
    def add_animal(self, animal: Animal) -> None:
        self.animals_in_care.append(animal)
        
    def stat(self):
        return {
            'name': self.name,
            'min': min(self.animals_in_care),
            'max': max(self.animals_in_care),
            'avg': sum(self.animals_in_care) / len(self.animals_in_care)
        }

class Zoo:
    def __init__(self) -> None:
        self.enclosures: list = []
        self.animals: list = []
        self.employees: list = []
        
        
    def add_enclosure(self, enclosure: Enclosure) -> None:
        self.enclosures.append(enclosure)
        
    def get_enclosure(self, id: str):
        for enclosure in self.enclosures:
            if enclosure.id == id:
                return enclosure
            else:
                return
            
    def remove_enclosure(self, enclosure: Enclosure) -> None:
        self.enclosures.remove(enclosure)
    
    def add_animal(self, animal: Animal) -> None:
        self.animals.append(animal)
        
    def get_animal(self, id: str):
        for animal in self.animals:
            if animal.id == id:
                return animal
            else:
                return
    
    def add_employee(self, employee: Employee) -> None:
        self.employees.append(employee)
        
    def get_employee(self, id: str):
        for employee in self.employees:
            if employee.id == id:
                return employee
            else:
                return
            
    def remove_employee(self, employee: Employee) -> None:
        self.employees.remove(employee)