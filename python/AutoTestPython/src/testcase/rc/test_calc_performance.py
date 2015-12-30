# coding=gbk
'''
Created on 2011-8-5
测试路径计算性能
每组用例分别按照4种代价类型计算4轮，每轮计算3次
@author: Administrator
'''
import fixture
from fixture import utility
from navapp import navitool
from navapp import autotest
import time


def dotest(*args, **kwargs):
    
    #time.sleep(10) #休眠5s可以使得第一次测定值稳定
    its = False
    if(kwargs.has_key('its')):#是否打开实时交通
        its = kwargs['its']
        
    routeinfo = []
    
    for mode in [0,1,4,2]:
        fixture.setup(its)#为了确保计算值确定，每轮都重新启动程序
        
        if its:  time.sleep(10)#Liulu说打开its后应等待6s
        time.sleep(5) #休眠5s可以使得第一次测定值稳定

        navitool.set_silence(True)#打开静音，加快测试速度
    
        #第一次
        calctime,r = navitool.navi_route(kwargs['start_end'],'',mode)
        print 'first time'
        r['calctime'] = calctime
        routeinfo.append(r)
        time.sleep(5)
        #第二次
        calctime,r = navitool.navi_route(kwargs['start_end'],'',mode)
        print 'second time'
        r['calctime'] = calctime
        routeinfo.append(r)
        time.sleep(5)
        #第三次
        calctime,r = navitool.navi_route(kwargs['start_end'],'',mode)
        print 'third time'
        r['calctime'] = calctime
        routeinfo.append(r)
        fixture.teardown()
        time.sleep(5)
    
    testok = True
    return testok, routeinfo

#以下仅为代码测试用            
if __name__ == "__main__":
    testok,rlst = dotest(start_end='2361-4132-7211----4519-1266-2472----2917-5611-5269')
    print(testok,rlst)
    testok,rlst = dotest(start_end='11723552 3916810, 11722671,3916104, 11723249 3916261,')
    print(testok,rlst)
    testok,rlst = dotest(start_end='11397863 2253835, 11410382 2255222,')
    print(testok,rlst)
