a,b,c = map(int, input().split())
print(len(list(filter(lambda x: c%x==0,range(a,b+1)))))
