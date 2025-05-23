from django.shortcuts import render

# Create your views here.
from .models import Consulta


# Create your views here.
def lista_consultas(request):
    consultas = Consulta.objects.all()
    return render(request, 'consulta/consulta_list.html', {'consulta': consulta})