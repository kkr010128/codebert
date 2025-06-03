import sys
N = int(input())
array = list(map(int,input().split()))

if not ( 1 <= N <= 100 ): sys.exit()
if not ( 1 <= min(array) and max(array) <= 1000 ): sys.exit()

for I in array:
    if I % 2 == 0 and not ( I % 3 == 0 or I % 5 == 0 ):
        print('DENIED')
        sys.exit()
print('APPROVED')