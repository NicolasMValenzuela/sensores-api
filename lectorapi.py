import json
import requests

req = requests.get('http://35.223.175.249:8000/')

print(req.json())