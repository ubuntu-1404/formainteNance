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
    
    calc_type = 0#如果未特别指定，计算方式都为时间最短
    if kwargs.has_key('calc_type'):
        calc_type = kwargs['calc_type']
    radius = 50#如果未特别指定，Bug发生在指定点50米内
    if kwargs.has_key('radius'):
        radius = kwargs['radius']
    duration = 15#如果未特别指定，log记录为15秒
    if kwargs.has_key('duration'):
        duration = kwargs['duration']
    scale = 10000#如果未特别指定，地图比例尺为10000
    if kwargs.has_key('scale'):
        scale = kwargs['scale']

    calctime,rlst = navitool.navi_route(kwargs['start_end'],'',calc_type)
    if calctime == -1:
        raise '路径计算错误'     
    navitool.navi_simnav()
    navitool.map_zoomscale(scale)
    autotest.set_vposevent_logging(kwargs['bugpoint'], radius, 1000, int(duration))
    tick = 0
    while not autotest.check_vposevent():
        time.sleep(1)
        tick = tick + 1
        if tick > 300:#超过5分钟的测试视为超时
            fixture.teardown()
            raise RuntimeError('测试超时')
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

