#TempConvert.py
TempStr = input ("请输入带符号的温度值:")
if TempStr[0]in ['F','f']:
    C = (eval(TempStr[1:-1])-32)/1.8
    print ("C{:.2f}".format(C))
elif TempStr[0] in['C','c']:
    F=1.8*eval(TempStr[1:-1])+32
    print ("F{:.2f}".format(F))

