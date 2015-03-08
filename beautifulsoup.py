# -*- coding: utf-8 -*-
"""
Created on Sat Mar 07 17:45:41 2015

@author: zhang
"""
#用beautiful soup来查找网页中标题的程序。

import urlparse
import urllib
from BeautifulSoup import BeautifulSoup

url='http://hktkdy.com/2015/03/03/201503/03/'
urls=[url]
while len(urls)>0:
    try:
        htmltext=urllib.urlopen(urls[0]).read().decode('utf-8')
        
    except:
        print urls[0]
    soup=BeautifulSoup(htmltext)
    #title=soup
    urls.pop(0)
    tag=soup.html.head.title.string  #这里必须是A而不能是a。省去了正则
                                                  #表达式re
    print tag
        