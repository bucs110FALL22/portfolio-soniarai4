import requests

class TriviaAPI:
  def __init__(self):
    self.url = 'https://opentdb.com/api.php?amount=1&category=9&difficulty=medium&type=boolean'
  
  def get(self):
    data = requests.get(self.url)
    response = data.json()
    
    if response.get('results'):
      return response['results']
    else:
      return None

'''
This API randomly gives the user a true/false trivia question. 
'''