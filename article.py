#!/usr/bin/env python2.7

from datetime import datetime 

class article(object):
    def __init__(self, title, description, date, body=""):
        self.title = title
        self.description = description
        self.date = date 
        self.body = body 
    def get_title(self):
        return self.title
    def get_description(self):
        return self.description
    def get_date(self):
        return self.date 
    def get_body(self):
        return self.body