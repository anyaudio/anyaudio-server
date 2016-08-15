import unittest
from tests import YMP3TestCase


class TestGetUrl(YMP3TestCase):
    """
    Test Get download url
    """
    def test_good_get_url(self):
        """test a successful search of a music video"""
        result = self._search('Love Story', just_results=True)
        get_url = result[0]['get_url']
        resp = self.app.get(get_url)
        self.assertEqual(resp.status_code, 200)
        self.assertIn('url', resp.data)


if __name__ == '__main__':
    unittest.main()
