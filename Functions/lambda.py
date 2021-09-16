f1 = lambda x: x**2
print(f1(2)) 
# is equivalent to 

def f2(x):
    return x**2
print(f2(2))
    
f3 = lambda x, y: x+ y
print(f3(1,2))


##
def myfunc(a):
  return lambda x : x * a

func1 = myfunc(2)  # 2*x
func2 = myfunc(3)  # 3*x
print(func1(11))
print(func2(11))

# It is equivalent to

def myfunc_outer(a):
  def myfunc_inner(x):
    return x * a
  return myfunc_inner


func1_new = myfunc_outer(2)
func2_new = myfunc_outer(3)
print(func1_new(11))
print(func2_new(11))