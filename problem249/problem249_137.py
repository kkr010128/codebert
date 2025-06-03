a, b, k = map(int, input().split())

x = min(a, k)
a -= x
k -= x
y = min(b, k)
b -= y

print(str(a),str(b))