def sum_i(N):
    return sum(list(int(i) for i in str(N)))


print("No") if sum_i(input()) % 9 else print("Yes")