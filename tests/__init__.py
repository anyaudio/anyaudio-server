import unittest
import json
# import os
from ymp3 import app


class YMP3TestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        # DATABASE_PATH = 'test.db'
        self.app = app.test_client()

    def _search(self, term, just_results=False):
        """
        searches and returns the result
        :just_results - If true, return results dict
        """
        resp = self.app.get('/api/v1/search?q=%s' % term)
        self.assertEqual(resp.status_code, 200)
        if just_results:
            return json.loads(resp.data)['results']
        else:
            return resp.data

    def tearDown(self):
        pass
        # if os.path.isfile('test.db'):
        #     os.unlink('test.db')
