from django.contrib import admin
from .models import Category, Item, ItemImage, Events, EventsImage

class ItemImageInline(admin.TabularInline):
    model = ItemImage
    extra = 1

class ItemAdmin(admin.ModelAdmin):
    inlines = [ItemImageInline]

class EventsImageInline(admin.TabularInline):
    model = EventsImage
    extra = 1

class EventAdmin(admin.ModelAdmin):
    inlines = [EventsImageInline]

admin.site.register(Category)
admin.site.register(Item, ItemAdmin)
admin.site.register(Events, EventAdmin)

