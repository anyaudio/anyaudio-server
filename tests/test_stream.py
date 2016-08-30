import unittest
import json
from tests import YMP3TestCase


class TestStream(YMP3TestCase):
    """
    Test Streaming feature
    """
    def test_good_stream(self):
        """test a successful stream of a music video"""
        result = self._search('Love Story', just_results=True)
        stream_url = result[0]['stream_url']
        resp = self.app.get(stream_url)
        self.assertEqual(resp.status_code, 200)
        self.assertIn('/stream_handler?', resp.data)
        # stream and download audio
        final_url = json.loads(resp.data)['url']
        resp = self.app.get(final_url)
        self.assertTrue(len(resp.data) > 1000 * 1000)

    def test_fake_stream_url(self):
        """test the 5xx response in case of fake stream url"""
        resp = self.app.get('/api/v1/stream?url=somefalseurl')
        self.assertEqual(resp.status_code, 500)


if __name__ == '__main__':
    unittest.main()
