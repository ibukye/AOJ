import sys
w = input().strip()
cnt = 0
for word in sys.stdin.read().split():
    if word == "END_OF_TEXT":break
    if word.lower() == w:cnt+=1
print(cnt)