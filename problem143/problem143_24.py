# Take the input K
# Take the inpus S

#Compare the length of S with K and put in in length
#If length<=K... print all
#If length>K... print some of the character

K = int(input()) # 0(1)
S = input() #0(1)
second_answer = [] #0(1)
x = 0 #0(1)

length = len(S) #0(1)

if length <= K : 
    print(S) #0(1)
else:
    while x<K : #0(K)
        print(S[x], end= (""))
        x += 1
    print("...")