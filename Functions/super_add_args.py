def super_add(*args):
	
	my_sum = args[0]
	for i in range(1,len(args)):
		my_sum += args[i]
	return my_sum


def super_add_2(*args):
	my_sum = 0 #args[0]
	for i in range(0,len(args)):
		my_sum += args[i]
	return my_sum


print(super_add(1,2))
print(super_add(1,2,3))
print(super_add(1,2,3,4))
print(super_add('a','b','c'))
#print(super_add_2('a','b','c'))
# print(super_add())

print(super_add([1],[1,2],[1,2,3]))