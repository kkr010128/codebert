MOD = 1000000007
def fast_power(base, power):
    """
    Returns the result of a^b i.e. a**b
    We assume that a >= 1 and b >= 0

    Remember two things!
     - Divide power by 2 and multiply base to itself (if the power is even)
     - Decrement power by 1 to make it even and then follow the first step
    """

    result = 1
    while power > 0:
        # If power is odd
        if power % 2 == 1:
            result = (result * base) % MOD

        # Divide the power by 2
        power = power // 2
        # Multiply base to itself
        base = (base * base) % MOD

    return result
n,k = [int(j) for j in input().split()]
d = dict()
ans = k
d[k] = 1
sum_so_far = 1
for i in range(k-1, 0, -1):
	d[i] = fast_power(k//(i),n)
	for mul in range(i*2, k+1, i):
		d[i]-=d[mul]
	# d[i] = max(1, d[i])
	ans+=(i*d[i])%MOD
	# if d[i]>1:
		# sum_so_far += d[i]
print(ans%MOD)
