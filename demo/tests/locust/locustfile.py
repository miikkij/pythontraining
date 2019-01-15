import os
import sys
sys.path.append(os.path.abspath('../user_client'))

from locust import Locust, TaskSet, task
from user_client import UserClient
from utils import ClientWrapper

class CustomLocust(Locust):
    def __init__(self, *args, **kwargs):
        super(CustomLocust, self).__init__(*args, **kwargs)
        self.client = ClientWrapper(UserClient(self.host))

class UserBehavior(TaskSet):
    def on_start(self):
        pass

    @task()
    def login(self):
        self.client.login('user', 'pass')

    @task()
    def user(self):
        self.client.self('abc')

class WebsiteUser(CustomLocust):
    task_set = UserBehavior
    min_wait = 0
    max_wait = 0
