from django.db import models

# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='picture')
    desc=models.TextField()
    price=models.IntegerField()
    offer=models.BooleanField(default=False)

class blog(models.Model):
    title=models.CharField(max_length=200)
    imag=models.ImageField(upload_to='picture')
    category=models.TextField()
    text=models.TextField()
    date=models.IntegerField()
    month=models.TextField(max_length=10)