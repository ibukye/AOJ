import sys
w = sys.stdin.readline().strip()
cnt = 0
for word in sys.stdin.buffer.read().split():
    if word == b"END_OF_TEXT":break
    if word.decode().lower() == w:cnt+=1
print(cnt)