import logging
from io import StringIO

import pytest

from src.decorators import log


@log()
def successful_function(x, y):
    return x + y


@log()
def error_function(x, y):
    return x / y


def capture_logs(func, *args, **kwargs):
    log_stream = StringIO()
    logger = logging.getLogger("FunctionLogger")
    handler = logging.StreamHandler(log_stream)
    logger.addHandler(handler)
    try:
        result = func(*args, **kwargs)
    finally:
        logger.removeHandler(handler)
    return result, log_stream.getvalue()


def test_successful_function():
    result, captured = capture_logs(successful_function, 1, 2)
    assert result == 3
    assert "successful_function ok"


def test_error_function():
    with pytest.raises(ZeroDivisionError):
        capture_logs(error_function, 1, 0)
