a=input()
b=int(input())
while b>0:
    tmp=input().split(" ")
    if tmp[0]=="replace":
        a=a[:int(tmp[1])]+tmp[3]+a[int(tmp[2])+1:]
    if tmp[0]=="reverse":
        tmp2="".join(list(a)[int(tmp[1]):int(tmp[2])+1])[::-1]
        a=a[:int(tmp[1])]+tmp2+a[int(tmp[2])+1:]
    if tmp[0]=="print":
        print(a[int(tmp[1]):int(tmp[2])+1])
    b-=1
