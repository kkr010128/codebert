def have_ABC_string(n, str):
    count = 0
    for i in range(n-2):
        if str[i] == 'A' and str[i+1] == 'B' and str[i+2] == 'C':
            count += 1
    return count

N = int(input())
S = input()
result = have_ABC_string(N, S)
print(result)