from django.shortcuts import render
from mywatchlist.models import WatchlistAbdi
from django.http import HttpResponse
from django.core import serializers

data = WatchlistAbdi.objects.all()

# Create your views here.
def show_mywatchlist(request):
    data_film = WatchlistAbdi.objects.all()
    context = {
        'list_film': data_film,
        'nama': 'Abdi'
    }
    return render(request, "mywatchlist.html", context)

def show_mywatchlist_by_xml(request):
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_mywatchlist_by_json(request):
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_mywatchlist_by_xml_id(request, id):
    dataid = WatchlistAbdi.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", dataid), content_type="application/xml")

def show_mywatchlist_by_json_id(request, id):
    dataid = WatchlistAbdi.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", dataid), content_type="application/json")
