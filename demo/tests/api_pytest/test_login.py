import os
import sys
import uuid

# Import the shared client from local path.
# The client could later be a library that can be loaded from Artifactory
sys.path.append(os.path.abspath('../user_client'))
from user_client import UserClient

baseurl = 'http://192.168.99.100:8000'

client = UserClient(baseurl)

# We can build complex use cases as single functions used in the actual tests
# similar to PageObject pattern used in UI testing:

def login(user, pwd):
  return client.login(user, pwd)

def self(sessionid):
  return client.self(sessionid)

# Test methods

def test_login_withcorrectpassword_returns200():
  res = login('user', 'pass')
  assert res.status_code == 200

def test_login_withincorrectpassword_returns401():
  res = login('user', 'bork')
  assert res.status_code == 401

def test_self_withvalidsession_returns200():
  res = login('user', 'pass')

  session = res.headers['session']
  res = self(session)
  assert res.status_code == 200

def test_self_withinvalidsession_returns401():
  res = self('ubc')
  assert res.status_code == 401
