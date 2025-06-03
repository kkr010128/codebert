def isPrimeNum(in_num):
    if in_num <= 1:
        return False
    elif in_num == 2:
        return True
    elif in_num % 2 == 0:
        return False
    else:
        if pow(2, in_num-1, in_num) == 1:
            return True
        else:
            return False


num_len = int(input())
cnt = 0
for i in range(num_len):
    num = int(input())
    if isPrimeNum(num)==True:
        cnt = cnt + 1

print(str(cnt))