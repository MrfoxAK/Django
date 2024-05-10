from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
     return render(request, 'shop/index.html')


def about(request):
     return HttpResponse("We are in About")

def contact(request):
     return HttpResponse("We are in Contact")

def tracker(request):
     return HttpResponse("We are in tracker")

def search(request):
     return HttpResponse("We are in search")

def productView(request):
     return HttpResponse("We are in product view")

def checkout(request):
     return HttpResponse("We are in checkout")














