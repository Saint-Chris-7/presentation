
from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.




class Stock(models.Model):
    tags =[

        ("cereals", "cereals"),
        ("flour", "flour"),
        ("fat_oils", "fat_oils"),
        ("dairy", "dairy"),
     
    ]
    storage =[
        ("freezer", "freezer"),
        ("dry", "dry"),
        ("low", "low"),
        ("air_tight", "air_tight"),
        ("canned", "canned")
    ]
    company = "ABC"

    product_name = models.CharField(verbose_name="product name",max_length=100)
    net_weight = models.PositiveIntegerField(verbose_name="weight in tonnes")
    qty = models.PositiveIntegerField(verbose_name="quantity")
    date = models.DateField(verbose_name="date of stock",auto_created=True,auto_now_add=True)
    isle = models.PositiveIntegerField(verbose_name="shelf no:",default=0)
    tags = models.CharField(verbose_name="select tag",max_length=50,choices=tags)
    storage = models.CharField(verbose_name="storage conditions",max_length=50,choices=storage)
    shelf_life = models.CharField(verbose_name="shelf life",max_length=50,blank=True)
    exp = models.DateField(verbose_name="Expiry date",null=True)
    attendant = models.ForeignKey(to=User,related_name="handler",on_delete = models.CASCADE,verbose_name="handler",default=1)
    status = models.CharField(verbose_name="comment",max_length=25,null=True)
    docs = models.FileField(upload_to="documents",verbose_name="documentation",null=True,max_length=100)

    def __str__(self) -> str:
        return f"{self.product_name}"
    
    @classmethod
    def company(cls):
        return cls.company

    @staticmethod
    def get_date():
        return datetime.today()


    class Meta:
        permissions =[
            ("can_allow_dispatch", "can allow dispatch"),
            ("can_make_reorders", "can make new orders"),
        ]
        ordering = ["-product_name","-date"]
    
    def get_absolute_url(self):
        return reverse("shop:detail-page",kwargs={"pk":self.pk})



    




    


    
