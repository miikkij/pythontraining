import requests

class UserClient(object):
  host = None

  def __init__(self, host):
    self.host = host
    pass

  def login(self, username, password):
    payload = {'username': username, 'password': password}
    url = self.host + '/api/user/login'
    return requests.post(url, json=payload)

  def self(self, sessionid):
    headers = {'session': sessionid}
    url = self.host + '/api/user'
    return requests.get(url, headers=headers)
