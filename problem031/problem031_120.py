import math
while True:
    n = input()
    if(n == 0):
        break
    s = map(int, raw_input().split())
    average = 0.0
    for i in s:
        average += i
    average /= len(s)
    alpha_pow = 0.0
    for i in range(len(s)):
        alpha_pow += (s[i] - average) * (s[i] - average)
    alpha_pow /= n
    print(math.sqrt(alpha_pow))