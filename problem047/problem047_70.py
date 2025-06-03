#coding:utf-8
a,op,b=map(str,input().split())
a,b=int(a),int(b)

while op!="?":
    if op=="+":
        ans=a+b
    elif op=="-":
        ans=a-b
    elif op=="*":
        ans=a*b
    elif op=="/":
        ans=a//b

    print(ans)

    a,op,b=map(str,input().split())
    a,b=int(a),int(b)