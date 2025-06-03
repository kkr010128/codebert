I=raw_input()
O=str()
list_upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#list_lower="abcdefghijklmnopqrstuvwxyz"
for i in I:
	if i in list_upper:
		O+=i.lower()
	else:
		O+=i.upper()
print O