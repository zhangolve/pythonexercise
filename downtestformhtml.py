
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
url='http://mindhacks.cn/2015/01/27/escape-from-your-shawshank-part5-2-platos-cave/'


m = urllib2.urlopen(url).read().decode("UTF-8")  


#p =re.compile(r'<p>.*</p>')  #删除评论信息，考虑用到列表项的删除。
#t=p.findall(m)

q=re.compile(r'<div class="comment-content"><p>.*</p>')
comment=q.findall(m)
print comment
p =re.compile(r'<p>.*</p>')
content=p.findall(m)
print content
for i in range(len(content)):
    for j in range(len(comment)):
        
    
        if content[i]==comment[j]:
            content[i]=[]
     #   t[i]=[]
#
#t=filter(lamda e:e!=q.findall(t), t)

f=open('5.html','w')
f.writelines(content)  
f.close()  
print 'succeed'
   
   
#-------- 在这里输入参数 ------------------  
  
# 这个是山东大学的百度贴吧中某一个帖子的地址  
#bdurl = 'http://tieba.baidu.com/p/2296017831?pn='  
#iPostBegin = 1  
#iPostEnd = 10  
  


#-------- 在这里输入参数 ------------------  
   
