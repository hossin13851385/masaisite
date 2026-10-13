from django.db import models

# Create your models here.
class product(models.Model):
    name = models.CharField(max_length= 50)
    category = models.ForeignKey(
        "category",
        on_delete=models.SET_NULL,
        null=True,
        related_name="products"
    )
    descrip = models.TextField()
    price = models.IntegerField()
    picture = models.ImageField(upload_to='profiles/')
    creat_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
            return self.name



class category(models.Model): 
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    parent = models.ForeignKey("self" , on_delete=models.SET_NULL , null=True , blank=True)
    imagefilde = models.ImageField(upload_to='category/')
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
