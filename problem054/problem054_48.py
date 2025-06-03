p_trump = [a + ' {}'.format(b) for a in ['S', 'H', 'C', 'D'] for b in range(1, 14)]
n = int(input())
trumps = []
for i in range(n):
    trumps.append(input())
for i in p_trump:
    if not i in trumps:
        print(i)

