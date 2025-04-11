"""
Function:
uio contains additional types of stream (file-like) objects and helper functions. This feature implements a subset of the corresponding CPython feature, as described below.
For more information, refer to the original CPython documentation: https://docs.python.org/3.5/library/io.html#module-io.

Descriptions taken from:
https://python.quectel.com/doc/API_reference/zh/stdlib/uio.html
"""


def open(name, mode='r', **kwarg):
    """Opens a file. This is an alias for the built-in open() function.

    :param name: String type. File name.
    :param mode: String type. Open mode.
    Open Mode	Description
    'r'	Open a file for reading.
    'w'	Open a file for writing only. Overwrites the file if the file exists.
    'a'	Opens a file for appending. The file pointer is at the end of the file, so the content is added to the end.
    :param kwargs: Variable-length parameter list.
    :return:uio object – Successful execution
    :raise: OSError - Failed execution
    """
