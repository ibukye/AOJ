import sys
cnt=0
w=input()
str=list(sys.stdin.read().lower().split())
for i in range(len(str)):
    if str[i]=="END_OF_TEXT":break
    if str[i]==w:cnt+=1
print(cnt)