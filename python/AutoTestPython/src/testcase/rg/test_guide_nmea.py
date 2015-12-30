# coding=gbk
'''
Created on 2011-8-23
加入nmea的RG测试
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
        
    #指定测试时间,t[0]测试时间起点 t[1] bug时间点
    time_span = kwargs['time_span']
    t = re.split(' ',time_span)
    #坐标序列
    plist = re.split(', *',kwargs['start_end'])
    start_time = ''
    if len(re.findall('\d+:\d+:\d+',plist[0])) == 1:
        start_time = plist[0]
    nmea = kwargs['nmea']
    #播放nmea
    if not autotest.play_nmea(nmea,t[0]):
        raise "Can't open nmea file"
    #获取nmea导航当前时间
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
    #未到达bug点
    while not checkbug():
        #判定偏航，偏航后重计算路线，否则继续nmea引导
        if not route_calc:
            #路线以时间为起点
            if start_time != '':
                #路线起点指定的时间到，开始计算
                if utility.compare_time(curr_time,start_time)>=0:
                    start_pos = autotest.get_nmeapos()
                    #将起始时间替换为具体的坐标位置,生成路径经纬度字符串
                    new_list = re.sub('\d+:\d+:\d+','%d %d'%(start_pos[0],start_pos[1]),kwargs['start_end'])
                    calctime,rlst = navitool.navi_route(new_list,'',calc_type)
                    if calctime == -1:
                        raise '路径计算错误'
                    route_calc = True
            #路线为经纬度
            else:
                calctime,rlst = navitool.navi_route(kwargs['start_end'],'',calc_type)
                if calctime == -1:
                    raise '路径计算错误'  
                route_calc = True
        #继续nmea引导 
        curr_time = autotest.get_nmeatime()
        time.sleep(1)
    if not isbugpoint:
        #马上截屏
        autotest.set_timeevent_logging(0, 1000, int(duration))
    autotest.screen_snapshot('route0.png')   
    time.sleep(duration*1.2)            
    fixture.teardown()
    return None
    
if __name__ == "__main__":
    testok = dotest(start_end='17:02:36, 11628920 4000220',time_span='17:33:36 17:35:00',nmea='bug_5665.nmea') 
    print(testok) 
    