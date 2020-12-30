from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

# this model Stores the data of the Phones Verified
class phoneModel(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=15, blank=False,unique=True,verbose_name='Phone',default='+999999999')
    isVerified = models.BooleanField(blank=False, default=False)
    counter = models.IntegerField(default=0, blank=False)   # For HOTP Verification
    def __str__(self):
        return str(self.phone_number)