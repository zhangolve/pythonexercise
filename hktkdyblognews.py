# -*- coding: utf-8 -*-
"""
Created on Wed Apr 01 17:51:08 2015

@author: zhang
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 18:31:08 2015

@author: zhang
"""

# -*- coding: utf-8 -*-

#import string
import urllib2
import re
import time
import smtplib
from email.mime.text import MIMEText

mailto_list = ['1262010981@qq.com']	# 收件人，多个收件人用逗号隔开
mail_host = 'smtp.gmail.com'
mail_user = 'zhangolve'				# 发件人
mail_pass = '13930613823zxw'				# 发件人密码

def send_mail(to_list, sub, content):
    msg = MIMEText(content, _subtype = 'html', _charset = 'utf-8')
    msg['Subject'] = sub
    msg['From'] = mail_user
    msg['To'] = ';'.join(to_list)
    try:
        s = smtplib.SMTP()
        s.connect(mail_host)
        s.ehlo()
        s.starttls()
        s.login(mail_user, mail_pass)
        s.sendmail(mail_user, to_list, msg.as_string())
        s.close()
        return True
    except Exception, e:
        print str(e)
        return False

def GetNews():
    url = 'http://hktkdy.com/2015/03/31/201503/033105/'
    req = urllib2.Request(url)
    page = urllib2.urlopen(req).read()
    p =re.compile(r'<p>.*</p>')
        # <a class="pad_left" href="http://i.whut.edu.cn/xxtg/znbm/jwc/201503/t20150331_163220.shtml" title="【教务处】关于举办慕课课程开发及混合式教学模式研讨会的通知">【教务处】关于举办慕课课程开发及混合式教学模式研讨...</a><span class="pad_right" >2015-03-31</span></li>
        #<a href="http://202.196.192.25:8980/jwc/20151373.html" title="2015年专升本网上报名相关事项通知" rel="bookmark">
    #<i class="icon-eject icon-large"></i>2015年专升本网上报名相关事项通知</a>
    
    items = p.findall(page)
    news=items
    #print items
    #news = []   #news原来是一个空的列表
    #for item in items:
       # if(item[2] == time.strftime('%Y-%m-%d',time.localtime(time.time()))):
            #news.append([item[0], item[1], item[2]])
            #print item[1]
           # news.append([item[0], item[1]])
    
    print news    
    return news
    

news = GetNews()
if news:
    
        
    sub = 'WHUT教务处最新通知推送（Anotherhome提供）' + time.strftime('%Y-%m-%d',time.localtime(time.time()))
    content = 'WHUT最新通知:'
    content=content+news[0]+news[1]+news[2]+news[-1]
    #for item in news:
       # content += item[2]
       # content += '  '
        #content += item[1]
        #content += '  '
       # content += item[0]
       # content += ''
    print content    
    #content += ' （校内资源，请用校园网或VPN访问）  <br><br> 推送服务由<a href="http://www.anotherhome.net/" target="_blank">Anotherhome</a>提供. 代码托管在<a href="https://github.com/DIYgod/WHUTNews" target="_blank">Github</a>上.'
    if send_mail(mailto_list, sub, content):
        print 'Succeed'
    else:
        print 'Fail'
else:
    print 'abc'
