# def func1(s):
#     '''
#     Print a string 's' and tell how many characters it has    
#     '''
    
#     print(s + " has " + str(len(s)) + " characters")


# help(func1)


def square(x):
    """
    Return the square of x.
    """
    return x ** 2, x**3, x**4

ans = square(2)
print(ans)

ans1, ans2, ans3 = square(2)
print(ans1,ans2,ans3)


def super_add(x, y):
    return x + y

print(super_add(3,4))

print(super_add("abc", 'def'))
print(super_add(str(3), "abc"))
#print(super_add((3, "abc"))