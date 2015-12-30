# coding=gbk
'''
Created on 2011-8-8

@author: Administrator
'''
import fixture
from fixture import utility
from navapp import navitool
from navapp import autotest
import time
import re


def dotest(*args, **kwargs):
    fixture.setup()
    
    calc_type = 0#���δ�ر�ָ�������㷽ʽ��Ϊʱ�����
    if kwargs.has_key('calc_type'):
        calc_type = kwargs['calc_type']
    radius = 50#���δ�ر�ָ����Bug������ָ����50����
    if kwargs.has_key('radius'):
        radius = kwargs['radius']
    duration = 15#���δ�ر�ָ����log��¼Ϊ15��
    if kwargs.has_key('duration'):
        duration = kwargs['duration']
    scale = 10000#���δ�ر�ָ������ͼ������Ϊ10000
    if kwargs.has_key('scale'):
        scale = kwargs['scale']

    calctime,rlst = navitool.navi_route(kwargs['start_end'],'',calc_type)
    if calctime == -1:
        raise '·���������'     
    navitool.navi_simnav()
    navitool.map_zoomscale(scale)
    autotest.set_vposevent_logging(kwargs['bugpoint'], radius, 1000, int(duration))
    tick = 0
    while not autotest.check_vposevent():
        time.sleep(1)
        tick = tick + 1
        if tick > 300:#����5���ӵĲ�����Ϊ��ʱ
            fixture.teardown()
            raise RuntimeError('���Գ�ʱ')
            break
    autotest.screen_snapshot('route0.png')
      
    time.sleep(duration*1.2)
    navitool.navi_simstop()
    fixture.teardown()
    return None

if __name__ == "__main__":
    fixture.connectdevice()
    testok = dotest(start_end='11327488 2313188, 11327903 2312859,',bugpoint='11327499,2313187')
    fixture.closedevice()
    print(testok)
#    testok = dotest(start_end='11622353 3999465, 11621518 3999359,',bugpoint='11622205,3999333')
#    print(testok)

