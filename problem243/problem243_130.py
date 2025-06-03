N = int(input())

lst = []

for i in range(N):
   lst.append(input().split())

X = input()

index = 0

for i in range(N):
   if lst[i][0] == X:
      index = i
      break

ans = 0

for i in range(index + 1, N):
   ans += int(lst[i][1])

print(ans)