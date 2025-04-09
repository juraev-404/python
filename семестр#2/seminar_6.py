import time
from collections import deque
from functools import wraps

def track_calls(func, period=10):
    calls = deque()
    
    @wraps(func)
    def wrapped(*args, **kwargs):
        current_time = time.time()
        while calls and calls[0] < current_time - period:
            calls.popleft()
        
        calls.append(current_time)
        print(f'Функция {func.__name__} вызвана {len(calls)} раз за последние {period} секунд')
        
        return func(*args, **kwargs)
    
    wrapped.call_history = calls  
    return wrapped

import random

@track_calls
def random_function():
    print(f"Случайное число: {random.randint(1, 100)}")

random_function()
random_function()
random_function()
random_function()


# б)

from functools import wraps

def with_defaults(*default_args):
    def decorator(func):
        @wraps(func)
        def wrapper(*args):
            new_args = list(default_args[:len(default_args) - len(args)]) + list(args)
            return func(*new_args)
        return wrapper
    return decorator

default_values = (1, 2, 3)

@with_defaults(*default_values)
def my_function(a, b, c):
    print(f"a={a}, b={b}, c={c}")

my_function()        # a=1, b=2, c=3
my_function(10)      # a=10, b=2, c=3
my_function(10, 20)  # a=10, b=20, c=3
my_function(10, 20, 30)  # a=10, b=20, c=30