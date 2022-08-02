from django.db import models

class Members(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    height = models.CharField(max_length=10, null=True, blank=True)
    weight = models.CharField(max_length=10, null=True, blank=True)
    creation_date = models.DateField(auto_now_add=True, null=True, blank=True)
