#!/usr/bin/env python

from lib.user import User

class Student(User):

    def learn(self, new_info):
        self.knowledge.append(new_info)
