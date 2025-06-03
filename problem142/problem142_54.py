import sys
N = input()
array_hon = [2,4,5,7,9]
array_pon = [0,1,6,8]
array_bon = [3]

if not ( int(N) <= 999 ): sys.exit()

if int(N[-1]) in array_hon: print('hon')
if int(N[-1]) in array_pon: print('pon')
if int(N[-1]) in array_bon: print('bon')
