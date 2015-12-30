# coding=gbk
'''
Created on 2011-8-4

@author: Administrator
'''
from navapp import xxtool
from navapp import autotest
from navapp import navitool
import time
import fixture

fixture.connectdevice()
fixture.setup()

#navitool.map_zoomrect(11631696,4001431,11631896,4001631)
#calctime,routeinfo = navitool.navi_route('11622353 3999465, 11621518 3999359,','',0)
#navitool.navi_simnav()
#time.sleep(10)
#navitool.navi_simstop()
#tmpval = navitool.get_mapcenter()

result = navitool.find_keyword('address', 110000, '上地东路')
for p in result:
    print p['name']

autotest.play_uilog('touch01.log')
#autotest.set_navievent_logging("onstartsimunavi", 1000, 10)
#autotest.set_vposevent_logging('11622205,3999333',50,1000,10)

#autotest.play_nmea("Bug2309.nmea")
for i in range(0,200):
#    print(autotest.get_nmeatime())
    time.sleep(1.0)
#autotest.stop_nmea()
fixture.teardown()
fixture.closedevice()
