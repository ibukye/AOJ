n = int(input())                    
a=list(map(int, input().split()))   # [1, 2, 3, 4, 5]
a.reverse()
print(" ".join(map(str, a)))

