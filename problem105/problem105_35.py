N = int(input())
ai = list(map(int,input().split()))
counter = 0
for a in ai[::2]:
  if a%2==1:
    counter += 1
print(counter)