from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import os
import sys
from configparser import ConfigParser
import ast


def main():
  config = ConfigParser()
  
  config.read('/Users/marshallfelder/Documents/Pet Projects/config/config.ini')
  
  headers = ast.literal_eval(config.get('coin', 'headers'))
  url = ast.literal_eval(config.get('coin', 'url'))
  parameters = ast.literal_eval(config.get('coin', 'parameters'))
  session = Session()
  
  def fetch_data(session, url, parameters, headers):
    session.headers.update(headers)
    try:
      response = session.get(url, params=parameters)
      data = json.loads(response.text)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
      print(e)
      sys.exit(1)
    return data

  data = fetch_data(session, url, parameters, headers)
  
  print(data['data'])

if __name__ == "__main__":
  main()