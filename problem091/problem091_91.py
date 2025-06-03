from itertools import combinations as comb
N = int(input())
L = list(map(int,input().split()))
count = 0
for a, b, c in comb(L, 3):
  if a != b and b != c and c != a and a + b > c and b + c > a and c + a > b:
    count += 1
print(count)