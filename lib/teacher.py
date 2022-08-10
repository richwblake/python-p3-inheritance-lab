#!/usr/bin/env python

from lib.user import User

import random

class Teacher(User):

    def __init__(self, f, l):
        super().__init__(f, l)
        self.knowledge = ["str is a data type in Python",
                "programming is hard, but it's worth it",
                "JavaScript async web request",
                "Python function call definition",
                "object-oriented teacher instance",
                "programming computers hacking learning terminal",
                "pipenv install pipenv shell",
                "pytest -x flag to fail fast"]


    def teach(self):
        return self.knowledge[random.randint(0, 8)] 
