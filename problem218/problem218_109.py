from collections import Counter
N = int(input())
C = Counter([input() for _ in range(N)])
# print(f'{list(C)=}')

max_value = max([value for value in C.values()])
# print(f'{max_value=}')

S = [key for key, value in zip(C.keys(), C.values()) if value == max_value]
# print(f'{S=}')

for s in sorted(S):
    print(s)
