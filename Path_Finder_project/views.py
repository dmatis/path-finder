from django.http import HttpResponse
from django.shortcuts import render
from bikeways.coordinates import getCoordsWithID


def home(request):
    return render(request, 'bikeways/home.html')

def coordwithid_test(request):
    coord = getCoordsWithID()
    return HttpResponse(coord, content_type='application/json')

def about(request):
    return render(request, "about.html", {})
