from django.db import models

# Create your models here.

class Clint(models.Model): 
    preview = models.ImageField(upload_to='clint/', null = False, blank = False)
    created = models.DateTimeField(auto_now_add=True)  
    updated = models.DateTimeField(auto_now=True)  

    class Meta:
        verbose_name = 'Our Clint'
        verbose_name_plural = 'Our Clints'