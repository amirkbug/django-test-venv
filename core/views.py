from django.http import HttpResponse

def home(request):
    return HttpResponse("salap")

def connect(request):
    return HttpResponse("connect shodi")