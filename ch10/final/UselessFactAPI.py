import requests

class UselessFactAPI:
  def __init__(self):
    self.url = "https://uselessfacts.jsph.pl/random.json"
  
  def get(self):
    data = requests.get(self.url) 
    json = data.json()
    return json["text"]

'''
Fetches a random useless fact from the Useless Fact API and returns it.
'''
UselessFactAPI()