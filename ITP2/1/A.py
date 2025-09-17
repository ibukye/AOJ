A=[]
q=int(input())
for _ in range(q):
    query=input().split()   # 要素をリストに
    if query[0]=="0":A.append(int(query[1]))
    elif query[0]=="1":print(A[int(query[1])])
    else:A.pop()