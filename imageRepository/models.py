from django.db import models

class User(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length = 255)
    
    def __str__(self):
        return self.name
    
class Image(models.Model):
    name = models.CharField(max_length = 30)
    description = models.CharField(max_length = 125)
    category = models.CharField(max_length = 30)
    date_published = models.DateField()
    path = models.CharField(default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class Location(models.Model):
    name = models.CharField(max_length = 30)
    x = models.FloatField()
    y = models.FloatField()
    image = models.OneToOneField(Image, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
