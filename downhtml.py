# -*- coding: utf-8 -*-
"""
Created on Sat Mar 07 16:36:13 2015

@author: zhang
"""

import  urllib2  
   
#定义百度函数  
url='http://hktkdy.com'


m = urllib2.urlopen(url).read()  

f=open('333.html','w')
f.write(m)  
f.close()  
   
   
#-------- 在这里输入参数 ------------------  
  
# 这个是山东大学的百度贴吧中某一个帖子的地址  
#bdurl = 'http://tieba.baidu.com/p/2296017831?pn='  
#iPostBegin = 1  
#iPostEnd = 10  
  


#-------- 在这里输入参数 ------------------  
   
