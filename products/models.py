from django.db import models

# Create your models here.
class product(models.Model):
    name = models.CharField(max_length= 50)
    descrip = models.TextField()
    price = models.IntegerField()
    picture = models.ImageField(upload_to='profiles/')
    creat_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now_add=True)