# [箱A, 箱B, 箱C]
list = input().split()
 
# 箱Aと箱B入れ替え
list[0], list[1] = list[1], list[0]
 
# 箱Aと箱C入れ替え
list[0], list[2] = list[2], list[0]    
              
print(' '.join(list))