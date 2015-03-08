# -*- coding: utf-8 -*-
"""
Created on Fri Mar 06 21:20:40 2015

@author: zhang
"""

#根据正则表达式分割字符串， 将分割后的所有子字符串放在一个表(list)中返回
import re


import urllib2  


class HTML_Tool:  
    # 用非 贪婪模式 匹配 \t 或者 \n 或者 空格 或者 超链接 或者 图片  
    BgnCharToNoneRex = re.compile("(\t|\n| |<a.*?>|<img.*?>)")  
      
    # 用非 贪婪模式 匹配 任意<>标签  
    EndCharToNoneRex = re.compile("<.*?>")  
  
    # 用非 贪婪模式 匹配 任意<p>标签  
    BgnPartRex = re.compile("<p.*?>")  
    CharToNewLineRex = re.compile("(<br/>|</p>|<tr>|<div>|</div>)")  
    CharToNextTabRex = re.compile("<td>")  
  
    # 将一些html的符号实体转变为原始符号  
    replaceTab = [("<","<"),(">",">"),("&","&"),("&","\""),(" "," ")]  
      
    def Replace_Char(self,x):  
        x = self.BgnCharToNoneRex.sub("",x)  
        x = self.BgnPartRex.sub("\n    ",x)  
        x = self.CharToNewLineRex.sub("\n",x)  
        x = self.CharToNextTabRex.sub("\t",x)  
        x = self.EndCharToNoneRex.sub("",x)  
  
        for t in self.replaceTab:    
            x = x.replace(t[0],t[1])    
        return x    
class hktkdy_Spider:  
    # 申明相关的属性  
    def __init__(self,url):    
        self.myUrl = url 
        self.datas = []  
        self.myTool = HTML_Tool()  
        print u'已经启动爬虫，咔嚓咔嚓' 



content = urllib2.urlopen('http://hktkdy.com/2015/03/03/201503/03/').read()
content = content.decode("UTF-8")
html =re.findall(r".?", content)  

print html
#print content
