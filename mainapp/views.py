# pylint: disable=C
from django.shortcuts import render  # pylint: disable=import-error
# from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView  # pylint: disable=import-error
from .models import Device, Card


def index_view(request):
    # return HttpResponse("<h1>Начальная страница</h1>")
    cards = Card.objects.all()
    return render(request, "mainapp/index.html", {'cards': cards})


class DeviceListView(ListView):  # pylint: disable=too-few-public-methods
    model = Device


class DeviceDetailView(DetailView):  # pylint: disable=too-few-public-methods
    model = Device


class DeviceCreateVIew(CreateView):  # pylint: disable=too-few-public-methods
    model = Device
    fields = '__all__'
    success_url = '/device-list/'
