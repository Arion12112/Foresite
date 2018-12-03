from django.shortcuts import render

from .forms import CsvUploadForm


def upload_csv_file(request):
    if not request.user.is_authenticated:
        return render(request, 'upload_csv/please_log_in.html')
    else:
        if request.method == "POST":
            form = CsvUploadForm(request.POST or None, request.FILES or None)
            if form.is_valid():
                file = form.save(commit=False)
                file.user = request.user
                file.csv_file = request.FILES['csv_file']
                file.csv_name = request.FILES['csv_file'].name
                file.save()
                return render(request, 'upload_csv/upload_csv_success.html',
                              {'form': form})
            else:
                return render(request, 'upload_csv/upload_csv_failed.html')
        else:
            form = CsvUploadForm()
            return render(request, 'upload_csv/upload_csv.html',
                          {'form': form})
