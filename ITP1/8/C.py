import sys
alpha='abcdefghijklmnopqrstuvwxyz'
cnt=[0 for _ in alpha]

text=sys.stdin.read().lower()
"""
while True:
    str=input().lower()
    if str=="":break
    for i in range(len(str)):
        for j in range(len(alpha)):
            if alpha[j] == str[i]:
                cnt[j]+=1

Traceback (most recent call last): 
File "/home/judge/onlinejudge/judge2.0/rep/code.py", line 5, 
in str=input().lower() 
EOFError: EOF when reading a line Command exited with non-zero status 1 
0.00user 
0.00system 
0:00.00elapsed 
85%CPU (0avgtext+0avgdata 8020maxresident)k 
0inputs+8outputs (0major+886minor)pagefaults 
0swaps
"""
for character in text:
    if character in alpha:
        cnt[alpha.index(character)]+=1

for i in range(len(alpha)):
    print(f"{alpha[i]} : {cnt[i]}")

