from django.db import models

# Create your models here.


class MyGenericModel(models.Model):
    theFile = models.FileField(upload_to='media/files/',default='aa',blank=True)
    firebase_id_token = models.CharField(max_length=50)