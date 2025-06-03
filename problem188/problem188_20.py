x, y, a, b, c = map(int, input().split())
list_A = list(map(int, input().split()))
list_B = list(map(int, input().split()))
list_C = list(map(int, input().split()))
list_A.sort(reverse=True)
list_B.sort(reverse=True)
list_C.sort(reverse=True)

list_N = list_A[:x] + list_B[:y] + list_C[:min(c, x + y)]
list_N.sort(reverse=True)
print(sum(list_N[:x+y]))