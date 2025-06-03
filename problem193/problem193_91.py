H,W,K = map(int,input().split())
S = [[int(i) for i in input()] for l in range(H)]
posibility = set()

for i in range(1<<H-1):
    SW = []
    tmp = S[0]
    counter = 0
    
    for k in range(H-1):
        if i>>k & 1:
            SW.append(tmp)
            tmp = S[k+1]
        else:
            tmp = [tmp[l]+S[k+1][l] for l in range(W)]
    SW.append(tmp)
    counter += len(SW)-1
    max_counter = 0

    for k in range(len(SW)):
        max_counter = max(max(SW[k]),max_counter)
    if max_counter >K:
        continue

    tmp_w = [SW[row][0] for row in range(len(SW))]
    
    for w in range(W-1):
        test = [tmp_w[row]+SW[row][w+1] for row in range(len(SW))]
        if max(test)>K:
            tmp_w = [SW[row][w+1] for row in range(len(SW))]
            counter += 1
        else:
            tmp_w = test

    posibility.add(counter)
print(min(posibility))