import logging
from functools import wraps
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """
    Декоратор для логирования выполнения функций.
    Записывает в лог информацию о том, успешно ли завершилась функция, или произошла ошибка.

    :param filename: Имя файла для записи логов. Если None, логи выводятся в консоль.
    """
    if filename:
        logging.basicConfig(filename=filename, level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    else:
        logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                logging.info(f"Функция '{func.__name__}' завершилась успешно.")
                return result
            except Exception as e:
                logging.error(f"Функция '{func.__name__}' завершилась с ошибкой: {e}")
                raise

        return wrapper

    return decorator
