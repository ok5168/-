import os
path=input('�������ļ�·��(��β����/)��')       

#��ȡ��Ŀ¼�������ļ��������б���
f=os.listdir(path)
print(f)


n=0
for i in f:
    
    #���þ��ļ���������·��+�ļ�����
    oldname=path+f[n]
    
    #�������ļ���
    newname=path+'a'+str(n+1)+'.JPG'
    
    #��osģ���е�rename�������ļ�����
    os.rename(oldname,newname)
    print(oldname,'======>',newname)
    
    n+=1
