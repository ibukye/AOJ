W,H,x,y,r=map(int,input().split())
if y+r<=H and y-r>=0 and x+r<=W and x-r>=0:print("Yes")
else:print("No")