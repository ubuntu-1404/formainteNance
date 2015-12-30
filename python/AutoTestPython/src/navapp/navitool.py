# coding=gbk
'''
Created on 2011-8-5

@author: Administrator
'''
import xxtool
import time
import sys
from fixture import utility
from xml.dom import minidom
from xml.dom.minidom import Node
#����Ϊ����ģʽ����ֹ������ɫ��һ��
def parse_interchange(xml):
    try:
        doc = minidom.parseString(xml)
    except:
        info=sys.exc_info()  
        print info[0],":",info[1]
        return []  
    node = doc.getElementsByTagName('xxml')[0]
    lst = [];
    for n in node.getElementsByTagName('record'):
        tmp = {}
        for p in n.childNodes:
            if(p.childNodes.length == 1):
                tmp[p.nodeName] = p.childNodes[0].nodeValue
            else:
                tmp[p.nodeName] = p.nodeValue
        lst.append(tmp)
    return lst
    
def set_daymode(daymode):
    xxtool.CallScript('''
        setting.set("autoday_mode", 0);
        uiman.set_daymode(%d);
        navi.daymode_set(%d);
        setting.set("night_mode", %d);
        uiman.refresh_state();
        '''%(daymode,daymode,daymode));

#���þ���ģʽ
def set_silence(bSilence):
    xxtool.CallScript('''
        interchange.parse( navi.voice_get());
        interchange.set("is_silence", %d);
        navi.voice_set(interchange.finalize());
        '''%(bSilence and 1 or 0));
        
#����ΪTTSģʽ����
def set_tts():
    xxtool.CallScript('''
        interchange.parse( navi.voice_get());
        interchange.set("is_tts", 1);
        navi.voice_set(interchange.finalize());
        ''');
        
#����Ϊ��������ģʽ����
def set_realvoice():
    xxtool.CallScript('''
        interchange.parse( navi.voice_get());
        interchange.set("is_tts", 0);
        navi.voice_set(interchange.finalize());
        ''');
        
#����ͼ��λ��ĳһ����������
def map_zoomrect(minlon,minlat,maxlon,maxlat):
    xxtool.CallScript('''
        interchange.clear();
        interchange.add_new();
        interchange.set("minlon", %d);
        interchange.set("minlat", %d);
        interchange.set("maxlon", %d);
        interchange.set("maxlat", %d);
        mainmap.zoomrect(interchange.finalize());
        global.set_variant("navi_guider", 1);
        uiman.refresh_state();
        '''%(minlon,minlat,maxlon,maxlat));
    
#���õ�ͼ������
def map_zoomscale(scale):
    xxtool.CallScript('''
        mainmap.zoomscale(%d);
        global.set_variant("navi_guider", 1);
        uiman.refresh_state();
        '''%scale);
    
#���õ�ͼ������
def map_zoomscaleindex(index):
    xxtool.CallScript('''
        mainmap.zoomscaleindex(%d);
        global.set_variant("navi_guider", 1);
        uiman.refresh_state();
        '''%index);
    
#���õ�ͼƽ��
def map_setcenter(lon,lat):
    xxtool.CallScript('''
        interchange.clear();
        interchange.add_new();
        interchange.set("lon",%d);
        interchange.set("lat",%d);
        mainmap.geocenter_set(interchange.finalize());
        uiman.refresh_state();
        '''%(lon,lat));
    
def map_lp2dp(lon,lat):
    v = parse_interchange(xxtool.CallScript('''
        interchange.clear();
        interchange.add_new();
        interchange.set("lon",%d);
        interchange.set("lat",%d);
        _xx_retval = mainmap.lp2dp(interchange.finalize());
        '''%(lon,lat)))
    return int(v[0]['x']),int(v[0]['y'])
   
    
def map_screensize():
    v = parse_interchange(xxtool.CallScript('''
        w = uiman.scr_width();
        h = uiman.scr_height();
        interchange.clear();
        interchange.add_new();
        interchange.set("x",w);
        interchange.set("y",h);
        _xx_retval = interchange.finalize();
        '''))
    return int(v[0]['x']),int(v[0]['y'])
