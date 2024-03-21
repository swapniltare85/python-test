
from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def home(request):
    peoples=[
        {'name':'Swapnil Tare', 'age':30},
        {'name':'Dev patil', 'age':33},
        {'name':'Aman Tare', 'age':18},
        {'name':'Sacin Tendulkar', 'age':34},
        {'name':'Shewta Patil', 'age':14},
    ]

    for people in peoples:
        if people['age']:
           print ('Yes')
    vegetable=['abc', 'tomato', 'potato']
    
    return render(request, "index.html", context={'page':'Django tutorial 2023','peoples':peoples, 'vegetable':vegetable})
    


def about(request):
    context={'page':'About'}
    return render(request, "about.html", context)

def contact(request):
    context={'page':'Contact'}
    return render(request, "contact.html", context)


def success_page(request):
    # print("*"*10)
    return HttpResponse("<h1>Hey This is success Page.</h1>")

