import json
import requests

def get_results():
  response = requests.get('https://meowfacts.herokuapp.com/').json()
  print(response)
get_results()