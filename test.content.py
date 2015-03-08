# -*- coding: utf-8 -*-
"""
Created on Sat Mar 07 16:58:58 2015

@author: zhang
"""

import re
import urllib2

url='http://hktkdy.com/2015/03/03/201503/03/'

html=urllib2.urlopen(url).read()
str = "<img /><a>srcd</a>hello</br><br/>"
str = re.sub(r'</?\w+[^>]*>','',str)
html=re.findall(r'开学.?补办',html)
print html
