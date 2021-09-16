# Elements in a list do not all have
# to be of the same type:
l = [1, 'a', 1.0, 1-1j]
print(l)
print(l[0])
print(type(l))

# in python 3 range generates an iterator, which can be converted to a list using 'list(...)'.
# It has no effect in python 2
print( list(range(1, 10, 1)) )
print( list(range(-10, 10)) )

#for i in range(1,10,1):

start = 10
stop = 30
step = 2

print(type(range(start, stop, step)))
