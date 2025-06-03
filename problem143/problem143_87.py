#input an interget
k=int(input())
#input an string
str1=str(input())
#get the length of the string
x=int(len(str1))
#initialise y
y=0
#make a second string for the appending
str2="..."

#if statement about how the string will function
#if the string is the same length as k then print it
if x<=k:
    print(str1)
#if not, delete the last character of the string
else:
    while y<k:
        print(str1[y],end=(""))
        y+=1
    print(str2)
