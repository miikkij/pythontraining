import time
import json
from locust import events

class ClientWrapper():
    client = None
    def __init__(self, client):
      self.client = client

    def __getattr__(self, name):
      attr = self.client.__getattribute__(name)
      if hasattr(attr, '__call__'):
        def newfunc(*args, **kwargs):
          start_time = time.time()
          try:
            result = attr(*args, **kwargs)
            total_time = int((time.time() - start_time) * 1000)
            events.request_success.fire(request_type="http", name=name, response_time=total_time, response_length=0)
            return result
          except Exception as e:
            total_time = int((time.time() - start_time) * 1000)
            events.request_failure.fire(request_type="http", name=name, response_time=total_time, exception=e)
        return newfunc
      else:
        return attr
