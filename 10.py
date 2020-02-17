1、在movies文件夹下面的所有文件前面都加上[可可可可]

 6
7
#coding:utf-8
import os
movie_name = os.listdir('./movies')
for temp in movie_name:
    new_name = '[可可可可]' + temp
 
    os.rename('./movies/'+temp,'movies/'+new_name)