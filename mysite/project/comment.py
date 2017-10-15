#!/usr/bin/env python2.7

class comment(object):
    def __init__(self,author="Deleted",body="",children=[]):
        self.author = author
        self.body = body
        self.children = children # Array of child children 
    def add_child(self, child):
        self.children += child 
    def get_author(self):
        return self.author
    def get_body(self):
        return self.body
    def get_children(self):
        return self.children
    def has_children(self):
        if len(self.children) > 0:
            return True
        else:
            return False 