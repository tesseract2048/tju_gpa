#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
 @author:   hty0807@gmail.com
"""

class Scale:

    ''' calculate GPA taking specified courses '''
    ''' courses is a list of dict contains credit and grading '''
    ''' where grading is either letter (i.e. A, A-) or number (0-100) '''
    def calc(self, courses):
        raise NotImplementedError()
