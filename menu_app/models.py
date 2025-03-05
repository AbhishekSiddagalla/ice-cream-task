from django.db import models


class IceCreamInfo(models.Model):
    ice_cream_flavour = models.CharField(max_length=64,default=None,null=True)
    ice_cream_name = models.CharField(max_length=64,default=None,null=True)
    ice_cream_weight = models.IntegerField(default=None,null=True)
    entry_date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.ice_cream_name} - {self.ice_cream_flavour} - {self.ice_cream_weight}"
