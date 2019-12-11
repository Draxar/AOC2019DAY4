# BRUTE FORCE blah...
minPass = 245182
maxPass = 790572
passNum = 0
passwords = []
def checkNumber(num):
  n = [int(x) for x in str(num)] 
  if n[0]>n[1] or n[1]>n[2] or n[2]>n[3] or n[3]>n[4] or n[4]>n[5]:
    return False
  if n[0]!=n[1] and n[1]!=n[2] and n[2]!=n[3] and n[3]!=n[4] and n[4]!=n[5]:
    return False
  return True

number = minPass
while number <= maxPass:
  if checkNumber(number):
    passwords.append(number)
    passNum += 1
  number += 1

print(passNum)

