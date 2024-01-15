import requests
import json


parameters = {"term": "Ann Arbor", "entity": "podcast"}
iTunes_response = requests.get("https://itunes.apple.com/search", params = parameters)

py_data = json.loads(iTunes_response.text)
for r in py_data['results']:
    print(r['trackName'])
