a = int(input())
b = input().split()
c = "APPROVED"
for i in range(a):
    if int(b[i]) % 2 == 0:
        if int(b[i]) % 3 == 0 or int(b[i]) % 5 == 0:
            c = "APPROVED"
        else:
            c = "DENIED"
            break
print(c)