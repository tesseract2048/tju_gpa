#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
 @author:   hty0807@gmail.com
"""
from school import School
from httputils import request
import re

class Stragety(School):

    ''' attempt to log in with specified authentication '''
    ''' authentication may contains username and password '''
    def login(self, authentication):
        u = authentication['username']
        p = authentication['password']
        # logging in
        resp = request("http://e.tju.edu.cn/Main/logon.do", data={'uid':u, 'password':p}).decode('gbk')
        if resp.find(u) < 0:
            raise Exception("Incorrect authentication")

    ''' get a list of available terms '''
    def terms(self):
        resp = request("http://e.tju.edu.cn/Education/stuachv.do").decode('gbk')
        p = re.compile("""<a class="titlelink" href="/Education/stuachv\\.do\\?todo=display&term=(\\d+)" >""")
        return p.findall(resp)

    ''' get course info of specified term '''
    def courses(self, term):
        resp = request("http://e.tju.edu.cn/Education/stuachv.do?todo=display&term=%s" % term).decode('gbk')
        p = re.compile("""<tr align="center" bgcolor="#FFFFFF" height="25" valign="bottom">([^<]*)<td class="(TableRowColor|TableAltRowColor2)"  align="center"><font class=ContextText2>(\\d+)</font></td>([^<]*)<td class="(TableRowColor|TableAltRowColor2)"  align="center"><font class=ContextText2>(\\d+)</font></td>([^<]*)<td class="(TableRowColor|TableAltRowColor2)"  align="left"><font class=ContextText2>([^<]*)</font></td>([^<]*)<td class="(TableRowColor|TableAltRowColor2)"  align="left"><font class=ContextText2>([^<]*)</font></td>([^<]*)<td class="(TableRowColor|TableAltRowColor2)"  align="center"><font class=ContextText2>([^<]*)</font></td>([^<]*)<td class="(TableRowColor|TableAltRowColor2)"  align="center"><font class=ContextText2>([^<]*)</font></td>([^<]*)<td class="(TableRowColor|TableAltRowColor2)"  align="center"><font class=ContextText2>([^\\d]*)(\\d+)([^<]*)</font></td>([^<]*)<td class="(TableRowColor|TableAltRowColor2)"  align="center"><font class=ContextText2>([^<]*)</font></td>([^<]*)<td class="(TableRowColor|TableAltRowColor2)"  align="center"><font class=ContextText2>([^<]*)</font></td>([^<]*)</tr>""", re.MULTILINE | re.DOTALL)
        courses = []
        for mch in p.findall(resp):
            course = {"id": mch[5].strip(), 
                "name": mch[8].replace("&nbsp;", " ").strip(), 
                "coursetype": mch[11].strip(),
                "courseclass": mch[14].strip(),
                "credit": float(mch[17].strip()),
                "grading": float(mch[21].strip()),
                "grading_type": mch[26].strip(),
                "comment": mch[28].strip(),
                }
            if course['grading'] < 60:
                continue
            courses.append(course)
        return courses
