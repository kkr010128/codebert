import sys
n = int(input())
for i in range(1, 46300):
    if n*25/27 <= i < (n+1)*25/27:
        print(i)
        sys.exit()
print(":(")