numbers = map(long, raw_input().split())

d = numbers[0] / numbers[1]
r = numbers[0] % numbers[1]
f = float(numbers[0]) / float(numbers[1])

print d, r, ('%.9f' % f)