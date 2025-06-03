N = int(input())
S = input()
S1 = set([])
S2 = set([])
S3 = set([])
for i in S:
    for s3 in S2:
        S3.add(s3+i)
    for s2 in S1:
        S2.add(s2+i)
    S1.add(i)
print(len(S3))