#�������ٶ�����ǰ��ͼδ������ת����������
def map_currgeosizeofscreen():
    v = parse_interchange(xxtool.CallScript('''
        w = uiman.scr_width();
        h = uiman.scr_height();
        interchange.clear();
        interchange.add_new();
        interchange.set("x",0);
        interchange.set("y",0);
        interchange.parse(mainmap.dp2lp(interchange.finalize()));
        lon0 = interchange.get_int("lon");
        lat0 = interchange.get_int("lat");
        interchange.clear();
        interchange.add_new();
        interchange.set("x",w);
        interchange.set("y",h);
        interchange.parse(mainmap.dp2lp(interchange.finalize()));
        lon1 = interchange.get_int("lon");
        lat1 = interchange.get_int("lat");
        w = lon1 - lon0;
        h = lat0 - lat1;
        interchange.clear();
        interchange.add_new();
        interchange.set("x",w);
        interchange.set("y",h);
        _xx_retval = interchange.finalize();
        '''))
    return int(v[0]['x']),int(v[0]['y'])
    
#·������
#start,end:��ʼ��
#midLst:;�����б�Ϊ��[]��û��;����
#methodȡֵ����
#    NAV_RC_Option_Time = 0,
#    NAV_RC_Option_Distance = 1,
#    NAV_RC_Option_ExHighWay = 2,
#    NAV_RC_Option_Recommand = 3,
#    NAV_RC_Option_PreferHighWay = 4,
#��������������
#    1������·��������ʱ��(���Ϊ-1����������ʧ�ܣ�
#    2��·����Ϣ���ܳ�������ʱ�䣩
def navi_route(start_end,mid,method):
    start_end = utility.trans_decodecoor(start_end)
    mid = utility.trans_decodecoor(mid)
    nLst = utility.trans_pointlst(start_end)
    start = nLst[0]
    end = nLst[len(nLst)-1]
    midLst = utility.trans_pointlst(mid)
    for n in range(1,len(nLst)-1):
        midLst.append(nLst[n])
    calctime = 0
    xxtool.CallScript('''
        navi.waypoint_removeall();
        starttick = 0;
        calctime = 0;
        function calc_ok_event()
        {
            calctime = autotest.gettickcount() - starttick;
        }
        function calc_fail_event()
        {
            calctime = -1;
        }
        interchange.clear();
        interchange.add_new();
        interchange.set("name","%s");
        interchange.set("lon",%d);
        interchange.set("lat",%d);
        navi.waypoint_start_set(interchange.finalize());
        interchange.clear();
        interchange.add_new();
        interchange.set("name","%s");
        interchange.set("lon",%d);
        interchange.set("lat",%d);
        navi.waypoint_dest_set(interchange.finalize());
        starttick = autotest.gettickcount();
        autotest.setnavievent("onroutecalcsuccess","calc_ok_event();");
        autotest.setnavievent("onroutecalcfailed","calc_fail_event();");
        interchange.parse( navi.rc_mode_get() );
        interchange.set("rc_mode", %d);
        navi.rc_mode_set(interchange.finalize());
        interchange.parse( navi.rc_mode_get() );
        rtic_rc_mode = interchange.get_int("rc_mode");
        if (5 == rtic_rc_mode)
        {
            its.rcalc_enable(1);
            setting.set("rtic", 1);
        }
        else
        {
            its.rcalc_enable(0);
            setting.set("rtic", 0);
        }
        setting.set("autoswitch", 0);
        '''%("",start['lon'],start['lat'],"",end['lon'],end['lat'],method));
    for node in midLst:
        xxtool.CallScript('''
            interchange.clear();
            interchange.add_new();
            interchange.set("name","");
            interchange.set("lon",%d);
            interchange.set("lat",%d);
            navi.waypoint_insert(interchange.finalize());
            '''%(node['lon'],node['lat']));
        
    xxtool.CallScript('''
        navi.route_calc();
        ''');
    #��֮��5������һֱ�������Ƿ����
    for i in range(0,600):
        time.sleep(0.5)
        calctime = int(xxtool.CallScript('''
            _xx_retval = calctime;
            '''));
        if(calctime != 0):
            break
    route_info = parse_interchange(xxtool.CallScript('''
            if(calctime != -1)
            {
                interchange.parse(navi.route_info());
                interchange.set("boundrect","");
            }
            else{
                interchange.add_new();
                interchange.set("estimatetime",0);
                interchange.set("routedistance",0);
            }
            _xx_retval = interchange.finalize();
            '''))
    route_info[0]['estimatetime'] = int(route_info[0]['estimatetime'])
    route_info[0]['routedistance'] = int(route_info[0]['routedistance'])
    time.sleep(1)
    return calctime,route_info[0]

