from django.db import models

# Create your models here.


class subscriber(models.Model):
    email = models.CharField(max_length = 255 , unique=True)
    
    def __str__(self):
        return self.email
    
    
class respos(models.Model):
    name = models.CharField(max_length = 255 )
    surname = models.CharField(max_length = 255 )
    email = models.CharField(max_length = 255 )
    phone_number = models.CharField(max_length = 255 )
    city = models.CharField(max_length = 255 )
    
    
    def __str__(self):
        return self.name
    
class banque_info(models.Model):
    content = models.TextField()
    
    
    
