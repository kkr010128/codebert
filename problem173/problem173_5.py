# 1 <= N <= 1000000
N = int(input())

total = []

# N項目までに含まれる->N項目は含まない。だからN項目は+1で外す。
for x in range(1, N+1):
    if x % 15 == 0:
        "FizzBuzz"
    elif x % 5 == 0:
        "Buzz"
    elif x % 3 == 0:
        "Fizz"
    else:
        total.append(x) #リストに加える
print(sum(total))