
###########################################################
# Part I
S1 = str('abc')  #single quote & double quote
S2 = str('abc')
print(S1 == S2)
print(S1 is S2)
print(id(S1)) # #How to check the memory location?????
print(id(S1) == id(S2))  # It seems S1 and S2 are the same
print(isinstance(S1,type(S2)))
#print(isinstance(S1,S2)) #syntax error

###########################################################
S1 = str('abc')
S2 = str('abcd')
print(id(S1) == id(S2))



###########################################################
s = "Hello world"
print(type(s))
print(s.find('e'))

print(s.find('o'))
print(s.index('o'))  # built in function for indexes???? Find all the indexes for "o"?
print(s.replace("world", 'John'))
print(s)

substr='l'
index1 = [i for i in range(len(s)) if s.startswith(substr, i)]
index2 = [i for i, ltr in enumerate(s) if ltr == substr]
print('index1',index1)
print('index2',index2)



# length of the string: the number of characters
print(len(s))

# Indexing of string
print(s[::2])  #s[start:end:step]
print(s[::-1])
print(s[::-2])
print(s[0])
print(s[5])
print(s[2:7])
print(s[:])
print(s[:-1])
print(s[:5])
print(s[2:])



# s1 = str('abc');

# print(s1 * 3)
# #print(int(s1[0]))
# #print(int(s1) * 3)
# #print(s1 / 2)


s1 = str('123')
print(int(s1))