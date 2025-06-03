N = int(input())
S_ord = [ord(i) for i in input()]
S_ord_change = [65 + (i + N - 65) % 26 for i in S_ord]
S_change = [chr(i) for i in S_ord_change]
result = ''.join(S_change)
print(result)