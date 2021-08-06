from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseNotFound
from .models import Phone

def index(request):
    return redirect(reverse(show_catalog))

def show_catalog(request):
    sort = request.GET.get('sort')
    if sort == 'min_price':
        phones = Phone.objects.order_by('price')
    elif sort == 'max_price':
        phones = Phone.objects.order_by('-price')
    else:
        phones = Phone.objects.order_by('name')

    template = 'catalog.html'
    context = {
        'phones': phones
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    try:
        phone = Phone.objects.get(slug=slug)
    except ObjectDoesNotExist:
        return HttpResponseNotFound('Phone not found')
    context = {'phone': phone}
    return render(request, template, context)