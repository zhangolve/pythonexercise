# -*- coding: utf-8 -*-
"""
Created on Wed Apr 01 17:05:52 2015

@author: zhang
"""
import re
url='aa<div>test1</div>bb<div>test2</div>cc'
p = re.compile(r'<div>.*</div>.*</div>')
q=re.compile(r'<div>.*?</div>')

output=p.findall(url)
output2=q.findall(url)
print output,output2


#url='aa<div>test1</div>bb<div>test2</div>cc'
#p=re.compile=(r'<div>.*</div>')

#output=p.findall('aa<div>test1</div>bb<div>test2</div>cc')

#print output



#import re
 
