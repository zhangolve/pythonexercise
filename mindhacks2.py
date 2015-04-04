
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 07 16:36:13 2015

@author: zhang
"""
#以我的博客中某一篇为样子来写的一个下载的程序，接下来应当做到的是对于程序本身内容的
#丰富，要学习正则表达式，现在的程序还只能爬去一个段落。然后是让他能够爬去所有的文章
#这里自然就要用到了循环。
#现在一篇文章能够爬去了，但是还要考虑去标签。
import  urllib2  
import re
   


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


    f=open('new3.html','a')
    f.writelines(title)
    f.write('\n')
    f.writelines(content)
    f.write('\n')
    f.close()
"""    
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


        f=open('new3.html','a')
        f.writelines(title)
        f.write('\n')
        f.writelines(content)
        f.write('\n')
        f.close()  


print 'succeed'
   
   
   
   
# -*- coding: utf-8 -*-
"""
"""
#以我的博客中某一篇为样子来写的一个下载的程序，接下来应当做到的是对于程序本身内容的
#丰富，要学习正则表达式，现在的程序还只能爬去一个段落。然后是让他能够爬去所有的文章
#这里自然就要用到了循环。
#现在一篇文章能够爬去了，但是还要考虑去标签。


import  urllib2  
import re


url='http://hktkdy.com'


m = urllib2.urlopen(url).read().decode("UTF-8")  


p =re.compile(r' <h1 class="post-title"><a data-pjax href="(.*?)">.*?</a>')
t=p.findall(m)

for i in range(0,len(t)):
    
    
    
   
    t[i]='http://hktkdy.com'+t[i]

page=urllib2.urlopen(t[1]).read().decode("UTF-8")  

p =re.compile(r'<li id="navbar-title">.*?>(.*?)</a></li>') #注意r后面的‘要紧挨着，不要有空格。       <li id="navbar-title"><a href="#">what you are</a></li>
q=re.compile(r'<p>(.*)</p>')
title=p.findall(page)
content=q.findall(page)
print title
print content

f=open('5.txt','a')
f.writelines(title)
f.write('\n')
f.writelines(content)
f.write('\n')
f.close()  
print 'succeed'
   
  """ 



