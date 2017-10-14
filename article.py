#!/usr/bin/env python2.7

from datetime import datetime 

class article(object):
    def __init__(self, title, description, date, body="", link):
        self.title = title
        self.description = description
        self.date = date 
        self.body = body 
        self.link = link 
    def get_title(self):
        return self.title
    def get_description(self):
        return self.description
    def get_date(self):
        return self.date 
    def get_body(self):
        return self.body
    def get_link(self):
        return self.link 
    def __str__(self): # Please don't use this lol, just use the get functions and then print those 
        return self.get_title()+ " " + self.get_description()+ " " + self.get_body() + " " + self.get_date()
        