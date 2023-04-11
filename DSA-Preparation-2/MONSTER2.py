# cook your dish here
import math
t=int(input())
for i in range(t):
    a,b,x,y=map(int,input().split())
    f=0
    if y<x:
        a=math.ceil(a/(x-y))
        if b-y*a>0:
            f=1
    print(f)
        
    