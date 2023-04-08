x = int(input())
#1. x%2, add to string. then subtract modulus, then divide by 2. repeat until division gives 0. convertedString - output as int 
convertedString = str()
while x!=0:
  convertedString = str(int(x%2)) + convertedString
  x = int((x-x%2)/2)
print(convertedString)
