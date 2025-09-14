"""
4棟
1フロア10部屋
3階建て
"""
all_buildings = [[[0] * 10 for _ in range(3)] for _ in range(4)]

n = int(input())
for _ in range(n):
    b, f, r, v = map(int, input().split())  # b棟f階r番にv人
    all_buildings[b-1][f-1][r-1] += v

for i in range(4):
    for j in range(3):
        #print(all_buildings[i][j])     # [0, 0, 8, 0, 0, 0, 0, 0, 0, 0]
        print("", " ".join(map(str, all_buildings[i][j])))
    if i != 3: print("#"*20)