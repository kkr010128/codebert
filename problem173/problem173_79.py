ary = list(filter(lambda x: int(x) % 3 != 0 and int(x) % 5 != 0, list(range(int(input()) + 1))))
print(sum(ary))