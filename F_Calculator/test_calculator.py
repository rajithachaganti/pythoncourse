import json
import unittest

from calculator import app


class TestCalculator(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print('Set up class')
        self.client = app.test_client()

    @classmethod
    def tearDownClass(self):
        print('Tear down class')

    def test_add(self):
        response = self.client.post('/add',
                                    data=json.dumps({'argument1': 5, 'argument2': 3}),
                                    headers={"Content-Type": "application/json"})
        pdb.set_trace()
        self.assertEqual(response.status_code, 200)

    def test_subtract(self):
        response = self.client.post('/subtract', data=json.dumps({'argument1': '5', 'argument2': '3'}),
                                    headers={"Content-Type": "application/json"})
        self.assertEqual(response.status_code, 200)

    def test_multiply(self):
        response = self.client.post('/multiply', data=json.dumps({'argument1': '5', 'argument2': '3'}),
                                    headers={"Content-Type": "application/json"})
        self.assertEqual(response.status_code, 200)

    def test_divide(self):
        response = self.client.post('/divide', data=json.dumps({'argument1': '15', 'argument2': '3'}),
                                    headers={"Content-Type": "application/json"})
        self.assertEqual(response.status_code, 200)

    def test_mod(self):
        response = self.client.post('/mod', data=json.dumps({'argument1': '15', 'argument2': '2'}),
                                    headers={"Content-Type": "application/json"})
        self.assertEqual(response.status_code, 200)

    def test_exp(self):
        response = self.client.post('/exp', data=json.dumps({'argument1': '5', 'argument2': '3'}),
                                    headers={"Content-Type": "application/json"})
        self.assertEqual(response.status_code, 200)

    def test_average(self):
        response = self.client.post('/average', data=json.dumps({'argument1': '15', 'argument2': '3'}),
                                    headers={"Content-Type": "application/json"})
        self.assertEqual(response.status_code, 200)

    def test_fail_add(self):
        response = self.client.post('/add', data=json.dumps({'argument1': 'five', 'argument2': '3'}),
                                    headers={"Content-Type": "application/json"})
        self.assertEqual(response.status_code, 400)

    def test_fail_sub(self):
        response = self.client.post('/add', data=json.dumps({'argument1': '10', 'argument2': 'three'}),
                                    headers={"Content-Type": "application/json"})
        self.assertEqual(response.status_code, 400)


if __name__ == '__main__':
    unittest.main()
