#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
 @author:   hty0807@gmail.com
"""

class School:

    ''' attempt to log in with specified authentication '''
    ''' authentication may contains username and password '''
    def login(self, authentication):
        raise NotImplementedError()

    ''' get a list of available terms '''
    def terms(self):
        raise NotImplementedError()

    ''' get course info of specified term '''
    def courses(self, term):
        raise NotImplementedError()
