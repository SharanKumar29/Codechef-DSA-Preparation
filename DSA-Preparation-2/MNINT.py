# cook your dish here
n= int(input())
for iter1 in range(n):
    x = int(input())
    ans = 1
    i = 2

    while(x>=i*i):
        c = 0
        while(x%i==0):
            x /=i
            c +=1
        if c>0:
            ans *= i
        i +=1

    if x>=2:
        ans *=x

    print(int(ans))
                