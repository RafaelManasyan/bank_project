def log(filename=""):
    """Декоратор для логирования функций"""

    def wrapper(my_func):
        def inner(*args, **kwargs):
            try:
                my_func(*args, **kwargs)
                if filename:
                    with open(filename, "w") as file:
                        file.write(f"{my_func.__name__}" " ok")
                if not filename:
                    print(f"{my_func.__name__}" " ok")
            except Exception as err:
                if filename:
                    with open(filename, "w") as file:
                        file.write(f"{my_func.__name__} error: {type(err).__name__}. Inputs: {args}, {kwargs}")
                if not filename:
                    print(f"{my_func.__name__} error: {type(err).__name__}. Inputs: {args} {kwargs}")

        return inner

    return wrapper
