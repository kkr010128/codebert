num_limit = int(input())
num_list = [0] * num_limit
j_limit = int(num_limit ** 0.5)
for j in range(1,j_limit+1):
    for k in range(1,j + 1):
        if num_limit < j**2 + k**2 + j*k:
            break
        for l in range(1,k+1):
            if num_limit < j**2 + k**2 + l**2 + j*k + k*l + l*j:
                break
            elif num_limit >= j**2 + k**2 + l**2 + j*k + k*l + l*j:
                if j > k:
                    if k > l:
                        num_list[j**2 + k**2 + l**2 + j*k + k*l + l*j-1] += 6
                    else:
                        num_list[j**2 + k**2 + l**2 + j*k + k*l + l*j-1] += 3
                elif k > l:
                    num_list[j**2 + k**2 + l**2 + j*k + k*l + l*j-1] += 3
                else:
                    num_list[j**2 + k**2 + l**2 + j*k + k*l + l*j-1] += 1
for i in num_list:
    print(i)