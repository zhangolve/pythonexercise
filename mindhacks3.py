# -*- coding: utf-8 -*-
"""
Created on Sat Apr 04 07:58:48 2015

@author: zhang
"""

import  urllib2  
import re


import httplib

def patch_http_response_read(func):
    def inner(*args):
        try:
            return func(*args)
        except httplib.IncompleteRead, e:
            return e.partial

    return inner
httplib.HTTPResponse.read = patch_http_response_read(httplib.HTTPResponse.read)
   


url='http://mindhacks.cn'


    
m = urllib2.urlopen(url).read()


    
pattern=re.compile(r'<div class="entry-thumbnails"><a class="entry-thumbnails-link" href="(.*?)">')
t=pattern.findall(m)

for i in range(0,len(t)):
    
        
    
    
    
    
   
   # t[i]='http://hktkdy.com'+t[i]
           
    page=urllib2.urlopen(t[i]).read()  

    p =re.compile(r'<title>(.*?)</title>') #注意r后面的‘要紧挨着，不要有空格。       <li id="navbar-title"><a href="#">what you are</a></li>
    q=re.compile(r'<p>(.*)</p>')    #经常会有异常，网络部稳定，考虑要加上except，例外。
    title=p.findall(page)
    content=q.findall(page)
    print title
    print content


    f=open('new344.html','a')
    f.writelines(title)
    f.write('\n')
    f.writelines(content)
    f.write('\n')
    f.close()
for j in range(2,11):
    url='http://mindhacks.cn/page/'+str(j)


    m = urllib2.urlopen(url).read() 


    p =re.compile(r'<div class="entry-thumbnails"><a class="entry-thumbnails-link" href="(.*?)">')
    t=p.findall(m)

    for i in range(0,len(t)):
    
    
    
   
        #t[i]='http://hktkdy.com'+t[i]

        page=urllib2.urlopen(t[i]).read()

        p =re.compile(r'<title>(.*?)</title>') #注意r后面的‘要紧挨着，不要有空格。       <li id="navbar-title"><a href="#">what you are</a></li>
        q=re.compile(r'<p>(.*)</p>')
        title=p.findall(page)
        content=q.findall(page)
        print title
        print content


        f=open('new344.html','a')
        f.writelines(title)
        f.write('\n')
        f.writelines(content)
        f.write('\n')
        f.close()  


print 'succeed'
   