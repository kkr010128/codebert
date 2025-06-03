H, W, K = map(int, input().split())
Ss = [list(map(int, input().replace("\n", ""))) for _ in range(H)]

cut_yoko_patterns = ["0","1"]
options = ["0","1"]

import copy

for i in range(H-2):
    cut_yoko_patterns = [cut_yoko_patterns[i] + options[j] for i in range(len(cut_yoko_patterns)) for j in range(len(options))]

answer = int(1e+5)
for cut_yoko_pattern in cut_yoko_patterns:
    yoko_cut_num = cut_yoko_pattern.count("1")
    boxs = [0 for _ in range(yoko_cut_num+1)]
    box_num = [0 for _ in range(H)]
    for i in range(H-1):
        if cut_yoko_pattern[i] == "1":
            box_num[i+1] = box_num[i] + 1
        else:
            box_num[i+1] = box_num[i]
    
    tate_cut_num = 0
    for j in range(W):
        temp_boxs = [0 for _ in range(yoko_cut_num+1)]
        for i in range(H):
            if Ss[i][j] == 1:
                temp_boxs[box_num[i]] += 1
        Impossible = False
        Should_cut = False
        for i in range(yoko_cut_num+1):
            if temp_boxs[i] > K:
                Impossible = True
            
            elif boxs[i] + temp_boxs[i] > K:
                Should_cut = True
        
        if Impossible == True:
            break
        elif Should_cut ==True:
            boxs = copy.deepcopy(temp_boxs)
            tate_cut_num += 1
        else:
            for i in range(yoko_cut_num+1):
                boxs[i] += temp_boxs[i]
    else:
        
        if tate_cut_num+yoko_cut_num < answer:
            answer = tate_cut_num + yoko_cut_num
print(answer)