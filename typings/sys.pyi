"""
Function:
System Related Features.

Descriptions taken from:
https://python.quectel.com/doc/API_reference/zh/stdlib/sys.html
"""


argv: list = ...  # The list of variable parameters of enabling the current program.
byteorder: str = ...  # Byte order (‘little’ - little-endian, ‘big’ - big-endian).

# Returns the current version information of MicroPython. MicroPython has the following attributes:
# 对于MicroPython，它具有以下属性：
#   name: Character string“ micropython”
#   version: Tuple (major, minor, micro), such as (1, 7, 0)
#   _mpy: The version information of mpy file. The parse method is below. mpy_cross needs to adapt to this version information when generating mpy.
implementation: object = ...

# The maximum value of QuecPython module integers which can retain on the current platform.
# If it is less than the maximum value in the platform, it is the maximum value represented by the MicroPython integer (this is the case for MicroPython ports that do not support the long integer).
maxsize: int = ...

modules: dict = ...  # Returns the imported modules in the current Python in dictionary form.
platform: str = ...  # MicroPython Operation Platform.
stdin = ...  # Standard Input (Default: USB virtual serial port. Other serial ports are optional).
stdout = ...  # Standard Output (Default: USB virtual serial port. Other serial ports are optional).
version: str = ...  # String type. MicroPython version.
version_info: tuple = ...  # Integer tuple type. MicroPython version.

def exit(retval: int = 0):
    """Exits the current program with the given parameters.

    :param retval: Integer type. Exiting parameter.
    :raise: This function triggers a SystemExit exit. If a parameter is given, its value is assigned as a parameter to SystemExit.
    """

def print_exception(exc, file=stdout):
    """Prints the exception information to the file object.

    The generated file is sys.stdout by default, which is the standard output of the exception information.

    :param exc: Exception object.
    :param file: The specified output file. The generated file is sys.stdout by default.
    """
