# coding=gbk
'''
Created on 2011-8-23
����nmea��RG����
@author: Administrator
'''
import fixture
from fixture import utility
from navapp import navitool
from navapp import autotest
import time
import re
import string


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
        
    #ָ������ʱ��,t[0]����ʱ����� t[1] bugʱ���
    time_span = kwargs['time_span']
    t = re.split(' ',time_span)
    #��������
    plist = re.split(', *',kwargs['start_end'])
    start_time = ''
    if len(re.findall('\d+:\d+:\d+',plist[0])) == 1:
        start_time = plist[0]
    nmea = kwargs['nmea']
    #����nmea
    if not autotest.play_nmea(nmea,t[0]):
        raise "Can't open nmea file"
    #��ȡnmea������ǰʱ��
    curr_time = autotest.get_nmeatime()
    route_calc = False
    navitool.map_zoomscale(scale)
    isbugpoint = (len(re.findall('\d+:\d+:\d+',t[1])) == 0)
    if isbugpoint:
        autotest.set_vposevent_logging(t[1], radius, 1000, int(duration))
    def checkbug():
        if isbugpoint:
            return autotest.check_vposevent()
        else:
            return utility.compare_time(t[1],curr_time) <= 0
    #δ����bug��
    while not checkbug():
        #�ж�ƫ����ƫ�����ؼ���·�ߣ��������nmea����
        if not route_calc:
            #·����ʱ��Ϊ���
            if start_time != '':
                #·�����ָ����ʱ�䵽����ʼ����
                if utility.compare_time(curr_time,start_time)>=0:
                    start_pos = autotest.get_nmeapos()
                    #����ʼʱ���滻Ϊ���������λ��,����·����γ���ַ���
                    new_list = re.sub('\d+:\d+:\d+','%d %d'%(start_pos[0],start_pos[1]),kwargs['start_end'])
                    calctime,rlst = navitool.navi_route(new_list,'',calc_type)
                    if calctime == -1:
                        raise '·���������'
                    route_calc = True
            #·��Ϊ��γ��
            else:
                calctime,rlst = navitool.navi_route(kwargs['start_end'],'',calc_type)
                if calctime == -1:
                    raise '·���������'  
                route_calc = True
        #����nmea���� 
        curr_time = autotest.get_nmeatime()
        time.sleep(1)
    if not isbugpoint:
        #���Ͻ���
        autotest.set_timeevent_logging(0, 1000, int(duration))
    autotest.screen_snapshot('route0.png')   
    time.sleep(duration*1.2)            
    fixture.teardown()
    return None
    
if __name__ == "__main__":
    testok = dotest(start_end='17:02:36, 11628920 4000220',time_span='17:33:36 17:35:00',nmea='bug_5665.nmea') 
    print(testok) 
    