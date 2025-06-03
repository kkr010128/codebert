"""
Given N, D, A, N means no. of monsters, D means distances of bombs, A attack of the bombs

Find the minimum of bombs required to win.

Each monster out of N pairs - pair[0] = position, pair[1] = health
"""
from collections import deque

mod = 1e9+7
def add(a, b):
    c = a + b
    if c >= mod:
        c -= mod
    return c

def main():
    N, D, A = [int(x) for x in raw_input().split()]
    D *= 2
    monsters = []
    
    for _ in range(N):
        pos, health = [int(x) for x in raw_input().split()]
        monsters.append([pos, health])    
    
    
    monsters.sort(key = lambda x : x[0])
    
    remain_attacks_queue = deque([])
    
    remain_attack = 0
    
    ans = 0
    
    for monster in monsters:
        # monster[0] - pos, monster[1] - health
        # queue[0] - position, queue[1] - attack points
        while len(remain_attacks_queue) and monster[0] - D > remain_attacks_queue[0][0]:
            remain_attack -= remain_attacks_queue.popleft()[1]
        if remain_attack < monster[1]:
            remained_health = monster[1] - remain_attack
            times = remained_health / A if remained_health % A == 0 else remained_health // A + 1
            #print(times)
            attack = times * A
            remain_attacks_queue.append([monster[0], attack])
            ans += times
            remain_attack += attack
        
    print(ans)
    

main()