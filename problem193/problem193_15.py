h,w,K = map(int,input().split())
sij = [input() for j in range(h)]

num = 2**(h-1)
hon = 10**18

for i in range(num):
    tmp = format(i,'0'+str(h)+'b')
    #print(tmp,tmp,tmp,tmp)
    yoko_hon = sum(list(map(int,tmp)))+1
    blk = [0]*(yoko_hon)
    #blk_num = 0
    tmp_col = 0
    tmp_hon = yoko_hon-1
    flag = True
    ok_flag = True
    for j in range(w):
        tmp_blk = [0]*(yoko_hon)
        blk_num = 0
        for k in range(h):
            if tmp[k] == str(1):
                blk_num += 1
            #print(blk_num,tmp_blk)
            tmp_blk[blk_num] += int(sij[k][j])
            #print(blk[blk_num] , tmp_blk[blk_num],k)
            if blk[blk_num] + tmp_blk[blk_num] > K:
                flag = False
                continue
        
        #print(ok_flag,flag,tmp_blk,blk)
        if flag == False:
            for l in range(yoko_hon):
                if tmp_blk[l] > K:
                    ok_flag = False
                    break
                blk[l] = tmp_blk[l]
            tmp_hon += 1
            tmp_col = 0
            flag = True
        else:
            for l in range(yoko_hon):
                blk[l] += tmp_blk[l]
                tmp_col += 1
        if ok_flag == False:
            break
            
    #print(ok_flag)
    if ok_flag == False:
        ok_flag = True
        continue
    #exit()
    hon = min(tmp_hon,hon)
    
print(hon)