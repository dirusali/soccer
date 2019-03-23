from django.http import HttpResponse

from templates import partidos.html

def home(request):
    return HttpResponse(partidos.html)
