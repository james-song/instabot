import os
import pickle
from queue import Queue

from .. import config

users_folder_path = config.PROJECT_FOLDER_PATH + config.USERS_FOLDER_NAME


class UserController(object):
    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super(UserController, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.queue = Queue()
        self.main_user = None

        self.load_all_users()

    def load_all_users(self):
        for user_path in os.listdir(users_folder_path):
            if user_path.endswith('.user'):
                username = user_path[:-5]
                user = self.load_user(username)
                if user is not None:
                    self.queue.put(user)

    @property
    def get_user(self):
        if not self.queue.empty():
            temp_user = self.queue.get()
            self.queue.put(temp_user)
            return temp_user

    @property
    def main(self):
        # TODO: check if main_user is set
        return self.main_user

    @main.setter
    def main(self, user):
        self.main_user = user

    @main.deleter
    def main(self):
        del self.main_user

    def load_user(self, name):
        input_path = users_folder_path + "%s.user" % name
        if not os.path.exists(input_path):
            # warn
            return None

        with open(input_path, 'rb') as finput:
            try:
                user = pickle.load(finput)
                if not user.logged_in:
                    return None
                return user
            except:
                # warnings.warn("%s is corrupted." % username)
                # warn
                os.remove(input_path)
                return None