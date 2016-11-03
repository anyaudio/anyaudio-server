import unittest
import requests
from tests import YMP3TestCase


class TestDownload(YMP3TestCase):
    """
    Test download
    """
    def test_successful_download(self):
        """test successful download of a music video"""
        result = self._search('Payphone Maroon 5', just_results=True)
        get_url = result[0]['get_url']
        title = result[0]['title']
        dl_url = self._get_dl_link(get_url, just_url=True) + '&format=mp3'
        resp = self.app.get(dl_url)
        self.assertTrue(len(resp.data) > 100000, resp.data)
        # test filename
        self.assertIn(title[:10], resp.headers['Content-Disposition'], resp.headers)
        # test file length
        self.assertEqual(int(resp.headers['Content-Length']), len(resp.data))

    def test_failed_download(self):
        """test fail"""
        resp = self.app.get('/api/v1/d?url=askfasfk')
        self.assertEqual(resp.status_code, 500)
        self.assertTrue(len(resp.data) < 1000)

    def test_successful_download_m4a(self):
        """test successful download of a music in m4a"""
        # search and get link
        result = self._search('Payphone Maroon 5', just_results=True)
        get_url = result[0]['get_url']
        dl_url = self._get_dl_link(get_url, just_url=True) + '&format=m4a'
        resp = self.app.get(dl_url)
        # test
        self.assertTrue(len(resp.data) > 100000, resp.data)
        self.assertEqual(int(resp.headers['Content-Length']), len(resp.data))
        self.assertIn(
            '.m4a', resp.headers['Content-Disposition'], resp.headers['Content-Disposition']
        )


class TestDownloadV2(YMP3TestCase):
    def test_successful_download(self):
        result = self._search_v2('Payphone Maroon 5', just_results=True)
        get_url = result[0]['get_url']
        # title = result[0]['title']
        dl_url = self._get_dl_link(get_url, just_url=True)
        resp = requests.get(dl_url)
        self.assertTrue(len(resp.content) > 100000, resp)


if __name__ == '__main__':
    unittest.main()
