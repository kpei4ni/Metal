from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'base.html')

def lol(request):
    return HttpResponse('<h1>ЖЕКА LOL</h1> <a href="/"></a>')