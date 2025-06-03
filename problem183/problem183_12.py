def find_divisor(x):
    Divisors = []
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0:
            Divisors.append(i)
            if i != x // i:
                Divisors.append(x // i)
    return Divisors

n = int(input())
ways = len(find_divisor(n-1)) - 1
Div = find_divisor(n)
for i in range(1, len(Div)):
    quo = n
    while quo % Div[i] == 0:
        quo = quo // Div[i]
    if quo % Div[i] == 1:
        ways += 1
print(ways)