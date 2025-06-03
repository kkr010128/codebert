N,*a = map(int,open(0).read().split())
max_num = a[0]
count = 0
for i in a:
  if max_num>=i:
    count+=1
  max_num = min(i,max_num)
print(count)