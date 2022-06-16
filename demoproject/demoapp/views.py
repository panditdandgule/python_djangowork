from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def appurlinfo(request):
    s='<h1>application url demo</h1>'
    return HttpResponse(s)

