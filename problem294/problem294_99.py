import bisect

N = int(input())
numbers = [int(i) for i in input().split()]
numbers = sorted(numbers)
counter = 0

for a in range(N):
    for b in range(a+1, N):
        c = bisect.bisect_left(numbers, numbers[a] + numbers[b])
        if c > b:
            counter += c - b -1
        
print(counter)