from django.db import models
from django.contrib.auth.models import User


class Data(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    txt_file_name = models.CharField(max_length=15)
    timestamp = models.DateTimeField(auto_now_add=True)
    timestep = models.PositiveSmallIntegerField()
    s3_location = models.CharField(max_length=30)
    data_processed = models.BooleanField(default=False)
    data_processed_error = models.BooleanField(default=False)
