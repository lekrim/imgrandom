from django.db import models

# Create your models here.
class Image(models.Model):
    img_type = models.CharField(max_length=25)
    img_size = models.CharField(max_length=25)
    img_category = models.CharField(max_length=25)
    img_name =  models.CharField(max_length=50)

    def __str__(self):
        return self.img_name # add s prefix to admin sitepy