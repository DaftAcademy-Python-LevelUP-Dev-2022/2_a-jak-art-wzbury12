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


def format_output(*required_keys):
    pass


def add_method_to_instance(klass):
    pass
