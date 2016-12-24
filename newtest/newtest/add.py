from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

text = """<form method="post" action="/add/">
    <input type="text" name="a" value="%d"> + <input type="text" name="b" value="%d">
    <input type="submit" value="="> <input type="text" value="%d">
</form>"""


@csrf_exempt
def index(request):
    if 'a' in request.POST:
        a = int(request.POST['a'])
        b = int(request.POST['b'])
    else:
        a = 0
        b = 0
    return HttpResponse(text % (a, b, a + b))