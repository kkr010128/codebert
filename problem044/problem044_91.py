ins = input().split()
a = int(ins[0])
b = int(ins[1])
c = int(ins[2])

print(len([x for x in list(range(a, b + 1)) if c % x == 0]))