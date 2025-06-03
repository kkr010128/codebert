text=input()
n=int(input())
for i in range(n):
    order=input().split()
    a,b=map(int,order[1:3])
    if order[0]=="print":
        print(text[a:b+1])
    elif order[0]=="reverse":
        re_text=text[a:b+1]
        text=text[:a]+re_text[::-1]+text[b+1:]
    else :
        text=text[:a]+order[3]+text[b+1:]
        
