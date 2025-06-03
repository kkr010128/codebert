n=int(input())
s=input()

score = 0

for p in range(1000):
    
    pw = str(p).zfill(3)
    
    start = 0
    n_match = 0
    
    for j in range(3):
        for i in range(start, len(s)):
            
            if s[i] == pw[j]:
                start = i+1
                n_match = n_match+1
                
                if j == 3-1:
                    # print(pw)
                    score = score+1
                
                break
        if n_match <= j:
            break
            
print(score)