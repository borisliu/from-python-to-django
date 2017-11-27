from django.views import generic

from .models import Address

class IndexView(generic.ListView):
    model = Address
    template_name = 'address/index.html'
