"""
Function:
The module realizes the conversion between binary data and various ASCII encoding (bidirectional), and subsets of the corresponding CPython module.
See CPython file binascii for more detailed information: https://docs.python.org/3.5/library/binascii.html#module-binascii

Descriptions taken from:
https://python.quectel.com/doc/API_reference/zh/stdlib/ubinascii.html
"""


def a2b_base64(data: str):
    """This function decodes the data encoded by base64.

    When decoding, invalid characters inputed by base64 will be ignored, and the bytes object will be returned.
    """

def b2a_base64(data: bytes):
    """Encodes binary data in base64 format and returns encoded data.

    The encoded data followed by a line break is represented as the bytes object.
    """

def hexlify(data: bytes, sep: str = ''):
    """Converts the binary data to the hexadecimal character string."""


def unhexlify(data: str):
    """Converts the hexadecimal character string to the binary character string."""
