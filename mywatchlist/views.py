from django.shortcuts import render
from mywatchlist.models import WishlistAbdi


# Create your views here.
def show_mywatchlist(request):
    data_barang_film = WishlistAbdi.objects.all()
    context = {
        'list_film': data_barang_film,
        'nama': 'Abdi'
    }
    return render(request, "mywatchlist.html", context)