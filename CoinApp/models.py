from django.db import models

# Create your models here.


class Group(models.Model):
    group_name = models.CharField(max_length=128)

    def __str__(self):
        return self.group_name

class Student(models.Model):
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, default=None, null=True)
    email = models.EmailField(blank=True)
    name = models.CharField(max_length=128)
    finCoins = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Equities(models.Model):
    company_name = models.CharField(max_length=128)
    price = models.IntegerField()
