x = int(input())
m = 100
for i in range(1, 10**18):
    m = (m*101)//100
    if m >= x:
        re = i
        break
print(re)