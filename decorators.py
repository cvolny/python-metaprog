#!/usr/bin/python3

#pylint: disable=C0111,C0103

from functools import lru_cache, wraps
import logging
import time

DEBUG = False
LOGLEVEL = logging.DEBUG if DEBUG else logging.WARNING
LOGFORMAT = '[%(asctime)s] %(fname)s(%(fargs)s): %(message)s'

def timed(name=None):
    '''timing logger function decorator.'''
    def decorate(func):
        if not DEBUG:
            return func
        logger = logging.getLogger(name if name else func.__module__)

        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            logger.debug('{0:f}s'.format(end-start),
                extra={'fname':func.__name__,
                    'fargs':','.join([str(arg) for arg in args])})
            return result
        return wrapper
    return decorate

@lru_cache(maxsize=50)
@timed()
def fib(n):
    '''Calculate Fibonacci number to n-th position.'''
    if n in (0, 1):
        return n
    return fib(n-1) + fib(n-2)

if __name__ == "__main__":
    logging.basicConfig(format=LOGFORMAT, datefmt="%H:%M:%S")
    logging.getLogger(__name__).setLevel(LOGLEVEL)
    for x in [5, 10, 15, 20, 25, 30]:
        print("{0:d}: {1:d}".format(x, fib(x)))
