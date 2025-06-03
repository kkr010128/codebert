input()
n = input()
count = 0
for i in range(2, len(n)):
   # print(n[i-2] + n[i-1] + n[i])
    if (n[i-2] + n[i-1] + n[i]) == 'ABC':
            count += 1
print(count)
