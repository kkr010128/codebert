N = int(input())
S_ord = [ord(i) for i in input()]
S_ord_change = []
for i in S_ord:
    i += N
    if i >= 91:
        i = i - 26
    S_ord_change.append(i)

S_change_chr = [chr(i) for i in S_ord_change]
result = ''.join(S_change_chr)
print(result)