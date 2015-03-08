# -*- coding: utf-8 -*-
"""
Created on Sat Mar 07 19:18:43 2015

@author: zhang
"""

import urllib2
import re
url='http://hktkdy.com'
htmltext=urllib2.urlopen(url).read().decode('utf-8')
for tag in re.findall(r'<p>.?</p>',htmltext):
    print tag
    