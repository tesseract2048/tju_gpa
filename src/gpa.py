#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
 @author:   hty0807@gmail.com
"""
from optparse import OptionParser
from importutils import getstragety

# Parse command line options
parser = OptionParser() 
parser.add_option("-s", "--school", action="store", 
                  dest="school", 
                  help="determine which school stragety to use") 
parser.add_option("-c", "--scale", action="store", 
                  dest="scale", 
                  help="determine which scale stragety to use")
parser.add_option("-u", "--username", action="store", 
                  dest="username", 
                  help="username for logging in")
parser.add_option("-p", "--password", action="store", 
                  dest="password", 
                  help="password for logging in")
parser.add_option("-t", "--term", action="store", 
                  dest="term", 
                  help="determine which term to collect GPAs (all if not provided)")

(options, args) = parser.parse_args() 
if not options.school:
    parser.error('School stragety must be specified')
if not options.scale:
    parser.error('Scale stragety must be specified')
if not options.username:
    parser.error('Username must be specified')
if not options.password:
    parser.error('Password must be specified')

school = getstragety("schools.%s" % options.school)
scale = getstragety("scales.%s" % options.scale)

def getgpa(term):
    courses = school.courses(term)
    gpa = scale.calc(courses)
    return {"courses": courses, "gpa": gpa}

school.login({'username': options.username, 'password': options.password})

if not options.term:
    terms = school.terms()
    gpa = {}
    for term in terms:
        gpa[term] = getgpa(term)
else:
    gpa = {options.term: getgpa(options.term)}

allcourses = []

for term in gpa:
    t = gpa[term]
    print '--- TERM %s ---' % term
    print 'GPA: %f' % t['gpa']
    print 'COURSES LIST:'
    for course in t['courses']:
        print '%s (%s): %s' % (course['name'], course['credit'], course['grading'])
        allcourses.append(course)

print '--- SUMMARY ---'
print 'GPA: %f' % scale.calc(allcourses)
