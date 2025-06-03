def prime_eratosthenes_edit(n):
    prime_list = []
    num_set = set()
    for i in range(2, 10 ** 6):
        if i not in num_set:
            prime_list.append(i)
            if n <= i:
                return i
            for j in range(i * i, 10 ** 6, i):
                num_set.add(j)


print(prime_eratosthenes_edit(int(input())))