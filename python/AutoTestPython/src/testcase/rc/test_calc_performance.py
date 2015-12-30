# coding=gbk
'''
Created on 2011-8-5
����·����������
ÿ�������ֱ���4�ִ������ͼ���4�֣�ÿ�ּ���3��
@author: Administrator
'''
import fixture
from fixture import utility
from navapp import navitool
from navapp import autotest
import time


def dotest(*args, **kwargs):
    
    #time.sleep(10) #����5s����ʹ�õ�һ�βⶨֵ�ȶ�
    its = False
    if(kwargs.has_key('its')):#�Ƿ��ʵʱ��ͨ
        its = kwargs['its']
        
    routeinfo = []
    
    for mode in [0,1,4,2]:
        fixture.setup(its)#Ϊ��ȷ������ֵȷ����ÿ�ֶ�������������
        
        if its:  time.sleep(10)#Liulu˵��its��Ӧ�ȴ�6s
        time.sleep(5) #����5s����ʹ�õ�һ�βⶨֵ�ȶ�

        navitool.set_silence(True)#�򿪾������ӿ�����ٶ�
    
        #��һ��
        calctime,r = navitool.navi_route(kwargs['start_end'],'',mode)
        print 'first time'
        r['calctime'] = calctime
        routeinfo.append(r)
        time.sleep(5)
        #�ڶ���
        calctime,r = navitool.navi_route(kwargs['start_end'],'',mode)
        print 'second time'
        r['calctime'] = calctime
        routeinfo.append(r)
        time.sleep(5)
        #������
        calctime,r = navitool.navi_route(kwargs['start_end'],'',mode)
        print 'third time'
        r['calctime'] = calctime
        routeinfo.append(r)
        fixture.teardown()
        time.sleep(5)
    
    testok = True
    return testok, routeinfo

#���½�Ϊ���������            
if __name__ == "__main__":
    testok,rlst = dotest(start_end='2361-4132-7211----4519-1266-2472----2917-5611-5269')
    print(testok,rlst)
    testok,rlst = dotest(start_end='11723552 3916810, 11722671,3916104, 11723249 3916261,')
    print(testok,rlst)
    testok,rlst = dotest(start_end='11397863 2253835, 11410382 2255222,')
    print(testok,rlst)
