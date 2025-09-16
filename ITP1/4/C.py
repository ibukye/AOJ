while 1:
    x,op,y=input().split()
    if op=="?":break
    if op=="+":print(int(x)+int(y))
    elif op=="-":print(int(x)-int(y))
    elif op=="*":print(int(x)*int(y))
    else:print(int(x)//int(y))