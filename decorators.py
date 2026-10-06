def debug(func):
    def wrapper(*args, **kwargs):
        arg_values = ", ".join(str(arg) for arg in args) if args else "0"
        kwarg_values = ", ".join(f"{k}={v}" for k, v in kwargs.items()) if kwargs else "0"
        func_name = func.__name__
        return f"Calling Function: ({func_name}) with args: {arg_values} and with kwargs: {kwarg_values}"
        # return func(*args,**kwargs)
    return wrapper


@debug
def greet(greeting="hi", name="abc"):
    print(f"{greeting}, {name} good things are coming soon")

@debug
def key_val(**kwargs):
    kwarg_list=[]
    for key, val in kwargs.items():
        kwarg_list.append(f"{key},{val}")
    return kwarg_list    
        
# print(greet("hello", "abdul wahab"))
# print(key_val(name="abdul wahab",age=26))

import time
def timer(func):
    def wrapper(*args,**kwargs):
        start_time=time.time()
        result=func(*args,**kwargs)
        end_time=time.time()
        print(f"function name: {func.__name__} ran in time {end_time-start_time}")
        return result
        
    return wrapper

@timer
def addition(a,b,tim):
    time.sleep(tim)
    return a + b

# print(addition(90000000000000000000,45,3))

def addition_cache(func):
    cache_dict={}
    print(cache_dict)
    def wrapper(*args,**kwargs):
        if args in cache_dict:
            return (f"this time cached result: {cache_dict[args]}")
        result=func(*args,**kwargs)
        cache_dict[args]=result        
        return result        
    return wrapper

@addition_cache
def long_func(a,b,tim):
    time.sleep(tim)
    return a+b

print(long_func(33,45,2))
print(long_func(33,45,2))

