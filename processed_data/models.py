from django.db import models
from upload_csv.models import CsvUpload


class ProcessedData(models.Model):
    upload_csv_processed = models.OneToOneField(
        CsvUpload, on_delete=models.CASCADE, primary_key=True)
    day_1 = models.FloatField(null=True, blank=True, default=None)
    day_2 = models.FloatField(null=True, blank=True, default=None)
    day_3 = models.FloatField(null=True, blank=True, default=None)
    day_4 = models.FloatField(null=True, blank=True, default=None)
    day_5 = models.FloatField(null=True, blank=True, default=None)
    day_6 = models.FloatField(null=True, blank=True, default=None)
    day_7 = models.FloatField(null=True, blank=True, default=None)
    image_path = models.CharField(max_length=100, default=None)
