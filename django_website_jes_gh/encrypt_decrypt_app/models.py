from django.db import models
from .simple_encryption import *

# Create your models here.
class Cryption(models.Model):
    message = models.TextField()
    start_key = models.IntegerField()
    key_increment = models.IntegerField()
    key_increments_increment = models.IntegerField()
    
    def __str__(self):
        return self.message