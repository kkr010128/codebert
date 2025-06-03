def f(i):
    if i == 2:return 1
    return pow(2, i-1, i) == 1
print(sum(1 for n in range(int(input())) if f(int(input()))))