a, v = map(int, input().split())
b, w = map(int, input().split())
t = int(input())
print('YES' if t*(v-w) >= abs(a-b) else 'NO')
