from django.http import HttpResponse
from django.shortcuts import render



def index(request):
     return render(request, 'index.html')


def facebook(request):
     return render(request, 'facebook.html')

def instagram(request):
     return render(request, 'instagram.html')













