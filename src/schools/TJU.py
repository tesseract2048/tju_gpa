#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
 @author:   hty0807@gmail.com
"""
from school import School
from tjueweb.client import EWebClient

class Stragety(School):

    def __init__(self):
        self.client = EWebClient()

    ''' attempt to log in with specified authentication '''
    ''' authentication may contains username and password '''
    def login(self, authentication):
        u = authentication['username']
        p = authentication['password']
        return self.client.login(u, p)

    ''' get a list of available terms '''
    def terms(self):
        return self.client.achvterms()

    ''' get course info of specified term '''
    def courses(self, term):
        return self.client.achv(term)
