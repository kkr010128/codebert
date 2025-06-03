import itertools
N, M, Q = map(int, input().split())
a = []
b = []
c = []
d = []
for q in range(Q):
    aq, bq, cq, dq = map(int, input().split())
    a.append(aq)
    b.append(bq)
    c.append(cq)
    d.append(dq)

max_answer = 0
for A in itertools.combinations_with_replacement(range(1, M + 1), N):
    # print(A)
    answer = 0
    for i in range(Q):
        # print(a[i], b[i], c[i], d[i])
        if A[b[i]-1] - A[a[i]-1] == c[i]:
            answer += d[i]
    # print(answer)
    if max_answer < answer:
        max_answer = answer
print(max_answer)