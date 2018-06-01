from django.shortcuts import render
from .models import sample_model


def index(request):
    objectt = sample_model.objects.all()
    return render(request,'index.html' , {'objectt': objectt})