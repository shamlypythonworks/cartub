from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from . models import *
# Create your views here.
def home(request,c_slug=None):
    categ = Category.objects.all()
    if c_slug!= None:
        catnm = get_object_or_404(Category,slug=c_slug)
        prod = products.objects.all().filter(categ=catnm)
    else:
         prod = products.objects.all()
    return render(request,'index.html',{'categs':categ,'prods':prod})
def contact(request):
    return render(request,'contact.html')
def searching(request):
    prod=None
    searchele = None
    if 'q' in request.GET:
        searchele = request.GET.get('q')
        prod=products.objects.all().filter(Q(name__contains=searchele))
    return render(request, 'search.html', {'qr': searchele, 'pr': prod})