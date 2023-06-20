import requests
import threading
import time

def get_data(urls):
    start_time = time.time()
    json_array = []
    for url in urls:
        json_array.append(requests.get(url).json)
    end_time = time.time
    past_time = float(end_time) - float(start_time)
    print(f"execution time is {past_time}")
    return json_array

urls = ["https://postman-echo.com/delay/3"] * 10
get_data(urls)