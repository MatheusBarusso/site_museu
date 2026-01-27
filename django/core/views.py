import random
from django.shortcuts import render
from django.db.models import Q
from item.models import Category, Item, ItemImage, Events

def index(request):
    items_ids = Item.objects.filter(images__isnull=False).values_list('id', flat=True).distinct()
    items_list = list(items_ids)
    random_ids = random.sample(items_list, min(len(items_list), 6))
    random_items = Item.objects.filter(id__in=random_ids)
    return render(request, 'core/index.html', {
        'random_items': random_items,
    })
    

def history(request):
    return render(request, 'core/history.html')

def contact(request):
    return render(request, 'core/contact.html')

def collection(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()
    items = Item.objects.all()

    if category_id and int(category_id) > 0:
        items = items.filter(category_id=category_id)

    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request, 'core/collection.html', {
        'items': items,
        'query': query,
        'categories': categories,
        'category_id': int(category_id),
    })

def events(request):
    events_list = Events.objects.all()
    return render(request, 'core/events.html', {
        'events_list': events_list
    })