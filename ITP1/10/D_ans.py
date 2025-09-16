"""
NumPyでvector演算
"""
import numpy as np

x = np.array(list(map(int, input().split())))
y = np.array(list(map(int, input().split())))
diff_abs = np.abs(x - y)

for p in range(1, 4):
    print(np.sum(diff_abs ** p) ** (1/p))
print(np.max(diff_abs))

"""
純Python
"""
def min_distance(diff_abs, p):
    return sum(d**p for d in diff_abs) ** (1/p)

def chef_distance(diff_abs):
    return max(diff_abs)

n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
diff_abs = [abs(xi - yi) for xi, yi in zip(x, y)]

for p in range(1, 4):
    print(min_distance(diff_abs, p))
print(chef_distance(diff_abs))