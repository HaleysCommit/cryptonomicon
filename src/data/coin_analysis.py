from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import os
import sys
from configparser import ConfigParser
import ast
from data_loader import DataLoader


def main():
  config = ConfigParser()
  data_loader = DataLoader()
  
  config.read('/Users/marshallfelder/Documents/Pet Projects/config/config.ini')
  headers = ast.literal_eval(config.get('coin', 'headers'))
  url = ast.literal_eval(config.get('coin', 'url'))
  parameters = ast.literal_eval(config.get('coin', 'parameters'))

  session = data_loader.connect_to_api(config, headers)
  data = data_loader.fetch_data(session, url, parameters)
  
  print(data['data'])

if __name__ == "__main__":
  main()