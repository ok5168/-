TempStr = input ()
if TempStr[:3]in ['RMB','rmb']:
    C = eval(TempStr[3:])*6.78
    print ("USD{:.2f}".format(C))
elif TempStr[:3] in['USD','usd']:
    F=eval(TempStr[3:])/6.78
    print ("RMB{:.2f}".format(F))
