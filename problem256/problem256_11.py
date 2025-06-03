import fractions as math
input_line = list(map(int,input().split(' ')))

ans = input_line[0] * input_line[1] // math.gcd(input_line[0], input_line[1])
print(ans)
