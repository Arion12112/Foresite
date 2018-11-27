from django.shortcuts import render


def processed_data(request):
    if not request.user.is_authenticated:
        return render(request, 'upload_csv/please_log_in.html')
    else:
