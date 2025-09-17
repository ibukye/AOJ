# TIME LIMIT EXCEEDED
A=[]
n=int(input())
for _ in range(n):
    query=input().split()
    if query[0]=="0":
        if query[1]=="0":A.insert(0,int(query[2]))
        else:A.append(int(query[2]))
    elif query[0]=="1":print(A[int(query[1])])
    else:
        if query[1]=="0":A.pop(0)
        else:A.pop()