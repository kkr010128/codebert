str1 = str(input())

if len(str1) != 6 :
     print('No')

if str1[2] == str1[3] and str1[4] == str1[5] :
     print('Yes')
else :
    print('No')  