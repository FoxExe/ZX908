"""
Function:
uasyncio is an asynchronous I/O library in MicroPython, also a lightweight subset of asyncio. It provides abstractions similar to coroutines and event loops in the standard library for running multiple coroutines concurrently and managing the execution and suspension of coroutines.
uasyncio , with a small code size and low memory footprint, is suitable for embedded systems and resource–constrained devices. It provides a set of APIs and tools to create and manage coroutines, network and protocol–related classes that support asynchronous I/O.

Descriptions taken from:
https://python.quectel.com/doc/API_reference/en/componentlib/uasyncio.html
"""


class Task(object):

    def cancel(self):
        """Cancels tasks."""


def create_task(coro) -> Task:
    """Creates an asynchronous task to run the given coroutine.

    :param coro:The coroutine object to be run.
    :return:
    """


def run(coro):
    """Runs a coroutine until it completes. This is the main way to start the event loop.

    :param coro:The coroutine object to be run.
    :return:
    """


def sleep(delay):
    """Sleeps for delay seconds. Other tasks can run in the meanwhile.

    :param delay:Integer (or float) type. The time in seconds that the current task or coroutine will block.
    :return:
    """


def sleep_ms(delay):
    """Sleeps for delay milliseconds. Other tasks can run in the meanwhile.

    :param delay:Integer (or float) type. The time in milliseconds that the current task or coroutine will block.
    :return:
    """


def wait_for(coro, timeout):
    """Waits for a coroutine to complete with a timeout in seconds. If the timeout elapses before the task is completed, the task is canceled and an exception will occur.

    :param coro:Coroutine type. The coroutine object.
    :param timeout:Integer (or float) type. The timeout in seconds.
    :return:
    """


def wait_for_ms(coro, timeout):
    """Waits for a coroutine to complete within a timeout in milliseconds. If the timeout elapses before the task is completed, the task is canceled and an exception will occur.

    :param coro:Coroutine type. The coroutine object.
    :param timeout:Integer (or float) type. The timeout in milliseconds.
    :return:
    """


def gather(*coros, return_exceptions=False):
    """Runs the given coroutines and collects the results. When all coroutines are completed, the function returns a result list. If return_exceptions is True, the raised exception will be returned as a result rather than raised immediately.

    :param coros:Coroutine type. Single or multiple coroutine objects.
    :param return_exceptions:Boolean type. Whether to return exceptions as the result.
    :return:
    """
