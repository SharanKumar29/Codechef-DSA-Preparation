t= int(input())
for i in range(t):
    x=int(input())
    n=0
    while n==0:
        a=str(x+1)
        if len(set(str(a))) == len(str(a)):
            print(a)
            n=1
        else: 
            x+=1
        
    
    
