input()
l = [int(i) for i in input().split()]
print(" ".join(map(str,l[::-1])))