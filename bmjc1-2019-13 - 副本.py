import turtle
import re
import os, sys,time
import random


# 每次执行，改下面两个变量就可以
# 文件所在目录，这里使用win目，最后不加/
# path=r"Z:/各科室及个人/电教室/信息化相关工作/保密相关/2018-11"
# 要替换的目录  手工改
path = '6/'
# 要替换成的日期   手工改
mytime0 = '2018-06-27'

mytime1 = mytime0.replace("-","年",1)
mytime1 = mytime1.replace("-","月",1)
mytime2 = (mytime1 + '日')

# 把目录中所有/换成\;如果不以/结尾的，再结尾加上/
path = path.replace("\","/")
if (path.endswith('/') == False):
    path = (path + '/')
print(path)

pattern_1 = '[1-9]\\d*-[0-9]\\d*-[0-9]\\d*'
pattern_2 = '[1-9]\\d*年[0-9]\\d*月[0-9]\\d*日'
# 后面会随机替换小、分、秒
pattern_3 = '\\d{2}:\\d{2}:\\d{2}'

dirs = os.listdir( path )
# 输出所有文件和文件夹
for file in dirs:
    # 改文件内容：
    file = (path + file)
    # print (file)
    random.seed()
    # 生成小时
    xiaoshi = str(random.randint(8,11)).zfill(2)
    # 生成分钟
    fenzhon = str(random.randint(1,59)).zfill(2)
    # 生成秒
    miao = str(random.randint(1,59)).zfill(2)
    # 要替换成的日间
    tihuanwei_3 = ((((xiaoshi + ':') + fenzhon) + ':') + miao)
    fo = open(file,"r+")
    line = fo.read()
    num = re.sub(pattern_1, mytime1, line)
    num = re.sub(pattern_2, mytime2, num)
    num = re.sub(pattern_3, tihuanwei_3, num)
    fo = open(file,"w+")
    fo.write(num)
    fo.close()
    # 改文件名：
    weijianminshijian = '\d{2}时\d{2}分\d{2}'
    weijianminshijian2 = ((((xiaoshi + '时') + fenzhon) + '分') + miao)
    newfile = re.sub(pattern_2,mytime2,file)
    newfile = re.sub(weijianminshijian,weijianminshijian2,newfile)
    os.rename(file,newfile)
    print(newfile)
    # 修改文件的  修改时间
    # 修改成如：'2016-12-21 10:22:56'
    timestring = ((mytime0 + ' ') + tihuanwei_3)
    mtime = time.mktime(time.strptime(timestring, '%Y-%m-%d %H:%M:%S'))
    os.utime(newfile,(mtime, mtime))
