# coding=gbk
'''
Created on 2011-9-1

@author: Administrator
'''

import win32com.client
import traceback
from navapp import autotest
from navapp import navitool
from testcase.poi import test_poi_correctness
import time
import fixture
import re
import os
import shutil

TestName = 'POI搜索'
localt = time.localtime()
TestTime = '%04d-%02d-%02d-%02d-%02d-%02d'%(localt[0],localt[1],localt[2],localt[3],localt[4],localt[5])

#fixture.connectdevice()

excel = win32com.client.Dispatch("Excel.Application")
excel.DisplayAlerts = False
filename = (fixture.SourceDir + '基础数据应用层测试检查list_14Q4.xls').decode('gbk')
output = (fixture.OutDir + '基础数据应用层测试检查list_output.xls').decode('gbk')
d1 = excel.Workbooks.Open(Filename = filename)
sheet = d1.Sheets('poi搜索')
#为了截图调整列宽
#sheet.Columns('J:J').ColumnWidth = 24

for line in range(6743,6744):
    find_type1 = sheet.Range('c%d'%line).Text
    distri = sheet.Range('e%d'%line).Text
    input_type1 = sheet.Range('f%d'%line).Text
    input_name1 = sheet.Range('G%d'%line).Text.encode('gbk')
    
    if(len(find_type1)!=0) and len(distri)!=0:
        print('Calculating... ' + input_name1)
        try:
            testok = test_poi_correctness.dotest(find_type = find_type1, districtccode = distri, input_name = input_name1, input_type = input_type1)
            print(testok)
            sheet.Range('H%d'%line).FormulaR1C1 = testok
        except RuntimeError:
            print '测试出现崩溃'
            teskok = False
            #把整行标为红色
            sheet.Rows('%d:%d'%(line,line)).Interior.ColorIndex = 3
            sheet.Rows('%d:%d'%(line,line)).Interior.Pattern = 1
            continue
        
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
shutil.copyfile(output,os.path.join(backdir , '基础数据应用层测试检查list_POI.xls'))      