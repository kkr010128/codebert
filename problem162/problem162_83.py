N, M = map(int, input().split())

odd_head, odd_tail = 1, 0
even_head, even_tail = 0, 0

if M & 1:
    odd_tail = M + 1
    even_head = M + 2
    even_tail = M + 2 + M - 1
else:
    odd_tail = 1 + (M - 1)
    even_head = M + 1
    even_tail = M + 1 + M

while odd_tail - odd_head > 0:
    print(odd_head, odd_tail)
    odd_head += 1
    odd_tail -= 1

while even_tail - even_head > 0:
    print(even_head, even_tail)
    even_head += 1
    even_tail -= 1