# cook your dish here
for _ in range(int(input())):
    x, m = map(int, input().split())
    newNum = ""
    for i in str(x):
        d = int(i)
        newNum += str(d**m % 10)
    revNum = newNum[::-1]
    if int(revNum) % 7 == 0:
        print("yes")
    else:
        print("no")