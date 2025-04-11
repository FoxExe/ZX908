"""
Function:
Math module provides mathematical operation functions, and realizes subsets of the corresponding CPython module.
See CPython file math for more detailed information: https://docs.python.org/3.5/library/math.html#module-math

Descriptions taken from:
https://python.quectel.com/doc/API_reference/zh/stdlib/math.html
"""

def pow(x, y):
    """Returns x to the yth power.

    :param x: Any type of real numbers.
    :param y: Any type of real numbers.
    :return: Floating point. x to the yth power.
    """

def acos(x):
    """Returns the arccosine radian value of x.

    :param x: Any type of real numbers that range from -1 to 1, including -1 and 1. If it is smaller than -1 or larger than 1, the error will be generated.
    :return: Floating point. The arccosine radian value of x.
    """

def asin(x):
    """Returns the arcsine radian value of x.

    :param x: Any type of real numbers that range from -1 to 1, including -1 and 1. If it is less than -1 or greater than 1, the error will be generated.
    :return: Floating point. The arcsine radian value of x.
    """

def atan(x):
    """Returns the arctangent radian value of x.

    :x: Any type of real numbers.
    :return: Floating point. The arctangent radian value of x.
    """

def atan2(x, y):
    """Returns the arctangent value of the given X and Y coordinate values.

    :param x: Any type of real numbers.
    :param y:Any type of real numbers.
    :return: Floating point. The arctangent value of the coordinate (x ,y).
    """

def ceil(x):
    """Returns the integer of a number obtained by rounding up.

    :param x: Any type of real numbers.
    :return: Integer type. x: The minimum integer which is greater than or equal to the input parameter.
    """

def copysign(x, y):
    """Puts the plus or minus symbol of y in front of x.

    :param x: Any type of real numbers.
    :param y: Any type of real numbers.
    :return: Floating point. The value after putting the plus or minus symbol of y in front of x.
    """

def cos(x):
    """Returns the cosine value of the x radian.

    :param x: Any type of real numbers.
    :return: Floating point. The cosine value of the x radian which ranges from -1 to 1.
    """

def degrees(x):
    """Converts the radian to the angle.

    :param x: Any type of real numbers.
    :return: Floating point. The angle which is converted by radian x.
    """

e: float = ...  # The mathematical constant e is a natural constant.

def exp(x):
    """Returns e to the xth power.

    :param x: Any type of real numbers.
    :return: Return Value Floating point. e to the xth power.
    """

def fabs(x):
    """Returns the absolute value of a number.

    :param x: Any type of real numbers.
    :return: Floating point. The absolute value of x.
    """

def floor(x):
    """Returns the integer of a number obtained by rounding down.

    :param x: Any type of real numbers.
    :return: Integer type. x: The maximum integer which is less than or equal to the input parameter.
    """

def fmod(x, y):
    """Returns the remainder of x/y.

    :param x: Any type of real numbers.
    :param y: Any type of real numbers.
    :return: Floating point. The remainder of x/y.
    """

def modf(x):
    """Returns a tuple consisting of the decimal and integer parts of x.

    :param x: Any type of real numbers.
    :return: Floating point. The remainder of x/y.
    """

def frexp(x):
    """Returns a tuple (m,e).

    :param x: Floating point.
    :return:Returns a tuple (m,e) , and returns the mantissa and exponent of x in the form of (m,e) .
    m is a floating point, e is an integer, and x == m * 2**e. If x is 0, (0.0, 0) will be returned, otherwise 0.5 <= abs(m) < 1 will be returned.
    """

def isfinite(x):
    """Determines whether x is a finite number.

    :param x: Any type of real numbers.
    :return: Determines whether x is a finite number. If x is a finite number, True will be returned, otherwise False will be returned.
    """

def isinf(x):
    """Determines whether x is an infinity number or a minus infinity number.

    :param x: Any type of real numbers.
    :return: If x is an infinity number or a minus infinity number, True will be returned, otherwise False will be returned.
    """

def isnan(x):
    """Determines whether x is not a number (NaN).

    :param x: Any type of real numbers.
    :return: If x is not a number, True will be returned, otherwise False will be returned.
    """

def ldexp(x, exp):
    """Returns the value of x*(2^i)

    :param x: Any type of real numbers.
    :return: Floating point. The value of x(2*i).
    """

def log(x):
    """Returns the natural logarithm of x.

    :param x: Any type of real numbers. If it is less than 0, the error will be reported.
    :return: Floating point. The natural logarithm of x.
    """

pi: float = ...  # Mathematical constant pi (Pi, which is generally expressed as π).

def radians(x):
    """Converts the angle to the radian.

    :param x: Any type of real numbers.
    :return: Floating point. The radian which is converted by the angle x.
    """

def sin(x):
    """Returns the sine value of x radian.

    :param x: Any type of real numbers.
    :return: Returns the sine value of x radian which ranges from -1 to 1.
    """

def sqrt(x):
    """Returns the square root of x.

    :param x: Any type of real numbers.
    :return: Floating point. The square root of x.
    """

def tan(x):
    """Returns the tangent value of x radian.

    :param x: Any type of real numbers.
    :return: Floating point. The tangent value of x radian which ranges from -1 to 1.
    """

def trunc(x):
    """Returns the integer part of x.

    :param x: Any type of real numbers.
    :return: Integer type. The integer part of x.
    """
