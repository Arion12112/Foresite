from django.shortcuts import render

from upload_csv.models import CsvUpload
from .models import ProcessedData


def processed_data(request):
    if not request.user.is_authenticated:
        return render(request, 'processed_data/please_log_in.html')
    else:
        user = request.user
        if CsvUpload.objects.filter(user=user).exists():
            csv_uploads = CsvUpload.objects.filter(user=user).all()
            context_data = {
                'csv_uploads': csv_uploads,
                'user': user,
            }
            return render(request, 'processed_data/list.html', context=context_data)
        else:
            return render(request, 'processed_data/no_data_uploaded.html')


def detail(request, csv_name):
    if not request.user.is_authenticated:
        return render(request, 'processed_data/please_log_in.html')
    else:
        user = request.user
        if CsvUpload.objects.filter(user=user, csv_name=csv_name, data_processed=True).exists():
            csv_processed = CsvUpload.objects.get(user=user, csv_name=csv_name, data_processed=True)
            if ProcessedData.objects.filter(upload_csv_processed=csv_processed).exists():
                processed_data = ProcessedData.objects.get(upload_csv_processed=csv_processed)
                return render(request, 'processed_data/detail.html', {'processed_data': processed_data})
            else:
                return render(request, 'processed_data/no_data_processed.html')
        else:
            return render(request, 'processed_data/no_data_processed.html')
