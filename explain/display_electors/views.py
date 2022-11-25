from django.shortcuts import render
#from django.http import HttpResponse
#from django.template import loader
#from django.http import HttpResponse
from .models import Territories , TerritoriesParents


# Create your views here.




def index(request):
    territories = Territories.objects.all()
    return render(request, 'display_electors/index.html'  , {'territories' : territories })

""" def index(request):
    territories = Territories.objects.order_by('name')
    return render(request, 'display_electors/index.html'  , {'territories' : territories }) """

""" def index(request):
    territories = Territories.objects.order_by('id')
    return render(request, 'display_electors/index.html'  , {'territories' : territories })
 """
""" def index(request):
    territories = Territories.objects.order_by('kind')
    return render(request, 'display_electors/index.html'  , {'territories' : territories })
 """
""" def index(request):
    territories = Territories.objects.order_by('code')
    return render(request, 'display_electors/index.html'  , {'territories' : territories })
 """



 