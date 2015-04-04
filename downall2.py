
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
   


#for j in range(4,10):
                       
url='http://hktkdy.com/page/4' #+str(j)
                    
                    
m = urllib2.urlopen(url).read() 
                    
                    
p =re.compile(r' <h1 class="post-title"><a data-pjax href="(.*?)">.*?</a>')
t=p.findall(m)
                    
for i in range(0,len(t)):
    
                        
                        
                        
                       
        t[i]='http://hktkdy.com'+t[i]
                    
        page=urllib2.urlopen(t[i]).read()  
                    
        p =re.compile(r'<p>(.*)</p>') #注意r后面的‘要紧挨着，不要有空格。
        txtpage=p.findall(page)
        print txtpage
                    
                    
        f=open('8.html','a')
        f.writelines(txtpage)  
        f.close()  
                    
print 'succeed'                     
                       
