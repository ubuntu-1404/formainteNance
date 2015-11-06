'''
Created on 2015年10月11日

@author: Sam
'''
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

parts = {2,0,0,0}
deltatime = 0.5
driver = webdriver.Firefox()
driver.get("http://192.168.102.6:8080/doudou")
# driver.get("http://192.168.12.2:8080/doudou")


#logon
elem = driver.find_element_by_name("username")
elem.send_keys("admin")
elem = driver.find_element_by_name("pwd")
elem.send_keys("123")
elem = driver.find_element_by_class_name("btn-green")
elem.click()
# elem.send_keys(Keys.RETURN)
for par in parts :
    if par == 1 :
    ########################选择用户管理############################
        driver.switch_to_default_content()
        driver.switch_to_frame("top01")
        elem = driver.find_elements_by_css_selector('*[id=user001]')
        elem[0].click()
        
        # 打开厂家管理并单击厂家添加
        driver.switch_to_default_content()
        driver.switch_to_frame("home01")
        driver.switch_to_frame("user_side01")
        elem = driver.find_elements_by_css_selector('*[id=user_side_a_ID002]')
        elem[0].click()
        driver.implicitly_wait(deltatime)
        elem = driver.find_elements_by_css_selector('*[id=rightadd]')
        elem[0].click()
        #厂家管理添加用户信息
        pname = "XiaoMi"
        paddr = "北京市海淀区上地七街1号"
        driver.switch_to_default_content()
        driver.switch_to_frame("home01")
        driver.switch_to_frame("user_show01")
        elem = driver.find_elements_by_css_selector('*[id=prodName]')
        elem[0].send_keys(pname)
        elem = driver.find_elements_by_css_selector('*[id=prodaddress]')
        elem[0].send_keys(paddr)
        elem = driver.find_elements_by_css_selector('*[id=rights_btn-green_id]')
        elem[0].click()
        
        # 打开用户管理并单击添加用户
        driver.switch_to_default_content()
        driver.switch_to_frame("home01")
        driver.switch_to_frame("user_side01")
        elem = driver.find_elements_by_css_selector('*[id=user_side_a_ID001]')
        elem[0].click()
        driver.implicitly_wait(deltatime)
        elem = driver.find_elements_by_css_selector('*[id=useradd]')
        elem[0].click()
        #填写新添加的用户信息
        pname = "XiaoMiAdmin"
        ppswd = "mipwd"
        driver.switch_to_default_content()
        driver.switch_to_frame("home01")
        driver.switch_to_frame("user_show01")
        elem = driver.find_elements_by_css_selector('*[id=loginName]')
        elem[0].send_keys(pname)
        elem = driver.find_element_by_css_selector('*[id=roelId]')
        select1 = Select(elem)
        select1.select_by_index(1)
        elem = driver.find_element_by_css_selector('*[id=produceid]')
        select1 = Select(elem)
        select1.select_by_index(1)
        elem = driver.find_elements_by_css_selector('input[id=password1]')
        elem[0].send_keys(ppswd)
        elem = driver.find_element_by_css_selector('input[name=rePwd]')
        elem.click()
        elem.send_keys(ppswd)
        elem = driver.find_elements_by_css_selector('*[id=user_btn-green_id]')
        elem[0].click()
    
    if par == 2:
    ########################升级管理############################
        for rounds in range(10000) :
            round = str(rounds)
            labround = rounds
            driver.switch_to_default_content()
            driver.switch_to_frame("top01")
            elem = driver.find_elements_by_css_selector('*[id=sjgl001]')
            elem[0].click()
            
            # 打开系统型号并单击型号添加################
            driver.switch_to_default_content()
            driver.switch_to_frame("home01")
            driver.switch_to_frame("side0001")
            elem = driver.find_elements_by_css_selector('*[id=side0001001]')
            elem[0].click()
            driver.implicitly_wait(deltatime)
            elem = driver.find_elements_by_css_selector('*[id=sysadd]')
            elem[0].click()
            #系统型号添加信息
            pname = "SysType-"+round
            driver.switch_to_default_content()
            driver.switch_to_frame("home01")
            driver.switch_to_frame("show0001")
            elem = driver.find_elements_by_css_selector('*[id=sysvalue]')
            elem[0].send_keys(pname)
            elem = driver.find_element_by_css_selector('*[id=produceid]')
            select1 = Select(elem)
            select1.select_by_index(1)
            elem = driver.find_elements_by_css_selector('*[id=sys_add_btn_id001]')
            elem[0].click()
            
            # 打开固件型号并单击型号添加################
            driver.switch_to_default_content()
            driver.switch_to_frame("home01")
            driver.switch_to_frame("side0001")
            elem = driver.find_elements_by_css_selector('*[id=side0001002]')
            elem[0].click()
            driver.implicitly_wait(deltatime)
            elem = driver.find_elements_by_css_selector('*[id=firmadd]')
            elem[0].click()
            #固件型号添加信息
            pname = "DevType-"+round
            driver.switch_to_default_content()
            driver.switch_to_frame("home01")
            driver.switch_to_frame("show0001")
            elem = driver.find_elements_by_css_selector('*[id=firmvalue]')
            elem[0].send_keys(pname)
            elem = driver.find_element_by_css_selector('*[id=produceid]')
            select1 = Select(elem)
            select1.select_by_index(1)
            elem = driver.find_elements_by_css_selector('*[id=sys_add_btn_id005]')
            elem[0].click()
            
            # 打开系统包管理并单击系统包上传################
            driver.switch_to_default_content()
            driver.switch_to_frame("home01")
            driver.switch_to_frame("side0001")
            elem = driver.find_elements_by_css_selector('*[id=side0001003]')
            elem[0].click()
            driver.implicitly_wait(deltatime)
            elem = driver.find_elements_by_css_selector('*[id=packadd]')
            elem[0].click()
            #固件型号添加信息
            pname = "DevType-"+round
            driver.switch_to_default_content()
            driver.switch_to_frame("home01")
            driver.switch_to_frame("show0001")
            elem = driver.find_elements_by_css_selector('*[id=modelId]')
            elem[labround].click()
            elem = driver.find_elements_by_css_selector('*[id=packvalue]')
            elem[0].send_keys(pname)
            elem = driver.find_element_by_css_selector('*[id=packageType]')
            select1 = Select(elem)
            select1.select_by_index(1)
            elem = driver.find_elements_by_css_selector('*[id=packFile]')
            elem[0].send_keys("C:\\Users\\Sam\\Desktop\\V126-V127.zip")
            elem = driver.find_elements_by_css_selector('*[id=describe]')
            elem[0].send_keys("C:\\Users\\Sam\\Desktop\\V126-V127.zip")
            elem = driver.find_elements_by_css_selector('*[id=sys_add_btn_id002]')
            elem[0].click()
            
            # 打开动画管理并单击动画上传################
            driver.switch_to_default_content()
            driver.switch_to_frame("home01")
            driver.switch_to_frame("side0001")
            elem = driver.find_elements_by_css_selector('*[id=side0001004]')
            elem[0].click()
            driver.implicitly_wait(deltatime)
            elem = driver.find_elements_by_css_selector('*[id=aniadd]')
            elem[0].click()
            #动画上传添加信息
            pname = "CartoonName-"+round
            driver.switch_to_default_content()
            driver.switch_to_frame("home01")
            driver.switch_to_frame("show0001")
            elem = driver.find_elements_by_css_selector('*[id=modelId]')
            elem[labround].click()
            elem = driver.find_element_by_css_selector('*[id=aniName]')
            elem.send_keys(pname)
            elem = driver.find_elements_by_css_selector('*[id=aniFile]')
            elem[0].send_keys("C:\\Users\\Sam\\Desktop\\V126-V127.zip")
            elem = driver.find_elements_by_css_selector('*[id=describe]')
            elem[0].send_keys("C:\\Users\\Sam\\Desktop\\V126-V127.zip")
            elem = driver.find_elements_by_css_selector('*[id=sys_add_btn_id007]')
            elem[0].click()
            
            # 打开固件管理并单击动画上传################
            driver.switch_to_default_content()
            driver.switch_to_frame("home01")
            driver.switch_to_frame("side0001")
            elem = driver.find_elements_by_css_selector('*[id=side0001005]')
            elem[0].click()
            driver.implicitly_wait(deltatime)
            elem = driver.find_elements_by_css_selector('*[id=wareadd]')
            elem[0].click()
            #固件上传添加信息
            pname = "DevName-"+round
            driver.switch_to_default_content()
            driver.switch_to_frame("home01")
            driver.switch_to_frame("show0001")
            elem = driver.find_elements_by_css_selector('*[id=modelId]')
            elem[labround].click()
            elem = driver.find_element_by_css_selector('*[id=firmVersion]')
            elem.send_keys(pname)
            elem = driver.find_elements_by_css_selector('*[id=firmFile]')
            elem[0].send_keys("C:\\Users\\Sam\\Desktop\\V126-V127.zip")
            elem = driver.find_elements_by_css_selector('*[id=describe]')
            elem[0].send_keys("C:\\Users\\Sam\\Desktop\\V126-V127.zip")
            elem = driver.find_elements_by_css_selector('*[id=sys_add_btn_id004]')
            elem[0].click()
            
            # 打开APP管理并单击APP上传################
            pathAPP="C:\\Users\\Sam\\Desktop\\XxLauncher.apk"
            pictureAddr="C:\\Users\\Sam\Desktop\\APPpicture.jpg"
            driver.switch_to_default_content()
            driver.switch_to_frame("home01")
            driver.switch_to_frame("side0001")
            elem = driver.find_elements_by_css_selector('*[id=side0001006]')
            elem[0].click()
            driver.implicitly_wait(deltatime)
            elem = driver.find_elements_by_css_selector('*[id=appadd]')
            elem[0].click()
            #APP上传添加信息
            driver.switch_to_default_content()
            driver.switch_to_frame("home01")
            driver.switch_to_frame("show0001")
            elem = driver.find_elements_by_css_selector('*[id=modelId]')
            elem[labround].click()
            elem = driver.find_elements_by_css_selector('*[id=appFile]')
            elem[0].send_keys(pathAPP)
            elem = driver.find_elements_by_css_selector('*[id=describe]')
            elem[0].send_keys(pathAPP+pathAPP+pathAPP)
            elem = driver.find_element_by_css_selector('*[id=appClassify]')
            select1 = Select(elem)
            select1.select_by_index(1)
            elem = driver.find_element_by_css_selector('*[id=appRecommend]')
            select1 = Select(elem)
            select1.select_by_index(1)
            for i in range(1, 6):
                elem = driver.find_elements_by_css_selector('*[id=appPicture]')
                elem[0].send_keys(pictureAddr)
                driver.implicitly_wait(deltatime-0.2)
            driver.implicitly_wait(deltatime)
            elem = driver.find_elements_by_css_selector('*[id=sys_add_btn_id006]')
            elem[0].click()
# driver.close()