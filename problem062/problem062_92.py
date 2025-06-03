while True:
    
    num = int(input())
    
    if num == 0:
        break
    box = []
    while num != 0:
        box.append(num%10)
        num = num//10
        
    print(sum(box))
