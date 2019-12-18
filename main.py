# BRUTE FORCE blah...
# 976 too high
minPass = 245182
maxPass = 790572
passNum = 0


def checkNumber(num):
	n = [int(x) for x in str(num)]
	if n[0] > n[1] or n[1] > n[2] or n[2] > n[3] or n[3] > n[4] or n[4] > n[5]:
		return False
	if ( 
  not (n[0] == n[1] and n[0] != n[2]) and 
  not (n[1] == n[2] and n[1] != n[0] and n[1] != n[3]) and 
  not (n[2] == n[3] and n[2] != n[1] and n[2] != n[4]) and 
  not (n[3] == n[4] and n[3] != n[2] and n[3] != n[5]) and 
  not (n[4] == n[5] and n[4] != n[3])) :
		return False
	return True


number = minPass
while number <= maxPass:
	if checkNumber(number):
		passNum += 1
	number += 1

print(passNum)
