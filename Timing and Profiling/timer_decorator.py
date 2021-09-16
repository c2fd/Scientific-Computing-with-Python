import time
import numpy as np

## decorator
def my_timer(my_func):
    def wrapper(*args, **kwargs):
        start = time.time()
        my_return = my_func(*args, **kwargs)
        end = time.time()
        return my_return, end - start
    return wrapper

@my_timer
def sum_func(my_array):
    my_sum = my_array[0]
    for i in range(1, len(my_array)):
        my_sum += my_array[i]
    return my_sum

len_list = []
time_list = []

for i in range(1, 21):
    len_ = i * 100
    my_array = np.random.rand(len_)
    _, time_ = sum_func(my_array)
    len_list.append(len_)
    time_list.append(time_)

import matplotlib.pyplot as plt
plt.plot(len_list, time_list,'o')
plt.show()