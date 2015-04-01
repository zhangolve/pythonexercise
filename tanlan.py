# -*- coding: utf-8 -*-
"""
Created on Wed Apr 01 17:21:58 2015

@author: zhang
"""
import re

url='aa<div>test1</div>bb<div>test2</div>cc'
p=re.compile=(r'<div>.*</div>')

output=p.findall(url)

print output







