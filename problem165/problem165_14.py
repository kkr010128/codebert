N = int(input())
S = [input() for i in range(N)]

# N = 5
# S = ['aa', 'a', 'aa', 'aaaa', 'aa']

C = dict([s,1] for s in S)
L = len(C)
print(L)