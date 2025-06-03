def main():
  import sys
  input=sys.stdin.buffer.readline
  h,w=map(int,input().split())
  b,q=b'.'*w,range(w)
  for i in range(h):
    s=input()
    a=[]
    a_add=a.append
    for x,y,z,c in zip(b,b'.'+s,s,q):
      if x==46>z:c+=1
      if y==46>z:i+=1
      if i>c:i=c
      a_add(i)
    b,q=s,a
  print(i)
main()
