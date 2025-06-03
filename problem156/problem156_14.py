def make_divisors(n: int) -> list:
    return_list = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            return_list.append(i)
            if i != n // i:
                return_list.append(n//i)

    return sorted(return_list)

X = int(input())
list = make_divisors(X)
mlist = []
for li in list[::-1]:
    mlist.append(-li)
mlist += list
B = -120
while True:
    for i in mlist:
        if ((B + i) ** 5) - (B ** 5) == X:
            print(B+i,B)
            exit()
    B += 1

