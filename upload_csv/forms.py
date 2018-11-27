from django import forms

from .models import CsvUpload


class CsvUploadForm(forms.ModelForm):
    csv_name = forms.CharField(
        required=True,
        max_length=20,
        widget=forms.TextInput(
            attrs={
                'class': "input is-primary",
                'placeholder': "CSV file name"
            }
        )
    )
    csv_file = forms.FileField()

    class Meta:
        model = CsvUpload
        fields = [
            'csv_name',
            'csv_file'
        ]
