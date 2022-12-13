import requests

class AdviceAPI:
  def __init__(self):
    self.url = "https://api.adviceslip.com/advice"
  
  def get(self):
    data = requests.get(self.url) 
    json = data.json()
    return json["slip"]["advice"]

'''
Fetches a random piece of advice from the Advice Slip API and returns it as a string. 
'''
