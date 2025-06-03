N = int(input())
S = input()

#print(ord("A"))
#print(ord("B"))
#print(ord("Z"))

for i in range(len(S)):
	ascii = ord(S[i]) + N   #Sのi文字目のアスキーコードを計算してしれにNを足してづらす
	if ascii > ord("Z"):    #アスキーコードがよりも大きくなった時はA初まりにづらす
		ascii = ascii - (ord("Z") - ord("A") + 1)
	print(chr(ascii),end = "") #,end = "" は１行ごとに改行しないでプリントする仕組み
