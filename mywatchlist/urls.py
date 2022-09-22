from django.urls import path
from mywatchlist.views import * 
#sesuaikan dengan nama fungsi yang dibuat

app_name = 'mywatchlist'

urlpatterns = [
    path('', show_mywatchlist, name='show_mywatchlist'),
    path('html/', show_mywatchlist, name='show_mywatchlist'),
    path('xml/', show_mywatchlist_by_xml, name='show_mywatchlist_by_xml'),
    path('json/', show_mywatchlist_by_json , name='show_mywatchlist_by_json'),
    path('xml/<int:id>', show_mywatchlist_by_xml_id, name='show_mywatchlist_by_xml_id'),
    path('json/<int:id>', show_mywatchlist_by_json_id, name='show_mywatchlist_by_xml_id'),
]