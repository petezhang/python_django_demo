from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import JsonResponse

# Create your views here.
def index(request):
    # return HttpResponse('hello world')
    return render(request,'index.html')

def setUserName(req):
    return JsonResponse({
        'data':'200'
    })
