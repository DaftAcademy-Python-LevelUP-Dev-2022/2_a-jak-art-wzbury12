def greeter(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return "Aloha " + result.title()
    return wrapper


def sums_of_str_elements_are_equal(func):
    pass


def format_output(*required_keys):
    pass


def add_method_to_instance(klass):
    pass
