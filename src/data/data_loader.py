from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import os
import sys
from configparser import ConfigParser
import ast

class DataLoader():
    
    def connect_to_api(self, config, headers):
        session = Session()
        session.headers.update(headers)
        return session

    def fetch_data(self, session, url, parameters):
        try:
            response = session.get(url, params=parameters)
            data = json.loads(response.text)
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)
            sys.exit(1)
        return data