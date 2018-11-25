from django import forms

from .models import CsvUpload


class CsvUploadForm(forms.Form):

    class Meta:
        model = CsvUpload
        field = ['csv_name', 'csv_file']
