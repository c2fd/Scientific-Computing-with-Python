# print all types defined in the `types` module
import types
#print(dir(types))


x = 1.5
print(x, type(x))

x = int(x)
print(x, type(x))

# x = int(-1.5)
# print(x, type(x))

z = complex(x)
print(z, type(z))

x = float(z)
print(x, type(x))

#x = float(z)