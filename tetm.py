import sys  
import re  
import time
from splinter.browser import Browser  
  
CLOASE_AFTER_TEST = False  

def testLogin(desc, username, password):
    browser = Browser('chrome')  
    browser.visit(__testUrl)  
    print('------------------------')
    print(desc + ': ' + username + ' ' + password)
    browser.fill('txt_user', username)
    browser.fill('txt_password', password)
    browser.find_by_name('btnLoin').first.click()
    time.sleep(1)
    alert = browser.get_alert()
    print (alert.text)
    print('------------------------')
    time.sleep(2)
    browser.quit()
    #browser.find_by_name('确定').first.click()
    #browser.back()

__testUrl = 'http://219.219.114.101/gts2018/tmsgl/login.aspx'  
  
print('--------------------------------')
print("测试网址:" + __testUrl)  
print('--------------------------------')
  
try:  
    testLogin('测试输入数字','123456','123456')
    testLogin('测试输入字母','abcdefg','abcdefg')
    testLogin('测试输入空用户名和密码','','')
    testLogin('测试输入空用户名','','abc123')
    testLogin('测试输入空密码','abc123','')
    testLogin('测试输入长字符','aaaaaaaaaaaaaaaaaaaaaaaa123456','aaaaaaaaaaaaaaaaaaaaaaaa123456')
    testLogin('测试输入短字符','a','1')   
    testLogin('测试输入特殊字符','?ab12!','/ab12.') 
    testLogin('测试输入纯特殊字符','?/-=~`','*(&^%$:')
    testLogin('测试输入中文用户名','用户名','a1')
    testLogin('测试输入SQL敏感字符',"'abc123--","abc'123--'")  
    testLogin('测试输入SQL注入',"' OR '1=1'--","' OR '1=1'--")  
    testLogin('测试输入XSS注入','<script>alert(document.cookie)</script>','<script>alert(document.cookie)</script>')
    '''
    testLogin('测试输入数字','1','1','用户名不存在!')
    testLogin('测试输入空用户名和密码','','','- 请输入用户名\n- 请输入密码')
    '''

except Exception as x:  
    print (x)
  
if CLOASE_AFTER_TEST:  
    browser.quit()  