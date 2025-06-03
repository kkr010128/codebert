nn, kk = list(map(int,input().split()))
pp = list(map(int,input().split()))

expectation = [0]*(nn-kk+1)
expectation[0] = sum(pp[0:kk])

for i in range(1,nn-kk+1):
    expectation[i] = expectation[i-1] - pp[i-1] + pp[i+kk-1]

print((max(expectation)+kk)/2)
