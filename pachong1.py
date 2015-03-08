# -*- coding: utf-8 -*-
"""
Created on Sat Mar 07 16:17:37 2015

@author: zhang
"""

import urllib,urllib2  
url = "http://blog.ithomer.net"  
req = urllib2.Request(url)  
content = urllib2.urlopen(req).read() 
fact=content.
print fact