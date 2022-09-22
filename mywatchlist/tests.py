from django.test import SimpleTestCase
from django.urls import reverse, resolve
from mywatchlist.views import show_mywatchlist, show_mywatchlist_by_xml, show_mywatchlist_by_json


# Create your tests here.
class TestUrls(SimpleTestCase):
    def test_show_mywatchlist_url(self):
        url = reverse('mywatchlist:show_mywatchlist')
        self.assertEqual(resolve(url).func, show_mywatchlist)

    def test_show_mywatchlist_by_xml_url(self):
        url = reverse('mywatchlist:show_mywatchlist_by_xml')
        self.assertEqual(resolve(url).func, show_mywatchlist_by_xml)

    def test_show_mywatchlist_by_json_url(self):
        url = reverse('mywatchlist:show_mywatchlist_by_json')
        self.assertEqual(resolve(url).func, show_mywatchlist_by_json)