box_A,box_B,box_C = map(int,input().split())

box_A,box_B = box_B,box_A
box_A,box_C = box_C,box_A
 
print(box_A,box_B,box_C)