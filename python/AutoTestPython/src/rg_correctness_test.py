# coding=gbk
'''
Created on 2011-8-7

@author: Administrator
'''
import win32com.client
import traceback
from navapp import autotest
from navapp import navitool
from testcase.rg import test_guide_correctness
from testcase.rg import test_guide_nmea
import time
import fixture
import re
import os
import shutil

TestName = 'RG合理性测试'
localt = time.localtime()
TestTime = '%04d-%02d-%02d-%02d-%02d-%02d'%(localt[0],localt[1],localt[2],localt[3],localt[4],localt[5])

#fixture.connectdevice()

excel = win32com.client.Dispatch("Excel.Application")
excel.DisplayAlerts = False
filename = (fixture.SourceDir + 'RG_Bug用例库.xlsx').decode('gbk')
output = (fixture.OutDir + 'RG基础数据应用层测试检查list_output.xls').decode('gbk')
d1 = excel.Workbooks.Open(Filename = filename)
sheet = d1.Sheets('RG用例库')
#为了截图调整列宽
sheet.Columns('J:J').ColumnWidth = 24
sheet.Columns('k:k').ColumnWidth = 24
for line in range(20,25):
    o = sheet.Range('E%d'%line)
    ref = sheet.Range('F%d'%line)
    col = "J%d" % line
    bug_nmea = sheet.Range('i%d'%line)
    if(len(o.Text)!=0) and len(ref.Text)!=0:
        print('Calculating... ' + o.Text)
        reflst = ref.Text.encode('utf-8')
        bug_nmea1 = bug_nmea.Text.encode('utf-8')
        try:
            if len(bug_nmea1) != 0:
                testok = test_guide_nmea.dotest(start_end=o.Text.encode('utf-8'),time_span=reflst,nmea=bug_nmea1)   
            else:
                testok = test_guide_correctness.dotest(start_end=o.Text.encode('utf-8'),bugpoint=reflst)     
            file_object = open(os.path.join(fixture.OutDir,"voice.log"),"r")
            try:
                voicelog = file_object.readlines( )
                voice_log = []
                log = []
                for i in range(0,len(voicelog)):       
                    log.append((re.split(";",voicelog[i]))[1])                    
                voice_log = "".join(log)
            finally:
                file_object.close( )   
        except RuntimeError:
            print '测试出现崩溃'
            teskok = False
            #把整行标为红色
            sheet.Rows('%d:%d'%(line,line)).Interior.ColorIndex = 3
            sheet.Rows('%d:%d'%(line,line)).Interior.Pattern = 1
            continue
        #创建动画并插入表格
        sheet.Range('k%d'%line).FormulaR1C1 = voice_log
        sheet.Rows('%d:%d'%(line,line)).RowHeight = 90#为了截图调整行高
        fn = fixture.OutDir + ("route0.png")
        pic = sheet.Pictures().Insert(fn)
        pic.ShapeRange.LockAspectRatio = True
        pic.ShapeRange.Height = 80
        pic.ShapeRange.Width = 140
        pic.ShapeRange.Rotation = 0
        pic.ShapeRange.Left = sheet.Range(col).Left
        pic.ShapeRange.Top = sheet.Range(col).Top
        #pic.Object.ImportMedia(fixture.OutDir.decode('gbk'))
        #建立目录备份测试结果
        TestCaseNo = sheet.Range('B%d'%line).Text
        BackupDir = os.path.join(fixture.OutDir,TestName,TestTime,TestCaseNo)
        os.makedirs(BackupDir)
        for p in os.listdir(fixture.OutDir):
            f = os.path.join( fixture.OutDir, p )
            if os.path.isfile( f ):
                shutil.copyfile(f,os.path.join(BackupDir,p))
                
#fixture.closedevice()

for i in xrange(d1.Sheets.Count,0,-1):
    if d1.Sheets(i) != sheet:
        d1.Sheets(i).Delete()
d1.Windows(1).FreezePanes = False
d1.SaveAs(output)
d1.Close()
excel = None

#输出Excel：
backdir = os.path.join(fixture.OutDir , TestName, TestTime)
try:
    os.makedirs(backdir)
except:
    None
shutil.copyfile(output,os.path.join(backdir , '基础数据应用层测试检查list_RG顺行.xls'))

