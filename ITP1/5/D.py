n=int(input())
for i in range(1,n+1):
    x=i
    if x%3==0:print(x);continue
    if x%10==3:print(x);x/=10;x-=1
    
