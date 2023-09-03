from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class User(models.Model):
    # user=models.OneToOneField(user,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, null=False)
    father_name = models.CharField(max_length=100, null=False)
    grandfather_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, unique=True, null=False)
    phone_number = models.CharField(max_length=20, null =False)
    password = models.CharField(max_length=100, null=False)
    registration_date = models.DateTimeField(auto_now_add=True)
   
    @property
    def get_name(self):
        return self.User.first_name+" "+self.User.father_name+" "+self.User.grandfather_name
    @property
    def get_id(self):
        return self.User.id
    def __str__(self):
        return self.User.first_name