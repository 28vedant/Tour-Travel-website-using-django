from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class CustomManger(models.Manager):
    def india_list(self):
        return self.filter(category__exact="India")
    def europe_list(self):
        return self.filter(category__exact="Europe")
    def thailand_list(self):
        return self.filter(category__exact="Thailand")
    def malaysia_list(self):
        return self.filter(category__exact="Malaysia")


class Pakage(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    pid = models.IntegerField(primary_key=True)
    pname = models.CharField(max_length=100)
    type =  (
        ("India", "India"),
        ("Europe", "Europe"),
        ("Thailand", "Thailand"),
        ("Malaysia", "Malaysia"),
    )
    category = models.CharField(max_length=50, choices=type, default="")

    pprice = models.IntegerField()
    pdescription = models.TextField()
    pimage = models.ImageField(upload_to='pakageimages')
    objects = models.Manager()
    pakagemanger = CustomManger()



class TourCart(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    pid = models.ForeignKey(Pakage, on_delete=models.CASCADE, null=True)
    qty = models.PositiveIntegerField(default=0)
    

class Order(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    pid = models.ForeignKey(Pakage, on_delete=models.CASCADE, null=True)
    orderid = models.IntegerField(primary_key=True)
    qty = models.PositiveIntegerField(default=0)
   