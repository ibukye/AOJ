import sys
x1,y1,x2,y2=sys.stdin.read().split()
x_diff=float(x2)-float(x1)
y_diff=float(y2)-float(y1)
distance=(x_diff**2+y_diff**2)**0.5
print(distance)