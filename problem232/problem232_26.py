a,b=map(int,input().split())
s1=str(a)*b
s2=str(b)*a
print(s1 if s2>s1 else s2)