# I have created this website - AKASH
from django.http import HttpResponse
from django.shortcuts import render

def index(reuqest):
     return render(reuqest, 'index.html')
def i(reuqest):
     return render(reuqest, 'i.html')
     # return HttpResponse("Home")


def analyze(request):
     t = request.POST.get('text','default')
     removepunc = request.POST.get('removepunc','default')
     print(t)
     if removepunc == "on":
          punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
          analyzed = ""
          for i in t:
               if i not in punctuations:
                    analyzed = analyzed + i
          params = {'purpose': 'Removed Puncuations', 'analyzed_text':analyzed}
          return render(request, 'analyze.html', params)
     else:
          return HttpResponse("Error")
# def capfirst(request):
#      return HttpResponse("Cap")

# def charcount(request):
#      return HttpResponse("char count")

# def newlineremove(request):
#      return HttpResponse("new line remove")


