#TempConvert.py
TempStr = input ("请输入带符号的温度值:")
F=1.8*eval(TempStr[0:-1])+32
print ("转后是{:.2f}F".format(F))
