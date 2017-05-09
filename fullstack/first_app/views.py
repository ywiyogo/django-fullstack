from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    my_dict = {'insert_me': "Hello Y !"}
    return render(request, "first_app/index.html", context=my_dict)
