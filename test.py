import unittest
from flask import Flask
from main import paralVolume, sphereVolume, coneVolume, cylinderVolume


class TestVolumeCalculator(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_int(self):
        with self.app.test_request_context('/paral', method='POST', data={'num_1': '5', 'num_2': '6', 'num_3': '8', 'e': '3'}):
            response = paralVolume()
            self.assertIn('Ответ: 240', response)
    def test_float(self):
        with self.app.test_request_context('/sphere', method='POST', data={'num_1': '7.8', 'e': '3'}):
            response = sphereVolume()
            self.assertIn('Ответ: 1987.799', response)

    def test_without_data(self):
        with self.app.test_request_context('/sphere', method='POST', data={'num_1': '', 'e': ''}):
            response = sphereVolume()
            self.assertIn('Введены не все значения', response)

    def test_minus(self):
        with self.app.test_request_context('/sphere', method='POST', data={'num_1': '-7', 'e': '3'}):
            response = sphereVolume()
            self.assertIn('Некорректный ввод', response)

    def test_letters_data(self):
        with self.app.test_request_context('/cone', method='POST', data={'num_1': 'five', 'num_2': 'nine', 'e': 'one'}):
            response = coneVolume()
            self.assertIn('Некорректный ввод', response)

    def test_comma_data(self):
        with self.app.test_request_context('/cylinder', method='POST', data={'num_1': '7,9', 'num_2': '4,1', 'e': '5'}):
            response = cylinderVolume()
            self.assertIn('Некорректный ввод', response)

    def test_float_e(self):
        with self.app.test_request_context('/cylinder', method='POST', data={'num_1': '9', 'num_2': '4', 'e': '5.4'}):
            response = cylinderVolume()
            self.assertIn('Некорректный ввод', response)


if __name__ == '__main__':
    unittest.main()
