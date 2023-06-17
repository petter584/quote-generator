import unittest
from flask import Flask
from flask_testing import TestCase
from main import app, get_random_quote

class QuoteGeneratorTests(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_main_route(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_hello_route(self):
        response = self.client.get('/hello')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'greeting': 'Hello world!'})

    def test_quote_route(self):
        response = self.client.get('/quote')
        self.assertEqual(response.status_code, 200)
        self.assertIn('quote', response.json)

    def test_get_random_quote(self):
        quote = get_random_quote()
        self.assertIsInstance(quote, str)

if __name__ == '__main__':
    unittest.main()
