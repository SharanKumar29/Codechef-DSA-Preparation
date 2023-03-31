t= int(input())
for i in range(t):
    a= int(input())
    P = 0
    while a % 2 == 0:
        a = a// 2
        P += 1
    print("1" if P % 2 == 0 else "0")
    
