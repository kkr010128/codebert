# coding:utf-8

W=input()
W=W.lower()

ct=0
while True:
    S=map(str,input().split())

    for i in S:
        if i=="END_OF_TEXT":
            print(ct)
            exit(0)
        elif i.lower()==W:
            ct=ct+1