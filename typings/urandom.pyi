"""
Function:
urandom module provides the tool for random number generation.

Descriptions taken from:
https://python.quectel.com/doc/API_reference/zh/stdlib/urandom.html
"""


def choice(obj: str) -> str:
    """Generates elements in object obj randomly. The type of obj is string.

    :param obj: String type.
    :return: String type. Some random element in obj.
    """

def getrandbits(k: int) -> int:
    """Generates a decimal number in the range of k bits randomly.

    :param: Integer type. Indicates the range.(Unit: bit)
    :return: Integer type. A random decimal number in the range of k bits.
    """

def randint(start: int, end: int) -> int:
    """Generates an integer between start and end.

    :param start: Integer type. The minimum value in the interval.
    :param end: Integer type. The maximum value in the interval.
    :return: Integer type. A random integer between start and end.
    """

def random() -> float:
    """Generates a floating point between 0 and 1.

    :return: Floating point.The floating point between 0 and 1.
    """

def randrange(start, end, step) -> int:
    """Generates a positive integer ascending to step and between start and end randomly.

    :param start: Integer type. The minimum value in the interval.
    :param end: Integer type. The maximum value in the interval.
    :param step: Integer type. The length of ascending.
    :return: Integer type. A random integer between start and end.
    """

def seed(sed:int):
    """Specifies the seed of a random number, generally used in conjunction with other random number generation functions.

    :param sed: Integer type.
    """

def uniform(start, end):
    """Generating A Floating Point Between start And end Randomly

    :param start: Any type of real numbers. The minimum value in the interval.
    :param end: Any type of real numbers. The maximum value in the interval.
    :return: Floating point. A random number between start and end.
    """
