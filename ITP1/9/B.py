

while True:
    str=input()
    if str=="-":break
    cnt=int(input())
    ope=0
    for _ in range(cnt):
        ope+=int(input())
    ope%=len(str)
    take=str[0:ope]
    str=str[ope:]
    str+=take
    print(str)

"""
1+2+1=4
ope=4%len(str)

先頭からn文字とって後ろにつける

"""
