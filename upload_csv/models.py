from django.contrib.auth.models import User
from django.db import models


def csv_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class CsvUpload(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    csv_name = models.CharField(max_length=20)
    csv_file = models.FileField(upload_to=csv_directory_path)
    csv_path = models.CharField(max_length=100, default=csv_directory_path)
    data_processed = models.BooleanField(default=False)
    error = models.BooleanField(default=False)
