#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
 @author:   hty0807@gmail.com
"""
from scale import Scale

class Stragety(Scale):

    ''' calculate GPA taking specified courses '''
    ''' courses is a list of dict contains credit and grading '''
    ''' where grading is either letter (i.e. A, A-) or number (0-100) '''
    def calc(self, courses):
        sum_weighted = float(0)
        sum_credit = float(0)
        for course in courses:
            grading = self.getgrading(course['grading'])
            sum_weighted += grading * course['credit']
            sum_credit += course['credit']
        if sum_credit == float(0):
            return float(0), float(0)
        return (sum_weighted / sum_credit, sum_credit)

    def getgrading(self, grading):
        if grading >= 90:
            return 4.0
        if grading >= 85:
            return 3.7
        if grading >= 82:
            return 3.3
        if grading >= 78:
            return 3.0
        if grading >= 75:
            return 2.7
        if grading >= 72:
            return 2.3
        if grading >= 68:
            return 2.0
        if grading >= 64:
            return 1.5
        if grading >= 60:
            return 1.0
        return 0.0