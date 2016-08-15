import unittest
import json
from tests import YMP3TestCase


class TestSearch(YMP3TestCase):
    """
    Test Search feature
    """
    def test_successful_search(self):
        resp = self.app.get('/api/v1/search?q=Numb')
        self.assertEqual(resp.status_code, 200)
        self.assertIn('Numb', resp.data)
        self.assertIn('Linkin Park', resp.data)
        data = json.loads(resp.data)
        self.assertEqual(len(data['results']), data['metadata']['count'])
        self.assertTrue(len(data['results']) > 15, resp.data)


if __name__ == '__main__':
    unittest.main()
