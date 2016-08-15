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
        dl_url = self._get_dl_link(get_url, just_url=True)
        resp = self.app.get(dl_url)
        self.assertTrue(len(resp.data) > 100000)


if __name__ == '__main__':
    unittest.main()
