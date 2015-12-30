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
    
    #指定测试时间
    time_span = kwargs['time_span']
    t = re.split(' ',time_span)
    #坐标序列
    plist = re.split(', *',kwargs['start_end'])
    start_time = ''
    if len(re.findall('\d+:\d+:\d+',plist[0])) == 1:
        start_time = plist[0]
    nmea = kwargs['nmea']
    
    expect_recalc = kwargs['expect_recalc']
    
    #播放nmea
    if not autotest.play_nmea(nmea,t[0]):
        raise "Can't open nmea file"
    curr_time = autotest.get_nmeatime()
    route_calc = False
    recalc = False
    #开始监听是否偏航重计算
    navitool.navi_recalclisten()
    while utility.compare_time(t[1],curr_time) > 0:
        if not route_calc:
            if start_time != '':
                #路线起点指定的时间到，开始计算
                if utility.compare_time(curr_time,start_time)>=0:
                    start_pos = autotest.get_nmeapos()
                    #将起始时间替换为具体的坐标位置
                    new_list = re.sub('\d+:\d+:\d+','%d %d'%(start_pos[0],start_pos[1]),kwargs['start_end'])
                    calctime,rlst = navitool.navi_route(new_list,'',0)
                    if calctime == -1:
                        raise '路径计算错误'            
                    route_calc = True
            else:
                calctime,rlst = navitool.navi_route(kwargs['start_end'],'',0)
                if calctime == -1:
                    raise '路径计算错误'            
                route_calc = True
        recalc = navitool.navi_hasrecalc()
        curr_time = autotest.get_nmeatime()
        time.sleep(1)
                
    fixture.teardown()
    return expect_recalc == recalc

if __name__ == "__main__":
    testok = dotest(start_end='11403840 2252390, 11635960 4008380',time_span='18:53:00 18:54:23',nmea='Bug20110217.nmea',expect_recalc=True)
    print(testok)
#    testok = dotest(start_end='15:34:00, 11636902 4000570, 11646553 4005434',time_span='15:34:00 15:37:00',nmea='Bug2481.nmea',expect_recalc=True)
#    print(testok)
#    testok = dotest(start_end='10808397 3500024, 11619167 3994232,',time_span='11:49:4 11:50:10',nmea='BugRecalc01.nmea',expect_recalc=True)
#    print(testok)
#    testok = dotest(start_end='0:06:01, 11619167 3994232',time_span='0:06:01 0:07:00',nmea='BugRecalc03.nmea',expect_recalc=False)
#    print(testok)
#    testok = dotest(start_end='16:23:25, 11619167 3994232',time_span='16:23:25 16:26:00',nmea='BugRecalc02.nmea',expect_recalc=False)
#    print(testok)

