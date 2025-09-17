L=[]
cursor=0 # ENDを指す
n=int(input())
for _ in range(n):
    query=input().split()
    if query[0]=="0":L.insert(cursor,int(query[1]));cursor+=1
    elif query[0]=="1":cursor+=int(query[1])
    else:
        L.pop(cursor-1)
        if cursor>len(L):cursor=len(L)
for i in range(len(L)):
    print(L[i])