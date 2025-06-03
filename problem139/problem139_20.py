H1, M1, H2, M2, K = map(int, input().split())

H1 *= 60
H2 *= 60

start = H1 + M1
end = H2 + M2

time = end - start
ans = time - K

print(ans)