from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    Name = models.CharField(max_length=50) 


class Ad(models.Model):
    Title = models.CharField(max_length=100)
    Description = models.CharField(max_length = 500)
    Category = models.ForeignKey(Category, on_delete = models.DO_NOTHING)
    Сreated_at = models.DateField(default=None)
    User = models.ForeignKey(User, on_delete = models.CASCADE, default=None, null=True)
    Сondition = models.CharField(max_length=100)

class Status(models.Model):
    status = models.CharField(max_length=50)
class ExchangeProposal(models.Model):
    ad_sender_id =  models.ForeignKey(Ad, on_delete = models.CASCADE, related_name = 'sender')
    ad_receiver_id = models.ForeignKey(Ad, on_delete = models.CASCADE, default=None, null=True)
    status = models.ForeignKey(Status, on_delete = models.DO_NOTHING)
    comment = models.CharField(max_length=200)
    сreated_at = models.DateField(default=None)
