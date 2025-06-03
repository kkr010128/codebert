A,B = map(int,input().split())

for n in range(10000):
  if int(0.08*n)==A and int(0.10*n)==B:
    print(n)
    exit()

print(-1)