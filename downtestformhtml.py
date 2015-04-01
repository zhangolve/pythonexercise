
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
   
#定义百度函数  
url='http://hktkdy.com/2015/03/31/201503/033105/'


m = urllib2.urlopen(url).read().decode("UTF-8")  
print m

p =re.compile(r'<p>.*</p>')
t=p.findall(m)
print t


f=open('3.txt','w')
f.writelines(t)  
f.close()  
print 'succeed'
   
   
#-------- 在这里输入参数 ------------------  
  
# 这个是山东大学的百度贴吧中某一个帖子的地址  
#bdurl = 'http://tieba.baidu.com/p/2296017831?pn='  
#iPostBegin = 1  
#iPostEnd = 10  
  


#-------- 在这里输入参数 ------------------  
   
