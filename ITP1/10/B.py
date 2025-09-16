import sys
import math
#a,b,c_angle=sys.stdin.read().split()
a,b,c_angle=map(float, input().split())
a=int(a)
b=int(b)
c_angle=int(c_angle)
S=0.5*a*b*math.sin(c_angle*math.pi/180)
c=(a**2+b**2-2*a*b*math.cos(math.radians(c_angle)))**0.5
L=a+b+c
a_2=a**2
b_2=b**2
c_2=c**2
#h=(4*a_2*c - b_2**2 - a_2**2 - c_2**2 + 2*(a_2*b_2 + b_2*c_2 + c_2*a_2)) / (4*a_2)
h = (2*S)/a
print(S)
print(L)
print(h)