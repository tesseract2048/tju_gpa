#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
 @author:   hty0807@gmail.com
"""
import requests
import urllib
import urllib2
import cookielib

cookiejar = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiejar))
headers = [
    ('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36'), 
    ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'), 
    ('Accept-Encoding', 'gzip,deflate,sdch'), 
    ('Accept-Langauge', 'en-US,en;q=0.8')
]
opener.addheaders = headers

def ungzip(s):
    from StringIO import StringIO
    import gzip
    buffer = StringIO(s)
    f = gzip.GzipFile(fileobj=buffer)
    return f.read()

def undeflate(s):
    import zlib
    return zlib.decompress(s, -zlib.MAX_WBITS)

def request(url, **args):
    if 'data' in args:
        args['data'] = urllib.urlencode(args['data'])
    r = opener.open(urllib2.Request(url, **args), timeout=60)
    data = r.read()
    if r.info().get('Content-Encoding') == 'gzip':
        data = ungzip(data)
    elif r.info().get('Content-Encoding') == 'deflate':
        data = undeflate(data)
    return data


