# coding=gbk
'''
Created on 2011-8-5
测试最少时间是否为最少,最短路径是否为最短
@author: Administrator
'''
import fixture
from fixture import utility
from navapp import navitool
from navapp import autotest
from navapp import xxtool
import time
import os


def dotest(*args, **kwargs):
    its = True
    fixture.setup(its)
    navitool.set_silence(True)#打开静音，加快测试速度
    
    casesrcdir = kwargs['casesrcdir']
    casedstdir = kwargs['casedstdir']
    caseno = kwargs['caseno']
    try:
        fixture.copyfile(os.path.join(casesrcdir,caseno),os.path.join(casedstdir,'tbt0.db'))
    except:
        fixture.teardown()
        raise
    
    refroute = ''
    if(kwargs.has_key('refroute')):#途径点
        refroute = kwargs['refroute']
        
    bugpoint = None
    if(kwargs.has_key('bugpoint')):#截屏前将地图缩放至指定区域
        bugpoint = kwargs['bugpoint']
        
    scaleindex = None
    if(kwargs.has_key('scaleindex')):#截屏前将地图缩放至指定区域
        scaleindex = kwargs['scaleindex']
        
    if its: time.sleep(15)#Liulu说打开its后应等待6s
        
    routeinfo = []
    index = 0
    for mode in [5,0]:
        calctime,r = navitool.navi_route(kwargs['start_end'],'',mode)
        autotest.route_record()
        autotest.screen_snapshot('route%d.png'%index)
        routeinfo.append(r)
        if scaleindex != None:navitool.map_zoomscaleindex(scaleindex)
        if bugpoint != None:
            t = utility.trans_pointlst(bugpoint)
            navitool.map_setcenter(t[0]['lon'],t[0]['lat'])
            autotest.screen_snapshot('route0%d.png'%index)
        index = index + 1
        
    
    fixture.teardown()
    testok = True
    return testok, routeinfo

#以下仅为代码测试用            
if __name__ == "__main__":
    fixture.connectdevice()
    testok,rlst = dotest(start_end='11640745 3996754, 11644214 3992500,',bugpoint = '11643897,3992507',scaleindex=16,caseno='20110628T165439+08',casesrcdir='C:\\TestSource\\beijing\\',casedstdir='\\ResidentFlash\\CMMBDATA\\MOT\\TTI\\')
    fixture.closedevice()
    print(testok,rlst)
