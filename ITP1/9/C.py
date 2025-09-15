n = int(input())
taro_score, hanako_score = 0, 0
for _ in range(n):
    taro, hanako = input().split()
    if taro>hanako:taro_score+=3
    elif hanako>taro:hanako_score+=3
    else:taro_score+=1;hanako_score+=1
print(f"{taro_score} {hanako_score}")