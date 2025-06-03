import sys
array = list(map(int,input().split()))
if not ( 1 <= min(array) and max(array) <= 100 ): sys.exit()
check = lambda x: isinstance(x,int)

print(array[2],array[0],array[1])