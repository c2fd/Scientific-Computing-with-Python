# def myfunction():
#   pass


#Q: \sum_{i=1}^100 i

def my_sum(k):
  if k == 1:
    return k
  else:
    return k + my_sum(k-1)

my_sum_value = 0;
for i in range(1, 100000001):
  my_sum_value += i
print(my_sum_value)

#print(my_sum(100000001))