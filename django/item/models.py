from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural="Categories" 

    def __str__(self):
        return self.name
    
    
class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.PROTECT)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    manufacturer = models.CharField(blank=True, max_length=255)
    wikipedia = models.URLField(blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='nome_criado', on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class ItemImage(models.Model):
    item = models.ForeignKey(Item, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='item_images')

    def __str__(self):
        return f"Imagem de {self.item.name}"
    

class Events(models.Model):
    name = models.CharField(max_length=255)
    year = models.IntegerField()
    activity = models.TextField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural="Events" 


class EventsImage(models.Model):
    evento = models.ForeignKey(Events, related_name='events_pics', on_delete=models.CASCADE)
    event_image = models.ImageField(upload_to='events_images')


