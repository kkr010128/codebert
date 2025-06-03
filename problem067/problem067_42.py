tarou = 0
hanako = 0
n = int(input())
for i in range(n):
    str1, str2 = input().split()
    if str1 > str2:
        tarou += 3
    elif str1 < str2:
        hanako += 3
    else:
        tarou += 1
        hanako += 1
print("{0} {1}".format(tarou, hanako))