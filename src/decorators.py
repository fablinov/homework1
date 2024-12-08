from functools import wraps
from time import time
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """Декоратор для логирования функции, аргументов, результатов и ошибок"""

    def decorator(func: Any) -> Any:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"{func.__name__} ok\n")
                else:
                    print(f"{func.__name__} ok")
                return result
            except Exception as error:
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"{func.__name__} error: {error.__class__.__name__}. Inputs: {args}, {kwargs}\n")
                else:
                    print(f"{func.__name__} error: {error.__class__.__name__}. Inputs: {args}, {kwargs}")

        return wrapper

    return decorator


def printing(func: Any) -> Any:
    def wrapper(*args: Any, **kwargs: Any)-> Any:
        print(f'Function {func} started')
        result = func(*args, **kwargs)
        print(f'Function {func} finished')
        return result
    return wrapper


def timer(func: Any) -> Any:
    def wrapper(*args: Any, **kwargs: Any)-> Any:
        time_1 = time()
        result = func(*args, **kwargs)
        time_2 = time()
        print(f'Time for work: {time_2 - time_1}')
        return result
    return wrapper


@printing
@timer
def my_function() -> None:
    for i in range(100000000):
        continue


my_function()