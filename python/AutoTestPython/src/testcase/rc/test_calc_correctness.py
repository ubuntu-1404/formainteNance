# coding=gbk
'''
Created on 2011-8-5
����·�߼��㾭������ԣ���Ҫ����������
@author: Administrator
'''
import fixture
from fixture import utility
from navapp import navitool
from navapp import autotest
import time


def dotest(*args, **kwargs):
    fixture.setup()

    compare_with = ''
    if(kwargs.has_key('compare_with')):#������
        compare_with = kwargs['compare_with']

    zoom_rect = None
    if(kwargs.has_key('zoom_rect')):#����ǰ����ͼ������ָ������
        zoom_rect = kwargs['zoom_rect']
        
    calc_mode = None
    if(kwargs.has_key('calc_mode')):#ָ������ģʽ,�����ָ�����������4��
        calc_mode = kwargs['calc_mode']
        
    routeinfo = []
    index = 0
    for mode in [0,1,4,2]:
        if calc_mode != None and calc_mode != mode:continue
        calctime,r = navitool.navi_route(kwargs['start_end'],'',mode)
        routeinfo.append(r)
        if zoom_rect != None:navitool.map_zoomrect(zoom_rect[0], zoom_rect[1], zoom_rect[2], zoom_rect[3])
        autotest.screen_snapshot('route%d.png'%index)
        index = index + 1
    #��������飬����·�߼����Ƿ���ֽϴ󶶶�
    if compare_with != '':
        for mode in [0,1,4,2]:
            if calc_mode != None and calc_mode != mode:continue
            calctime,r = navitool.navi_route(compare_with,'',mode)
            routeinfo.append(r)
            if zoom_rect != None:navitool.map_zoomrect(zoom_rect[0], zoom_rect[1], zoom_rect[2], zoom_rect[3])
            autotest.screen_snapshot('route%d.png'%index)
            index = index + 1
        
    
    fixture.teardown()
    testok = None#������޷�ֱ���ж�
    return testok, routeinfo

#���½�Ϊ���������            
if __name__ == "__main__":
    testok,rlst = dotest(start_end='11168220 4082530, 11628920 3991040,',calc_mode=2)
    print(testok,rlst)
