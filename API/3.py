import requests

# POST

to_do_item = {
    "userId": 2,
    "title": "my to do",
    "completed": False
    }
post_url = "https://jsonplaceholder.typicode.com/todos"
post_response = requests.post(post_url, to_do_item)
print(post_response.json())