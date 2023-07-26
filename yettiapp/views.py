from django.http import HttpResponse

def index(request):
    return HttpResponse('helllo')

def index2(request):
    return HttpResponse('vay')