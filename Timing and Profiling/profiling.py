
import numpy as np
import cProfile


def outer_loop_func():
    np.random.rand(100, 100)

def inner_loop_func():
    pass

def test_func():
    for i in range(1000):
        outer_loop_func()
        for j in range(1000):
            inner_loop_func()


cProfile.run('test_func()')