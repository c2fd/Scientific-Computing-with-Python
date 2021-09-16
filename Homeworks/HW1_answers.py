# Version I
# A number is said to be Disarium if the sum of its digits raised to their respective positions is the number itself.
#Create a function that determines whether a number is a Disarium or not. Note: Please upload your final answer in a .py file.

#Examples
#is_disarium(75) ➞ False
# 7^1 + 5^2 = 7 + 25 = 32
#is_disarium(135) ➞ True
# 1^1 + 3^2 + 5^3 = 1 + 9 + 125 = 135
#is_disarium(544) ➞ False
#is_disarium(518) ➞ True
#is_disarium(466) ➞ False
#is_disarium(8) ➞ True

def is_disarium(n):
	str_n = str(n)
	my_sum = 0.
	for i in range(0, len(str_n)):
		my_sum += int(str_n[i]) ** (i+1)
	return n == my_sum

def is_disarium(n):
	digs = [int(i) for i in str(n)]
	digs_pow = [digs[i]**(i+1) for i in range(len(digs))]
	return n == sum(digs_pow)

def is_disarium(n):
	digs_pow = [ int(value)**(index+1)  for index, value in enumerate(str(n))]
	return n == sum(digs_pow)

import math
def is_disarium(n):
	assert( n > 0)
	len = int(math.log10(n))+1
	my_sum = 0
	index = len
	my_n = n
	while my_n > 0:
		my_sum += (my_n % 10) ** index
		my_n = my_n // 10
		index = index - 1
	return n == my_sum

print(is_disarium((544)))
print(is_disarium((518)))
print(is_disarium((466)))
print(is_disarium((8)))

import time
start = time.time()
print([n for n in range(30000000,40000000) if is_disarium(n)])
print('Time :',time.time()-start)
