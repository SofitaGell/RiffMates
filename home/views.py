from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def credits(request):
    content = "Nicky\nSofitaGell"
    return HttpResponse(content, content_type="text/plain")