#��ʼ�����Ƿ���ƫ���ؼ���
#֮���趨�ڵ���navi_hasrecalc����Ƿ����ؼ���
def navi_recalclisten():
    xxtool.CallScript('''
        has_recalc = 0;
        function recalc_event()
        {
            has_recalc = 1;
        }
        autotest.setnavievent("onrouterecalc","recalc_event();");
        ''')
    
#�����navi_recalclisten���ù����Ƿ�����ƫ���ؼ���
def navi_hasrecalc():
    has_recalc = int(xxtool.CallScript('''
        _xx_retval = has_recalc;
        '''))
    return has_recalc != 0
    
#��ʼģ�⵼��
def navi_simnav():
    xxtool.CallScript('''
        global.set_variant("simu_start", 1);
        uiman.goto( "mapbrowse_$W_$H.ui" );
        ''');

#ֹͣģ�⵼��
def navi_simstop():
    xxtool.CallScript('''
        navi.simulation_stop();
        ''');
    
#��ȡ��λ��
def get_vehiclepos():
    val = xxtool.CallScript('''
        _xx_retval = navi.vehicle_position_get();
        ''');
    v = parse_interchange(val)
    return {'lon':int(v[0]['lon']),'lat':int(v[0]['lat']),'heading':int(v[0]['heading'])}

#��ȡ��Ļ�������ڵĵ�ͼλ��
def get_mapcenter():
    val = xxtool.CallScript('''
        _xx_retval = mainmap.geocenter_get();
        ''');
    v = parse_interchange(val)
    return {'lon':int(v[0]['lon']),'lat':int(v[0]['lat'])}

#districtcode 6λ��������
def find_keyword(findtype,districtccode,keyword):
    if findtype == 'poi':#��Ȥ��
        val = xxtool.CallScript('''
            find.set_find_type("around://?0X3000-0X3000,");
            ''');
    elif findtype == 'cross':#����·��
        val = xxtool.CallScript('''
            find.set_find_type("around://?0X2000-0X2000,");
            ''');
    elif findtype == 'address':#��ַ
        val = xxtool.CallScript('''
            find.set_find_type("around://?0X1000-0X1000,");
            ''');
    return parse_interchange(xxtool.CallScript('''
        interchange.clear();
        interchange.add_new();
        interchange.set("code",%d000);
        interchange.set("name","����");
        find.set_district(interchange.finalize());
        _xx_retval= find.find_by_keyword("%s",0);
        '''%(districtccode,keyword)))
    
def find_py(findtype,districtccode,py):
    if findtype == 'poi':#��Ȥ��
        val = xxtool.CallScript('''
            find.set_find_type("around://?0X3000-0X3000,");
            ''');
    elif findtype == 'cross':#����·��
        val = xxtool.CallScript('''
            find.set_find_type("around://?0X2000-0X2000,");
            ''');
    elif findtype == 'address':#��ַ
        val = xxtool.CallScript('''
            find.set_find_type("around://?0X1000-0X1000,");
            ''');
    return parse_interchange(xxtool.CallScript('''
        interchange.clear();
        interchange.add_new();
        interchange.set("code",%d000);
        interchange.set("name","����");
        find.set_district(interchange.finalize());
        _xx_retval= find.find_by_py("%s",0);
        '''%(districtccode,py)))  
    
def find_around(codeRange,lon,lat):
    xxtool.CallScript('''
        interchange.clear();
        ''')
    for c in codeRange:
        xxtool.CallScript('''
            interchange.add_new();
            interchange.set("id","%s");
            interchange.set("icon",0);
            '''%c)
        
    return parse_interchange(xxtool.CallScript('''
        tmp = interchange.finalize();
        interchange.clear();
        interchange.add_new();
        interchange.set("lon",%d);
        interchange.set("lat",%d);
        _xx_retval= find.find_by_around(tmp,interchange.finalize());
        '''%(lon,lat)))  
    