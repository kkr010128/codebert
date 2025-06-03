n = int(input())
s = str(input())

n = n-2
count = 0
for i in range(n):

    if s[i]+s[i+1]+s[i+2] == "ABC":
        count = count+1

print(count)
