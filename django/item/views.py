from django.shortcuts import render, get_object_or_404
from .models import Category, Item, ItemImage

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category).exclude(pk=pk)[0:3]

    return render(request, 'item/detail.html', {
        'item': item,
        'related_items': related_items
    })

def index(request):
    random_items = Item.objects.filter(images__isnull=False).distinct().order_by('?')[:6]

    return render(request, 'core/index.html', {
        'randon_items':random_items,
    })

