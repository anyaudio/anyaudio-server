import unittest
from tests import YMP3TestCase


class TestDownload(YMP3TestCase):
    """
    Test download
    """
    def test_successful_download(self):
        """test a successful search of a music video"""
        result = self._search('Love Story', just_results=True)
        get_url = result[0]['get_url']
        title = result[0]['title']
        dl_url = self._get_dl_link(get_url, just_url=True)
        resp = self.app.get(dl_url)
        self.assertTrue(len(resp.data) > 100000)
        # test filename
        self.assertIn(title[:10], resp.headers['Content-Disposition'])
        # test file length
        self.assertEqual(int(resp.headers['Content-Length']), len(resp.data))

    def test_failed_download(self):
        """test fail"""
        resp = self.app.get('/api/v1/d/askfasfk')
        self.assertEqual(resp.status_code, 500)
        self.assertTrue(len(resp.data) < 1000)


if __name__ == '__main__':
    unittest.main()
