S = list(input())
A = [0]*(len(S)+1)

node_value = 0
for i in range(len(S)):
    if S[i] == "<":
        node_value += 1
        A[i+1] = node_value
    else:
        node_value = 0

node_value = 0
for i in range(len(S)-1,-1,-1):
    if S[i] == ">":
        node_value += 1
        A[i] = max(A[i], node_value)
    else:
        node_value = 0

print(sum(A))