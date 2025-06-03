import sys

input()
numbers = map(int, input().split())
evens = [number for number in numbers if number % 2 == 0]

if len(evens) == 0:
    print('APPROVED')
    sys.exit()
    
for even in evens:
    if even % 3 != 0 and even % 5 != 0:
        print('DENIED')
        sys.exit()

print('APPROVED')
