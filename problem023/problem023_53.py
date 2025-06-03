"""
n=int(input())
s=[int(x) for x in input().split()]
q=int(input())
t=[int(x) for x in input().split()]
#print(s)
c=0
for i in t:
    if i in s:
        c+=1
print(c)
"""
"""
n=int(input())
s=[int(x) for x in input().split()]
q=int(input())
t=[int(x) for x in input().split()]
#binary search
a=0
for i in range(q):
    L=0
    R=n-1#探索する方の配列(s)はソート済みでないといけない
    while L<=R:
        M=(L+R)//2
        if s[M]<t[i]:
            L=M+1
        elif s[M]>t[i]:
            R=M-1
        else:
            a+=1
            break
print(a)
"""
#Dictionary
#dict型オブジェクトに対しinを使うとキーの存在確認になる
n=int(input())
d={}
for i in range(n):
    command,words=input().split()
    if command=='find':
        if words in d:
            print('yes')
        else:
            print('no')
    else:
        d[words]=0

