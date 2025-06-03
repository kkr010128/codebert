N = input()

sum_n = 0
for n in N:
    num = int(n)
    sum_n += num

if(sum_n % 9 == 0):
    print("Yes")
else:
    print("No")
