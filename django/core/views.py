from django.shortcuts import render
from item.models import Category, Item, ItemImage

def index(request):
    random_items = Item.objects.filter(images__isnull=False).distinct().order_by("?")[0:6]
    
    return render(request, 'core/index.html', {
        'random_items': random_items,
    })

def history(request):
    return render(request, 'core/history.html')

def contact(request):
    return render(request, 'core/contact.html')

def collection(request):
    items = Item.objects.all()
    return render(request, 'core/collection.html', {
        'items': items,
    })