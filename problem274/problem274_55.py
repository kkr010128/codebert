def main():
	n, m = map(int, input().split())
	rev = input()[::-1]
	ans = []
	cur = nxt = 0
	while cur < n:
		for i in range(cur + 1, cur + m + 1):
			if i==n:
				nxt = i
				break
			if rev[i]=="0":
				nxt = i
		if cur==nxt:
			print(-1)
			exit()
		ans += [str(nxt - cur)]
		cur = nxt
	print(" ".join(ans[::-1]))


if __name__=="__main__":
	main()
