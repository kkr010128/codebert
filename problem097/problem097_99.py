k = int(input())

def test_case(k):
    ans,cnt = 7,1
    
    if k % 2 == 0 or k % 5 == 0:
        return -1
    
    if k == 1 or k == 7:
        return 1
    
    while (1):
        ans = (ans * 10 + 7) % k
        cnt += 1
        
        if ans == 0:
            return cnt
        
print(test_case(k))

