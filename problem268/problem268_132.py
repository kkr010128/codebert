# similar to problem if n person are arranged in a row and have 3 different hats to wear
# no of ways of wearing hats so that every adjacent person wears different hats
# so ith person cannot wear more than 3 no of different ways
mod = 10**9+7
def main():
	ans =1
	n = int(input())
	arr = list(map(int , input().split()))
	col=[0 for i in range(0 , 6)]
	for i in range(0 , n):
		cnt , cur =0 , -1
		if arr[i]==col[0]:
			cnt = cnt+1
			cur = 0
		if arr[i]==col[1]:
			cnt = cnt+1
			cur = 1
		if arr[i]==col[2]:
			cnt = cnt+1
			cur = 2
		if cur ==-1:
			print(0)
			exit()
		col[cur]=col[cur]+1
		ans = (ans*cnt)%mod
		ans = ans%mod
	print(ans)

if __name__ =="__main__":
	main()