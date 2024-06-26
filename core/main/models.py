from django.db import models
from django.utils.text import slugify


class Menu(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    dishes = models.ManyToManyField('MenuItem')

    def __str__(self) -> str:
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    photo = models.ImageField(upload_to='media')
    price = models.IntegerField()
    category = models.ForeignKey('Category', on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
    

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
 
    def __str__(self) -> str:
        return self.name
        
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)