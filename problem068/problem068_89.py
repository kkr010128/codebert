#coding: utf-8
#itp1_9d

def rev(s,a,b):
 b=b+1
 t=s[a:b]
 u=t[::-1]
 x=s[:a]
 y=s[b:]
 return x+u+y

def rep(s,a,b,w):
 b=b+1
 x=s[:a]
 y=s[b:]
 return x+w+y

s=raw_input()
n=int(raw_input())
for i in xrange(n):
 d=raw_input().split()
 a=int(d[1])
 b=int(d[2])
 if d[0]=="print":
  print s[a:b+1]
 elif d[0]=="reverse":
  s=rev(s,a,b)
 elif d[0]=="replace":
  w=d[3]
  s=rep(s,a,b,w)