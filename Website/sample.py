import requests
import json

url = "https://api.themoviedb.org/3/movie/19995?api_key=23804a8fe2dd745c8b0709c0ee6e7bc7&language=en-US"
response = requests.get(url) 

print(json.dumps(response.json(), indent = 4))