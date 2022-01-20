from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    response = "<p>Rango says hey there partner!</p><br>"
    response += "<a href='about/'>go to about</a>"
    return HttpResponse(response)
    
def about(request):
    response = "<p>Rango says here is the about page.</p><br>"
    response += "<a href='../'>go to index</a>"
    return HttpResponse(response)