from django.http.response import HttpResponse
from django.http import HttpResponse
from django.template import loader
from ToDo.models import *
# Create your views here.
def show_list(request):
    list = List.objects.all()
    template = loader.get_template('list.html')
    context = {
        'list' : list,
    }
    result = template.render(context=context, request=request)
    return HttpResponse(result)

def show_items(request,id):
    list = List.objects.get(id=id)
    items = Item.objects.all().filter(list_id=id)
    template = loader.get_template('items.html')
    context = {
         'list': list,
         'items': items,
    }
    result = template.render(context=context, request=request)
    return HttpResponse(result)