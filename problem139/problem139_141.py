H1, H2, H3, H4, K = map(int, input().split())
up = H1*60 + H2
down = H3*60 + H4
print(down - up - K)