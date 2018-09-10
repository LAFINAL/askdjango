from django.shortcuts import render
from django.http import HttpResponse
import os
from askdjango import settings

# Create your views here.
def intro(request):
    return render(request, 'dojo/dojo.html')

def dojo_sum(request, numbers):
    result = sum(list(map(int, numbers.split("/"))))
    return HttpResponse(result)

def excel_download(request):
    filepath = os.path.join(settings.BASE_DIR, 'exnumbers.xlsx')
    filename = os.path.basename(filepath)
    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type = 'application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
        return response

    