def greeter(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return "Aloha " + result.title()
    return wrapper


def sums_of_str_elements_are_equal(func):
    def wrapper(*args, **kwargs):
        tab = func(*args, **kwargs).split()
        sumx = 0
        sumy = 0
        for x in tab[0]:
            if(x != "-"):
                sumx += int(x)
        if (tab[0][0]=="-"):
            sumx *= -1
        for x in tab[1]:
            if(x != "-"):
                sumy += int(x)
        if (tab[1][0]=="-"):
            sumy *= -1
        
        if (sumx == sumy):
            return str(sumx) + " == " + str(sumy)
        else:
            return str(sumx) + " != " + str(sumy)
    return wrapper


def format_output(*dec):
    def format_output(func):
        def wrapper(*args, **kwargs):
            x = func(*args, **kwargs)
            ret = {}
            for y in dec:
                
                a = y.split("__")
                val = ""
                for z in a:
                    if (list(x.keys()).count(z) <= 0):
                        raise ValueError
                    elif (x[z] == ""):
                        val = 'Empty value '
                    else: 
                        val += x[z] + " "
                val = val[:-1]
                ret[y] = val
            return ret
        return wrapper
    return format_output

from functools import wraps
def add_method_to_instance(klass):
    def decorator(func):
        @wraps(func) 
        def wrapper(self, *args, **kwargs): 
            return func(*args, **kwargs)
        setattr(klass, func.__name__, wrapper)
        
        return func
    return decorator
