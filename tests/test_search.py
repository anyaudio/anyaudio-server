import unittest
import json
from tests import YMP3TestCase


class TestSearch(YMP3TestCase):
    """
    Test Search feature
    """
    def successful_search_test(self, version):
        """test a successful search of a music video"""
        result = self._search('Numb', version=version)
        self.assertIn('Numb', result)
        self.assertIn('Linkin Park', result)
        data = json.loads(result)
        self.assertEqual(len(data['results']), data['metadata']['count'])
        self.assertTrue(len(data['results']) >= 10, result)

    def test_successful_search_v1(self):
        self.successful_search_test('v1')

    def test_successful_search_v2(self):
        self.successful_search_test('v2')

    def test_long_video_not_returned(self):
        """test search of a term which usually will have long videos as results"""
        resp = self.app.get('/api/v1/search?q=mashup nonstop')
        data = json.loads(resp.data)
        self.assertTrue(len(data['results']) < 13)


if __name__ == '__main__':
    unittest.main()
