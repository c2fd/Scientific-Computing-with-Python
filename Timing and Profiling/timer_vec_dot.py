import time
import numpy as np

## O(n)
def sum_func(my_array):
    my_sum = my_array[0]
    for i in range(1, len(my_array)):
        my_sum += my_array[i]
    return my_sum

len_list = []
time_list = []

for i in range(1, 21):
    len_ = i * 1000
    my_array = np.random.rand(len_)
    start = time.time()
    sum_func(my_array)
    end = time.time()
    len_list.append(len_)
    time_list.append(end - start)

import matplotlib.pyplot as plt
plt.plot(len_list, time_list,'o')
plt.show()
