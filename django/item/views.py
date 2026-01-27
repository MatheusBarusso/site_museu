from django.shortcuts import render, get_object_or_404
from .models import Category, Item, ItemImage, Events, EventsImage

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

def event_detail(request, pk):
    evento = get_object_or_404(Events, pk=pk)
    return render(request, 'item/event_detail.html', {
        'evento': evento,
    })

