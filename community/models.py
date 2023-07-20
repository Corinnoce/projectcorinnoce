from django.db import models

# Create your models here.
from accounts.models import Crypto


class Collection (models.Model):
    user = models.ForeignKey(Crypto,on_delete=models.CASCADE,default=None)
    slug = models.SlugField()

"""
class UserAcesspreminium(models.Model):
    user = models.OneToOneField(Crypto, on_delete=models.CASCADE)
    start_order = models.DateTimeField(auto_now=False)
    expire_at = models.DateTimeField(auto_now=False)
    expire = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.user.username(self.start_order)}"
"""
