n = int(input())
nums = []
for i in range(3, n + 1):
  if i % 3 == 0 or i % 10 == 3 or '3' in str(i):
      #print('',i,end='')
      nums.append(i)
for i in nums:
    print('',i,end='')
print()