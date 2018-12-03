from django.contrib.auth.models import User
from django.db import models


class CsvUpload(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    csv_name = models.CharField(max_length=100)
    csv_file = models.FileField()
    data_processed = models.BooleanField(default=False)
    error = models.BooleanField(default=False)
