#  not resolved
n_ori =int(input())
n_dif = n_ori - 1
sq_ori = int(n_ori**.5)
sq_dif = int(n_dif**.5)
divisor_ori = []
divisor_dif = []

for i in range(1, sq_ori+1):
	if n_ori % i == 0:
		divisor_ori.append(i)
		if i != n_ori // i:
			divisor_ori.append(n_ori//i)

for i in range(1, sq_dif+1):
	if n_dif % i == 0:
		divisor_dif.append(i)
		if i != n_dif // i:
			divisor_dif.append(n_dif//i)
			
cnt = 0
for k in divisor_ori:
	if k == 1:
		continue
	else:
		tmp = n_ori
		while tmp % k == 0:
			tmp = tmp//k

		if tmp % k == 1:
			cnt += 1

print(cnt + len(divisor_dif) - 1)



# # num = n - 1
# # sq = int(num**.5)
# # if sq == 1:

# # for k in range(2, sq+1):
# # 	if k == sq and num % k == 0:
# # 		cnt += 1
# # 	elif num % k == 0:
# # 		cnt += 2
# # cnt += 1

# # sq2 = int(n ** .5)
# # for k in range(2, sq2+1):
# # 	x = n
# # 	if x % k == 0:
# # 		while x % k == 0:
# # 			x = x//k
# # 		if x % k == 1:
# # 			cnt += 1

# # cnt += 1

# # print(cnt)



