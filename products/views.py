from django.shortcuts import render
from django.http import HttpResponse




"""
A---->B------> une instruction | instruction 
2-2 | *4 ---------->0
"""
#ULR et Request
def home(request, *args, **kwargs):
    mylist = [45, 66, 676, 67]
    nom = "donald"
    return render(request, 'index4.html', {"list":mylist, 'nom':nom})


def contact(request):
    return render(request, 'contact.html')

def blog(request):
    return HttpResponse("blog page")        