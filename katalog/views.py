from django.shortcuts import render
from katalog.models import CatalogItem


# TODO: Create your views here.
def show_katalog(request):
    data_barang_katalog = CatalogItem.objects.all()
    context = {
    'list_katalog': data_barang_katalog,
    'nama': 'Abdillah Assajjad',
    'NPM' : "2106653571"
    }
    return render(request, "katalog.html", context)