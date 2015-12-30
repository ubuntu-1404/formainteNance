# coding=gbk
'''
Created on 2011-8-5

@author: Administrator
'''
import xxtool
import re
import time
from fixture import utility
from fixture import SourceDir
from fixture import syncfile
_loggine_no_ = 0

#开关UI
def enable_ui(enable):
    xxtool.CallScript('''
        autotest.enable_ui(%d);
        '''%(enable and 1 or 0));
        
#回放nmea（从指定时间开始）
def play_nmea(nmeafile,startfrom = ''):
    t = re.split(':',startfrom)
    if len(t) < 3:
        t = [-1,-1,-1]
    return xxtool.PlayNmea(SourceDir + nmeafile,int(t[0]),int(t[1]),int(t[2]))
    
def stop_nmea():
    xxtool.StopNmea()
    
def get_nmeatime():
    return xxtool.GetNmeaTime()

def get_nmeapos():
    p = re.split(',',xxtool.GetNmeaPos())
    p[0] = int(p[0])
    p[1] = int(p[1])
    p[2] = float(p[2])
    p[3] = float(p[3])
    return p
#开始记录UILog，供回放使用
def record_uilog(logfile):
    xxtool.CallScript('''
        autotest.startuilog("%s");
        '''%(logfile));
    
#回放UILog
def play_uilog(logfile):
    syncfile(logfile)
    xxtool.CallScript('''
        autotest.playtouch("%s");
        '''%(logfile));
    
#截屏
def screen_snapshot(file):
    md_performance()#在这里调用是为了强制重新绘制
    xxtool.CallScript('''
        autotest.screenlogging("%s");
        '''%(file));
        
def voice_record(time):
    xxtool.CallScript('''
        autotest.voicelogging(%d);
        '''%(time));
    
def route_record():
    xxtool.CallScript('''
        autotest.routelogging(0,1);
        ''');
    
def set_navievent_logging(eventname,interval,times):
    global _loggine_no_
    _loggine_no_ = _loggine_no_ + 1
    xxtool.CallScript('''
        navievent_called = 0;
        function navievent_logging%d()
        {
            if(navievent_called == 0)
            {
                navievent_called = 1;
                autotest.screenlogging(%d,%d);
                autotest.voicelogging(%d*%d);
            }
        }
        autotest.setnavievent("%s","navievent_logging%d();");
        '''%(_loggine_no_,interval,times,interval,times,eventname,_loggine_no_));

def check_navievent():
    return int(xxtool.CallScript('''
        _xx_retval = navievent_called;
        '''))==1;
    
def set_vposevent_logging(vpos,radius,interval,times):
    global _loggine_no_
    _loggine_no_ = _loggine_no_ + 1
    v = utility.trans_pointlst(vpos)
    xxtool.CallScript('''
        vposevent_called = 0;
        function vposevent_logging%d()
        {
            if(vposevent_called == 0){
                vposevent_called = 1;
                autotest.screenlogging(%d,%d);
                autotest.voicelogging(%d*%d);
            }
        }
        autotest.setvposevent(%d,%d,%d,"vposevent_logging%d();");
        '''%(_loggine_no_,interval,times,interval,times,v[0]['lon'],v[0]['lat'],radius,_loggine_no_));

def check_vposevent():
    return int(xxtool.CallScript('''
        _xx_retval = vposevent_called;
        '''))==1;
    
def set_timeevent_logging(time,interval,times):
    global _loggine_no_
    _loggine_no_ = _loggine_no_ + 1
    xxtool.CallScript('''
        timeevent_called = 0;
        function timeevent_logging%d()
        {
            if(timeevent_called == 0){
                timeevent_called = 1;
                autotest.screenlogging(%d,%d);
                autotest.voicelogging(%d*%d);
            }
            global.kill_timer(timerid%d);
        }
        timerid%d = global.set_timer("timeevent_logging%d();",%d);    
        '''%(_loggine_no_,interval,times,interval,times,_loggine_no_,_loggine_no_,_loggine_no_,time));
        
def check_timeevent():
    return int(xxtool.CallScript('''
        _xx_retval = timeevent_called;
        '''))==1;

#在程序结束前保存所有截图
#在设备时，由于需要保存到Flash上，这一过程比较慢
def save_all():
    print "Saving files..."
    xxtool.CallScript('''
        autotest.saveall();
        ''')
    for i in range(0,1000):
        if (int(xxtool.CallScript('''
            _xx_retval = autotest.issaveover();
            '''))==1):
            break
        time.sleep(1)
    print "Saving over."
    
#测试MD帧绘制效率
def md_performance():
    return int(xxtool.CallScript('''
        _xx_retval = autotest.displayperf();
        '''))
    