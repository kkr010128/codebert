dice = ['23542', '14631', '12651', '15621', '13641', '24532']

d = input().split()
q = int(input())

for _ in range(q):
    num = input().split()
    order = str(d.index(num[0]) + 1) + str(d.index(num[1]) + 1)
    [print(d[i]) for i in range(6) if order in dice[i]]
