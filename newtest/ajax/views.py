# Create your views here.
from django.http import HttpResponse

def input(request):
    input = request.GET["input"]
    return HttpResponse('<p>You input is "%s"</p>' % input)