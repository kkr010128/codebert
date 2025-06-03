N = int(input())

lst = input().split()

count = 0

for i in range(N):
   if (i + 1) % 2 == 1 and int(lst[i]) % 2 == 1:
      count += 1

print(count)