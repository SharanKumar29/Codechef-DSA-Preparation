t=int(input())
while(t>0):
    K,N=map(int, input().split())
    oneMod=twoMod=zeroMod=0
    if(K%3==0):
        oneMod=twoMod=zeroMod=int(K/3)
    else:
        extra = K%3
        oneMod=twoMod=zeroMod=int((K-extra)/3)
        if(extra == 1):
            oneMod+=1
        else:
            oneMod+=1
            twoMod+=1
    
    if(N<=oneMod):
        print((N-1)*3+1)
    elif(N<=twoMod+oneMod):
        print(((N-oneMod)-1)*3+2)
    else:
        print((N-(oneMod+twoMod))*3)
    t-=1