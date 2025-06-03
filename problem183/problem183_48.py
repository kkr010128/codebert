#約数全列挙
def make_divisors(n):
	divisors = []
	for i in range(1, int(n**0.5)+1):
		if n % i == 0:
			divisors.append(i)
			if i != n // i:
				divisors.append(n//i)
	return divisors


n=int(input())
#n%k!=0
cnt=len(make_divisors(n-1))-1

#n%k==0
lst=make_divisors(n)
for k in lst:
	if k!=1:
		t=n
		while t%k==0:
			t//=k
		if (t-1)%k==0:
			cnt+=1
print(cnt)