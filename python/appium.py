from appium import webdriver
import time
from selenium.webdriver.common.keys import Keys
# from pathlib import Path
desired_caps = {}
desired_caps['platformName'] = 'Android'
# desired_caps['platformVersion'] = '5.1.1'
# desired_caps['platformVersion'] = '4.4.4'
# desired_caps['deviceName'] = 'VirtualDevice_1'
desired_caps['deviceName'] = 'android-ab192e8653eadd82'
desired_caps['app'] = 'C:\\Users\\Sam\\python\\wodezoon.apk'
# desired_caps['app'] = 'C:\\Users\\Sam\\python\\MyAPP.apk'

driver      =  webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
#
#name        =  driver.find_elements_by_android_uiautomator('new UiSelector().clickable(true)')
#name[2].click()
#name[2].send_keys('183XXXXX905') 
name        =   driver.find_element_by_class_name('android.widget.EditText')
button      =   driver.find_elements_by_class_name('android.widget.Button')
button[1].click()
time.sleep(10)
button[0].click()
tmp1 = ""
for i in range(1,3):
    tmp1 = tmp1 + "-" + str(i)
    print(i)
name.click()
name.send_keys(tmp1)
name.send_keys(Keys.ENTER)
time.sleep(10)
name.clear()
