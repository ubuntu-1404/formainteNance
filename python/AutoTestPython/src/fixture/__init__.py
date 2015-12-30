# coding=gbk
import time
from navapp import xxtool
import os
import shutil

#_ExeNamePC = 'E:\\workspace\\xproduct\\apollo_cyx2.7_test\\trunk\\xxnav\\scriptUI\\bin\\sosod.exe' 
_ExeNamePC = 'E:\\PC版\\cyx15Q2_beijing\\sosod.exe' 
#第二导航路径
_ExeNamePND = '\\SDMMC\\XXNAV\\MCNE_YF.exe'
#第一导航路径
#_ExeNamePND = '\\ResidentFlash2\\APP\\XXNAV\\MCNE_YF.exe'
#_ExeNamePND = '\\ResidentFlash\\ITS_NAV\\MCNE_YF.exe'
_OutDirPND = '\\ResidentFlash2\\tmp\\'

OutDir = 'E:\\tool\\自动化测试工具\\test\\tmp\\'
SourceDir = 'E:\\tool\\自动化测试工具\\test\\TestSource\\'
ClassName = 'soso_class'
RunOnDevice = False
def connectdevice():
    global RunOnDevice
    RunOnDevice = True
    xxtool.StartDevice()
    
def closedevice():
    global RunOnDevice
    RunOnDevice = False
    xxtool.StopDevice()
    
def setup(its = False):#缺省关闭its，因为its启动后几秒内会因接收数据导致响应迟钝，影响测试结果。
    #print 'enter step'
    global RunOnDevice
    from navapp import navitool
    for p in os.listdir(OutDir):
        f = os.path.join( OutDir, p )
        if os.path.isfile( f ):
            try:
                os.remove( f )
            except os.error:
                print('临时文件删除失败:'+f)
    #print 'run step  delete file'
    if RunOnDevice:
        xxtool.DeleteFilesOnDevice(_OutDirPND)
    #print 'run step  %s' % (_OutDirPND)
    f = open(os.path.join(OutDir,"start.xjs"), "w")
    
    f.write('''
        setting.set("its",%d);
        '''%(its and 1 or 0))
    f.close()
    #print 'run step  write start.xjs'
    if RunOnDevice:
        #print 'run step  RunOnDevice copytodevi'
        xxtool.CopyFileToDevice(os.path.join(OutDir,"start.xjs"),os.path.join(_OutDirPND,"start.xjs"))
        
    if not xxtool.Setup(RunOnDevice and _ExeNamePND or _ExeNamePC, "autotest://start.xjs 0 " + (RunOnDevice and _OutDirPND or OutDir), ClassName):
        raise '不能启动导航程序'
    #print 'run step  xxtool run, and wait 4'
    time.sleep(4)
    navitool.set_daymode(0)
    #print 'run step  set_daymode'
    navitool.set_tts()
    #print 'exit step '
        
def teardown():
    global RunOnDevice
    from navapp import autotest
    try:
        autotest.save_all()
    except:
        None
    xxtool.TearDown()
    if RunOnDevice:
        xxtool.CopyFilesFromDevice(_OutDirPND,OutDir)
    
def syncfile(file):
    global RunOnDevice
    shutil.copyfile(SourceDir + file,OutDir + file)
    if RunOnDevice:
        xxtool.CopyFileToDevice(OutDir + file,_OutDirPND + file)
    
def copyfile(srcfile,dstfile):
    global RunOnDevice
    if not os.path.isfile(srcfile):
        raise "error"
    if RunOnDevice:
        xxtool.CopyFileToDevice(srcfile,dstfile)
    else:
        shutil.copyfile(srcfile,dstfile)
    