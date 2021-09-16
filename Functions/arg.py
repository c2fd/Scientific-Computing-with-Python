def myfunc(x, p=2, debug=False):
    if debug:
        print("evaluating myfunc for x = " + str(x) + " using exponent p = " + str(p))
    return x**p

# print(myfunc(x=2))
# print(myfunc(x=2,p=3))
# print(myfunc(x=2, debug=True, p=3))
# print(myfunc(debug=True, p = 3, x=2))

print(myfunc(x=2, p=2,debug = False))