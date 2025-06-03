(N,) = [int(x) for x in input().split()]
brackets = [input() for i in range(N)]

delta = []
minDelta = []
for s in brackets:
    balance = 0
    mn = 0
    for c in s:
        if c == "(":
            balance += 1
        else:
            balance -= 1
        mn = min(mn, balance)
    delta.append(balance)
    minDelta.append(mn)

if sum(delta) == 0:
    # Want to get balance as high as possible
    # Take any positive as long there's enough balance to absorb their minDelta
    # Can sort since anything that works will only increase balance and the ones with worse minDelta comes later
    posIndices = [i for i in range(N) if delta[i] > 0]
    posIndices.sort(key=lambda i: minDelta[i], reverse=True)

    # At the top can take all with zero delta, just need to absorb minDelta
    eqIndices = [i for i in range(N) if delta[i] == 0]

    # When going back down, want to preserve existing balance as much as possible but take a hit for stuff that does need to use the balance to absorb minDelta
    negIndices = [i for i in range(N) if delta[i] < 0]
    negIndices.sort(key=lambda i: delta[i] - minDelta[i], reverse=True)

    balance = 0
    for i in posIndices + eqIndices + negIndices:
        if balance + minDelta[i] < 0 or balance + delta[i] < 0:
            print("No")
            exit()
        balance += delta[i]
    assert balance == 0

    print("Yes")
else:
    print("No")
