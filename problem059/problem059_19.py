RC = input().split()
r = int(RC[0])
c = int(RC[1])
A_c_sum =[]
final_sum = 0
for j in range(c):
    A_c_sum.append(0)
for i in range(r):
    A_r = input().split()
    A_r_sum = 0
    for j in range(c):
        A_c_sum[j] += int(A_r[j])
        print(A_r[j]+" ", end="")
        A_r_sum += int(A_r[j])
    print(A_r_sum)
    final_sum += A_r_sum
print(" ".join(map(str,A_c_sum))+" ",end="")
print(final_sum)