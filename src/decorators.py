import functools
import logging
import sys
from typing import Callable, Any


def log() -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """Декоратор для логирования выполнения функций."""
    logger = logging.getLogger("FunctionLogger")
    logger.setLevel(logging.INFO)
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(logging.Formatter("%(message)s"))
        logger.addHandler(handler)

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                logger.info(f"{func.__name__} ok")
                return result
            except Exception as e:
                logger.error(f"{func.__name__} error: {e.__class__.__name__}")
                raise

        return wrapper

    return decorator
