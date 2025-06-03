x, y, a, b, c = map(int, input().split())
p = [int(i) for i in input().split()]
q = [int(i) for i in input().split()]
r = [int(i) for i in input().split()]

p = list(reversed(sorted(p)))
q = list(reversed(sorted(q)))
r = list(reversed(sorted(r)))
apple = p[:x] + q[:y] + r
apple = list(reversed(sorted(apple)))
print(sum(apple[:x+y]))