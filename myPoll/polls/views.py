from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello World, We're at the polls index")
