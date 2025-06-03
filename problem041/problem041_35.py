W,H,x,y,r = (int(i) for i in input().split())
answer = "Yes"

if x - r < 0 :
    answer = "No"
elif y - r < 0 :
    answer = "No"
elif x + r > W :
    answer = "No"
elif y + r > H :
    answer = "No"

print(answer)