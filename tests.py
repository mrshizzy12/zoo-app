import unittest
from flask import current_app
from app import create_app, zoo



class TestZooApi(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.appctx = self.app.app_context()
        self.appctx.push()
        self.client = self.app.test_client()
        
        
    def tearDown(self):
        self.appctx.pop()
        self.app = None
        self.appctx = None
        self.client = None
        
    def test_app(self):
        assert self.app is not None
        assert current_app == self.app
        
    def test_api_get_all_animals(self):
        response = self.client.get('/animals')
        assert response.status_code == 200
        
    def test_api_add_animal(self):
        response = self.client.post('/add_animal', json={
            'species': 'bird',
            'common_name': 'chicken',
            'age': 1
        })
        assert response.status_code == 200
        assert response.json['species'] == 'bird'
        
    def test_api_add_enclosure(self):
        response = self.client.post('/add_enclosure', json={
            'name': 'Poultry 1',
            'space': '100 sq. meters'
        })
        assert response.status_code == 200
        assert response.json['name'] == 'Poultry 1'
        
    def test_api_add_employee(self):
        response = self.client.post('/add_employee', json={
            'name': 'John Doe',
            'address': '605 park avenue, new jersey'
        })
        assert response.status_code == 200
        assert response.json['name'] == 'John Doe'
        
    def test_get_employee_stats(self):
        response = self.client.get('/employees/stats')
        assert response.status_code == 200

        
    def test_api_feeding_schedule(self):
        response = self.client.get('/tasks/feeding')
        assert response.status_code == 200
        
    def test_api_cleaning_schedule(self):
        response = self.client.get('/tasks/cleaning')
        assert response.status_code == 200
        
    def test_api_medical_schedule(self):
        response = self.client.get('/tasks/medical')
        assert response.status_code == 200
        