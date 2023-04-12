# cook your dish here
for _ in range(int(input())):
    s = input()
    n = len(s)
    c =0
    t = 0
    for i in range(n):
        if s[i]=="0":
            c+=1
        elif s[i]=="7" and c>=2:
            t = t+(int((c*(c-1))/2))
    print(t)   
