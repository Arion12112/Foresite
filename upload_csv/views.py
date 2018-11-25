from django.shortcuts import render

from .forms import CsvUploadForm


def upload_csv_file(request):
    if not request.user.is_authenticated:
        return render(request, 'registration/login.html')
    else:
        form = CsvUploadForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            file = form.save(commit=False)
            file.user = request.user
            file.csv_file = request.FILES['csv_file']
            file.save()
            return render(request, 'upload_csv/upload_csv_success.html')
        else:
            return render(request, 'upload_csv/upload_csv_failed.html')
