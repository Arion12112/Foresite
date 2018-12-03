from django import forms

from .models import CsvUpload


class CsvUploadForm(forms.ModelForm):
    csv_file = forms.FileField()

    class Meta:
        model = CsvUpload
        fields = [
            'csv_file'
        ]
