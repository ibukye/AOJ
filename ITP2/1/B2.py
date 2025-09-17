from collections import deque
# 通常のlistだと先頭に追加する場合にO(n)のコストだが
# dequeだと先頭、末尾への追加に対してO(1)のコストで実行できる
A=deque()
n=int(input())
for _ in range(n):
    query=input().split()
    if query[0]=="0":
        if query[1]=="0":A.appendleft(int(query[2]))
        else:A.append(int(query[2]))
    elif query[0]=="1":print(A[int(query[1])])
    else:
        if query[1]=="0":A.popleft()
        else:A.pop()