#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
 @author:   hty0807@gmail.com
"""

def getstragety(module):
    mod = __import__(module, globals(), locals(), [module], -1)
    clazz = getattr(mod, 'Stragety')
    return clazz()
