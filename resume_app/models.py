from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    skills = models.CharField(max_length=200)
    education = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)

    def save(self, *args, **kwargs):
        if self.user is None:
            self.user = User.objects.get(username='default')
        super(Customer, self).save(*args, **kwargs)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
