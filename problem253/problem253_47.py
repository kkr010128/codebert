s = list(map(int, input().split()))
N = s[0]
A = s[1]
B = s[2]

if (B - A) % 2 == 0:
  print((B - A) // 2)
else:
  print(min(A - 1,N - B) +  1 + (B - A - 1) // 2)