
'''
保密检查文件批量修改程序
要需要修改的文件统一放到一个目录里
要改三个地方的日期和日间


2018-11-21更新：时间随机生成
V1.1
'''
import re
import os, sys
import random
 #文件所在目录  注意把\改成/  目录最后要加/
path="Z:/各科室及个人/电教室/信息化相关工作/保密相关/2018-11/"

pattern_1 = '[1-9]\\d*-[0-9]\\d*-[0-9]\\d*'
tihuanwei_1='2018-11-09' #要替换成的日期

pattern_2 = '[1-9]\\d*年[0-9]\\d*月[0-9]\\d*日'
tihuanwei_2='2018年11月09日'  #要替换成的日期

pattern_3 = '\\d{2}:\\d{2}:\\d{2}'
#tihuanwei_3='10:25:17'  #要替换成的日间，会全部一样的时间


dirs = os.listdir( path )
# 输出所有文件和文件夹
for file in dirs:

    #改文件内容：
    file=path+file
    #print (file)

    random.seed()
    xiaoshi=str(random.randint(8,11)).zfill(2) #生成小时
    fenzhon=str(random.randint(1,59)).zfill(2) #生成分钟
    miao=str(random.randint(1,59)).zfill(2) #生成秒
    tihuanwei_3=xiaoshi +':'+fenzhon+':'+miao  #要替换成的日间 

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



