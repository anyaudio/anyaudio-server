import unittest
# import os
from ymp3 import app


class YMP3TestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        # DATABASE_PATH = 'test.db'
        self.app = app.test_client()

    def tearDown(self):
        pass
        # if os.path.isfile('test.db'):
        #     os.unlink('test.db')
