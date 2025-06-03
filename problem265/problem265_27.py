n=int(input())
m=int(n/1.08)
for i in range(-2,3):
    if int((m+i)*1.08)==n:
        print(m+i)
        exit()
print(":(")