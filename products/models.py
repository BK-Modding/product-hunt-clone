from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()
    pub_date = models.DateField()
    votes_total = models.IntegerField(default=1)
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='images/icons/')
    body = models.TextField()
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]