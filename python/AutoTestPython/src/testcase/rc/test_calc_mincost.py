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
import time


def dotest(*args, **kwargs):
    its = False
    if(kwargs.has_key('its')):#是否打开实时交通
        its = kwargs['its']
        
    fixture.setup(its)
    navitool.set_silence(True)#打开静音，加快测试速度
    
    refroute = ''
    if(kwargs.has_key('refroute')):#途径点
        refroute = kwargs['refroute']
        
    bugpoint = None
    if(kwargs.has_key('bugpoint')):#截屏前将地图缩放至指定区域
        bugpoint = kwargs['bugpoint']
        
    scaleindex = None
    if(kwargs.has_key('scaleindex')):#截屏前将地图缩放至指定区域
        scaleindex = kwargs['scaleindex']
        
    snapshot = False
    if(kwargs.has_key('snapshot')):#截屏
        snapshot = kwargs['snapshot']
        
    if its: time.sleep(6)#Liulu说打开its后应等待6s
        
    routeinfo = []
    index = 0
    for mode in [0,1,4,2]:
        calctime,r = navitool.navi_route(kwargs['start_end'],'',mode)
        autotest.route_record()
        routeinfo.append(r)
        if scaleindex != None:navitool.map_zoomscaleindex(scaleindex)
        if bugpoint != None:
            t = utility.trans_pointlst(bugpoint)
            navitool.map_setcenter(t[0]['lon'],t[0]['lat'])
        if snapshot :autotest.screen_snapshot('route%d.png'%index)
        index = index + 1
    #加入途径点再计算一轮
    if refroute != '':
        for mode in [0,1,4,2]:
            calctime,r = navitool.navi_route(kwargs['refroute'],'',mode)
            autotest.route_record()
            routeinfo.append(r)
            if scaleindex != None:navitool.map_zoomscaleindex(scaleindex)
            if bugpoint != None:
                t = utility.trans_pointlst(bugpoint)
            if snapshot :autotest.screen_snapshot('route%d.png'%index)
            index = index + 1
        
    
    fixture.teardown()
    testok = True
    for r in routeinfo:
        if routeinfo[0]['estimatetime'] > r['estimatetime']:
            testok = False 
        if routeinfo[1]['routedistance'] > r['routedistance']:
            testok = False 
    return testok, routeinfo

#以下仅为代码测试用            
if __name__ == "__main__":
    try:
        testok,rlst = dotest(start_end='12343828 4177975, 12437403 4013394,')
        print(testok,rlst)
    except:
        print '被测试程序出现崩溃，测试终止'
    testok,rlst = dotest(start_end='11723552 3916810, 11723249 3916261,',refroute='11723552 3916810, 11722671,3916104, 11723249 3916261,')
    print(testok,rlst)
    testok,rlst = dotest(start_end='11397863 2253835, 11410382 2255222,')
    print(testok,rlst)
    testok,rlst = dotest(start_end='11723552 3916810, 11723249 3916261,',snapshot=True)
    print(testok,rlst)
