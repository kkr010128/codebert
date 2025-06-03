n=int(input())
hoge=[]
for i in range(n):
  hoge.append(input())
huga=list(set(hoge))
print(len(huga))