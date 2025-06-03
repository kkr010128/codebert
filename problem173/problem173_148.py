total = 0

n = int(input())
for i in range(1, n + 1):
    if not ((i % 5 == 0) or (i % 3 == 0)):
        total = total + i
        
print(total)
