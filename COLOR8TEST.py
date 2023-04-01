t= int(input())
for i in range(t):
    n,x1,x2,x3,x4,x5,x6=map(int,input().split())
    a=(x1+x2+x3+x4+x5+x6)*((n+1)//2)
    print(a)
    
