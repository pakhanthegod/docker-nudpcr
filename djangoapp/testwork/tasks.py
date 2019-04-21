import json
import urllib.request
import time
from unittest import mock

from celery import shared_task

data = [{"year": 1805, "month": 7}, {"first": "анна", "middle": "павловна", "last": "шерер"}, {"first": "мария", "middle": "феодоровна"}, {"first": "василий"}, {"first": "анна", "middle": "павловна"}, {"parts": [{"name": "Инженерной", "type": "улица"}, {"number": "2"}]}, {"parts": [{"name": "Алтуфьевское", "type": "шоссе"}, {"number": "51", "type": "дом"}]}, {
        "parts": [{"name": "Карелия", "type": "республика"}, {"name": "Петрозаводск", "type": "город"}, {"name": "Маршала Мерецкова", "type": "улица"}, {"number": "8 Б", "type": "дом"}, {"number": "4", "type": "офис"}]}, {"first": "вячеслав", "middle": "владимирович", "last": "бушуев"}, {"first": "вера", "middle": "константиновна", "last": "бушуева"}]

mocked_data = json.dumps(data).encode('utf-8')

@shared_task
# Mocked request because a local test
@mock.patch('urllib.request.Request', mock.MagicMock(return_value=mocked_data))
def fetch_data():
    url = 'http://some-url.com'  # This should probably be in django.conf.settings
    request = urllib.request.Request(url)

    # with urllib.request.urlopen(request) as response:
    #     response_body = response.read()
        # data = json.loads(response_body)
    data = json.loads(request)

    

    time.sleep(1)  # Simulate delay

    return data
