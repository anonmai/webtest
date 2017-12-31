#!/user/bin/python  
# -*- coding: utf8 -*-  
  
import sys  
import re  
import importlib
from splinter.browser import Browser  
  
CLOASE_AFTER_TEST = False  
GBK = "gbk"  
UTF8 = "utf8"  
  

importlib.reload(sys)  
  
encoding = lambda x:x.encode('gbk')  
  
def output(x):  
    """ 
        encode and print 
    """  
    print (encoding(x))
  
def resultMsg(x):  
    """ 
        judge result and print, x : True or False 
    """  
    if x == True:  
        print ('pass')  
    else:  
        print ('[X]not pass') 
    print ('--------------------------')  
  
def checkresult(x):  
    """ 
        check result message, x : the error message u want 
    """  
    resultMsg(browser.is_text_present(x))  
''' 
def testLogin(desc, username, password, result):  
    output(desc)  
    browser.fill('TPL_username',username.decode)  
    browser.fill('TPL_password',password.decode)
    browser.find_by_value('登录').first.click()  
    checkresult(result)  
'''
def testLogin(desc, username, password, result):
    output(desc)
    browser.fill('UserName', username)
    browser.fill('Password', password)
    browser.find_by_name('Submit').first.click()
    checkresult(result)


__testUrl = 'http://www.syhs.org/User/Login.asp'  
  

browser = Browser('chrome')  
browser.visit(__testUrl)  
  
output("测试页面:"+browser.title)  
  
try:  
'''
    testLogin('测试输入数字','1','1','找不到')
    testLogin('测试输入字母','a','b'，'找不到')
    testLogin('测试输入字母','a','b'，'找不到')
    testLogin('测试输入字母','a','b'，'找不到')
'''
    testLogin('测试注册用户','webtest','testweb82'，'尚未通过认证')

except Exception as x:  
    print (x)
  
if CLOASE_AFTER_TEST:  
    browser.quit()  