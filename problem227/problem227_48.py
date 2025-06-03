n, k = map(int , input().split())
hn = [int(num) for num in input().split()]

hn.sort(reverse = True)
if len(hn) > k:
  print(sum(hn[k:]))
else :
  print(0)