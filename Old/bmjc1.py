
'''
保密检查文件批量修改程序
要需要修改的文件统一放到一个目录里
要改三个地方的日期和日间
2018-9-11
V1.0
'''
import re
import os, sys

 #文件所在目录  注意把\改成/  目录最后要加/
path="Z:/各科室及个人/电教室/信息化相关工作/保密相关/2018-9-11/"

pattern_1 = '[1-9]\\d*-[0-9]\\d*-[0-9]\\d*'
tihuanwei_1='2018-09-11' #要替换成的日期

pattern_2 = '[1-9]\\d*年[0-9]\\d*月[0-9]\\d*日'
tihuanwei_2='2018年09月11日'  #要替换成的日期

pattern_3 = '\\d{2}:\\d{2}:\\d{2}'
tihuanwei_3='17:36:26'  #要替换成的日间


dirs = os.listdir( path )
# 输出所有文件和文件夹
for file in dirs:
    #改文件内容：
    file=path+file
    #print (file)
    fo=open(file,"r+")
    line=fo.read()
    num = re.sub(pattern_1, tihuanwei_1, line)
    num = re.sub(pattern_2, tihuanwei_2, num)
    num = re.sub(pattern_3, tihuanwei_3, num)
    fo=open(file,"w+")
    fo.write(num)
    fo.close()
    
    #改文件名：
    newfile=re.sub(pattern_2,tihuanwei_2,file)
    os.rename(file,newfile)
    print(newfile)



