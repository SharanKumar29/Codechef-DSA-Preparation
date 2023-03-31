import math
t= int(input())
for i in range(t):
   
    h,w,x,y,k=map(int,input().split())
    z=math.sqrt((w-x)**2+(h-y)**2)
    print("1" if z<k else "0")
