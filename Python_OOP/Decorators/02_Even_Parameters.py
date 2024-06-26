def even_parameters(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, int):
                if arg % 2 == 0:
                    continue

            return "Please use only even numbers!"

        return func(*args)

    return wrapper


@even_parameters
def add(a, b, c):
    return a + b + c


print(add(2, 2, 4))
