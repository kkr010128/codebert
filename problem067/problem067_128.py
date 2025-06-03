turn = int(input())

taro_score = 0
hanako_score = 0 

for i in range(turn):
    tcard,hcard = input().split()
    tcard = str(tcard)
    hcard = str(hcard)
    taro_card = [0]*len(tcard)
    hanako_card = [0]*len(hcard)
    
    
    for j in range(len(tcard)):
        taro_card[j] = ord(tcard[j])
    
    
    for k in range(len(hcard)):
        hanako_card[k] = ord(hcard[k])
        
    if len(tcard) == len(hcard):
    
        for l in range(len(tcard)):
            if taro_card[l] > hanako_card[l]:
                taro_score += 3
                break
            
            elif taro_card[l] < hanako_card[l]:
                hanako_score += 3
                break   
            
            else:
                if l == len(tcard)-1:
                    taro_score += 1
                    hanako_score += 1
                else:
                    continue
    
    elif len(tcard) < len(hcard):
        
        for a in range(len(tcard)):
            if taro_card[a] > hanako_card[a]:
                taro_score += 3
                break
            
            elif taro_card[a] < hanako_card[a]:
                hanako_score += 3
                break
                
            else:
                if a == len(tcard)-1:
                    #taro_score += 3
                    hanako_score += 3
                    
                else:
                    continue
                    
    else:
            
        for b in range(len(hcard)):
            if taro_card[b] > hanako_card[b]:
                taro_score += 3
                break

            elif taro_card[b] < hanako_card[b]:
                hanako_score += 3
                break

            else:
                if b == len(hcard)-1:
                    #hanako_score += 3
                    taro_score += 3

                else:
                    continue
                              
print("%d %d"%(taro_score,hanako_score))
