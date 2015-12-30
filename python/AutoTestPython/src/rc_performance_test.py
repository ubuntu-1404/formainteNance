# coding=gbk
'''
Created on 2011-8-7

@author: Administrator
'''
import win32com.client
import traceback
from navapp import autotest
from navapp import navitool
from testcase.rc import test_calc_performance
import time
import fixture
import os
import shutil

TestName = 'RC性能测试'
localt = time.localtime()
TestTime = '%04d-%02d-%02d-%02d-%02d-%02d'%(localt[0],localt[1],localt[2],localt[3],localt[4],localt[5])

#fixture.connectdevice()

excel = win32com.client.Dispatch("Excel.Application")
excel.DisplayAlerts = False
filename = (fixture.SourceDir + '基础数据应用层测试检查list_block_split.xls').decode('gbk')
output = (fixture.OutDir + '基础数据应用层测试检查list_output.xls').decode('gbk')
d1 = excel.Workbooks.Open(Filename = filename)
sheet = d1.Sheets('RC计算速度_split')
#需要填充的数据列：
cols = ['F','G','H','J','K','L','N','O','P','R','S','T']
for line in range(18,31):
    o = sheet.Range('E%d'%line)
    if(len(o.Text)!=0):
        print('Calculating... ' + o.Text)
        try:
            testok,rlst = test_calc_performance.dotest(start_end=o.Text.encode('utf-8'))
        except:
            print '测试出现崩溃'
            testok = False
            sheet.Rows('%d:%d'%(line,line)).Interior.ColorIndex = 3
            sheet.Rows('%d:%d'%(line,line)).Interior.Pattern = 1
            continue
        #填充Excel
        for i in range(0,12):
            col = (cols[i]+"%d")%line
            sheet.Range(col).FormulaR1C1 = float(rlst[i]['calctime'])/1000 

#fixture.closedevice()

for i in xrange(d1.Sheets.Count,0,-1):
    if d1.Sheets(i) != sheet:
        d1.Sheets(i).Delete()
d1.SaveAs(output)
d1.Close()
excel = None

#输出Excel：
backdir = os.path.join(fixture.OutDir , TestName, TestTime)
try:
    os.makedirs(backdir)
except:
    None
shutil.copyfile(output,os.path.join(backdir , '基础数据应用层测试检查list_output.xls'))


