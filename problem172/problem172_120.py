import sys

N = input()

for i in range ( len ( N )):
    if '7' == N[i] :
        print("Yes")
        sys.exit()
print("No")