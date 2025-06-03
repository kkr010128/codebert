
N = int(input())
As = list(map(int, input().split()))
ans = 0

tall = int(As[0])

for A in As:
	if(tall > A):
		ans += tall - A
	else:
		tall = A

print(ans)