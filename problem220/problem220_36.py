s, t = map(str, input().split())
a, b = map(int, input().split())
u = input()
st = {}
st[s] = a
st[t] = b
st[u] -= 1
print('{} {}'.format(st[s], st[t]))