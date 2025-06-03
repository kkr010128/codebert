N = int(input())

ACcount = 0 
WAcount = 0
TLEcount = 0
REcount = 0
for i in range(N):
	S=input()

	if S == "AC":
		ACcount = ACcount + 1
	elif S == "WA":
		WAcount = WAcount + 1
	elif S == "TLE":
		TLEcount = TLEcount + 1
	elif S == "RE":
		REcount = REcount + 1

print("AC x", ACcount)
print("WA x", WAcount)
print("TLE x", TLEcount)
print("RE x", REcount)
