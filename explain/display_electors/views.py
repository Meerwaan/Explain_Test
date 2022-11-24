from django.shortcuts import render
#from django.http import HttpResponse
#from django.template import loader
#from django.http import HttpResponse
from .models import Territories , TerritoriesParents


# Create your views here.

""" def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render()) """


def index(request):
    return render(request, 'display_electors/index.html' )