"""
Function:
gc module realizes the garbage collection of the memory, and subsets of the corresponding CPython module.
See CPython file gc for more detailed information: https://docs.python.org/3.5/library/gc.html#module-gc

Descriptions taken from:
https://python.quectel.com/doc/API_reference/zh/stdlib/gc.html
"""


def enable():
    """Enables the mechanism for automatic reclaiming memory fragments."""

def disable():
    """Disables the mechanism for automatic reclaiming memory fragments."""

def isenabled():
    """Queries whether the mechanism for automatic reclaiming memory fragments is enabled.

    :return: True-The mechanism for automatic reclaiming memory fragments is enabled;False-The mechanism for automatic reclaiming memory fragments is disabled.
    """

def collect():
    """Reclaims the memory fragments actively."""

def mem_alloc():
    """Queries the applied memory size which has been applied.

    :return: Returns the applied memory size. Unit: byte.
    """

def mem_free():
    """Queries the remaining available memory size.

    :return: Returns the remaining available memory size. Unit: byte.
    """
