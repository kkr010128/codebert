def move(up,bottom,right,left,front,back,direction):
    if direction == "N":
        return (front,back,right,left,bottom,up)
    elif direction == "S":
        return (back,front,right,left,up,bottom)
    elif direction == "E":
        return (left,right,up,bottom,front,back)
    elif direction == "W":
        return (right,left,bottom,up,front,back)
    
up,front,right,left,back,bottom = input().split()
direction = list(input())

for i in range(len(direction)):
    up,bottom,right,left,front,back = move(up,bottom,right,left,front,back,direction[i])
    
print(up)