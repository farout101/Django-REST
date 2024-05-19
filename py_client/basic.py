import requests

# endpoint ="https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api"

get_response = requests.get(endpoint, params={"name":"Gway To"},json={"test":"Gway To"})

print(get_response.json()['message'])