
'''
保密检查文件批量修改程序
要需要修改的文件统一放到一个目录里
要改三个地方的日期和日间

2019-11-19 v1.3


2019-09-12 v1.2 
目录名自动改/，文件名中的时间和文本内时间也同步


2018-11-21 V1.1
更新：时间随机生成
'''
import re
import os, sys
import random
 
 #每次执行，改下面两个变量就可以
 #文件所在目录，这里使用win目，最后不加/
# path=r"Z:/各科室及个人/电教室/信息化相关工作/保密相关/2018-11"
path=r"6/"  #要替换的目录  手工改
riqi='2018-06-12' #要替换成的日期   手工改

riqi=riqi.replace("-","年",1)
riqi=riqi.replace("-","月",1)
mytime=riqi+"日"


#把目录中所有/换成\;如果不以/结尾的，再结尾加上/
path=path.replace("\\","/")
if path.endswith('/')==False:
    path=path+"/"
print(path)



pattern_1 = '[1-9]\\d*-[0-9]\\d*-[0-9]\\d*'
tihuanwei_1=riqi #要替换成的日期


pattern_2 = '[1-9]\\d*年[0-9]\\d*月[0-9]\\d*日'
tihuanwei_2=mytime




pattern_3 = '\\d{2}:\\d{2}:\\d{2}'
#后面会随机替换小、分、秒



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
    weijianminshijian = '\d{2}时\d{2}分\d{2}'
    weijianminshijian2=xiaoshi+'时'+fenzhon+'分'+miao
    newfile=re.sub(pattern_2,tihuanwei_2,file)
    newfile=re.sub(weijianminshijian,weijianminshijian2,newfile)
    os.rename(file,newfile)
    print(newfile)



