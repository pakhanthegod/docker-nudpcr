import json
import time

from django.shortcuts import render
from django.template.response import TemplateResponse
from django.views.decorators.csrf import csrf_protect

from .forms import FetchDataForm
from .tasks import fetch_data


# @csrf_protect
# def fetch_data_view(request):
#     """
#     A view for fetching data from an extern API
#     """
#     if request.method == 'POST':
#         form = FetchDataForm(request.POST)
#         if form.is_valid():
#             task = fetch_data.delay()  # Sending the task to workers
#             data = task.get()  # Wait until the task get completed and get data from it

#             ctx = {
#                 'data': data
#             }

#             return TemplateResponse(request, 'testwork/complete.html', ctx)
#     else:
#         form = FetchDataForm()
    
#     ctx = {
#         'form': form
#     }

#     return TemplateResponse(request, 'testwork/form.html', ctx)


# @csrf_protect
# def fetch_data_no_celery_view(request):
#     """
#     A view for fetching data from an extern API
#     """
#     if request.method == 'POST':
#         form = FetchDataForm(request.POST)
#         if form.is_valid():
#             data = [{"year": 1805, "month": 7}, {"first": "анна", "middle": "павловна", "last": "шерер"}, {"first": "мария", "middle": "феодоровна"}, {"first": "василий"}, {"first": "анна", "middle": "павловна"}, {"parts": [{"name": "Инженерной", "type": "улица"}, {"number": "2"}]}, {"parts": [{"name": "Алтуфьевское", "type": "шоссе"}, {"number": "51", "type": "дом"}]}, {
#                 "parts": [{"name": "Карелия", "type": "республика"}, {"name": "Петрозаводск", "type": "город"}, {"name": "Маршала Мерецкова", "type": "улица"}, {"number": "8 Б", "type": "дом"}, {"number": "4", "type": "офис"}]}, {"first": "вячеслав", "middle": "владимирович", "last": "бушуев"}, {"first": "вера", "middle": "константиновна", "last": "бушуева"}]

#             mocked_data = json.dumps(data).encode('utf-8')
#             data = json.loads(mocked_data)

    

#             time.sleep(1)  # Simulate delay
#             ctx = {
#                 'data': data
#             }

#             return TemplateResponse(request, 'testwork/complete.html', ctx)
#     else:
#         form = FetchDataForm()
    
#     ctx = {
#         'form': form
#     }

#     return TemplateResponse(request, 'testwork/form.html', ctx)


@csrf_protect
def fetch_data_view(request):
    """
    A view for fetching data from an extern API
    """
    task = fetch_data.delay()  # Sending the task to workers
    data = task.get()  # Wait until the task get completed and get data from it

    ctx = {
        'data': data
    }

    return TemplateResponse(request, 'testwork/complete.html', ctx)


@csrf_protect
def fetch_data_no_celery_view(request):
    """
    A view for fetching data from an extern API
    """
    
    data = [{"year": 1805, "month": 7}, {"first": "анна", "middle": "павловна", "last": "шерер"}, {"first": "мария", "middle": "феодоровна"}, {"first": "василий"}, {"first": "анна", "middle": "павловна"}, {"parts": [{"name": "Инженерной", "type": "улица"}, {"number": "2"}]}, {"parts": [{"name": "Алтуфьевское", "type": "шоссе"}, {"number": "51", "type": "дом"}]}, {
        "parts": [{"name": "Карелия", "type": "республика"}, {"name": "Петрозаводск", "type": "город"}, {"name": "Маршала Мерецкова", "type": "улица"}, {"number": "8 Б", "type": "дом"}, {"number": "4", "type": "офис"}]}, {"first": "вячеслав", "middle": "владимирович", "last": "бушуев"}, {"first": "вера", "middle": "константиновна", "last": "бушуева"}]

    mocked_data = json.dumps(data).encode('utf-8')
    data = json.loads(mocked_data)



    time.sleep(1)  # Simulate delay
    ctx = {
        'data': data
    }

    return TemplateResponse(request, 'testwork/complete.html', ctx)