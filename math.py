import random #This is importing a library for random num generator
'''
7 types of math operators
+ (addition)
- (subtraction)
* (multiplication)
/ (divide)
% (modulous)
**(power)
//(divide w/o remainder) 
'''
#Examples
num = 23

print('5+3 = ', 5+3)
print('5-3 = ', 5-3)
print('5*3 = ', 5*3)
print('5/3 = ', 5/3)
print('5%3 = ', 5%3)
print('5**3 = ',5**3)
print('5//3 = ',5//3)
print('21+num*2= ',21+num*2) 

Random_num = random.randrange(0,25)
for x in range (0,10):
	Random_num = random.randrange(0,25)
	print(Random_num)	
