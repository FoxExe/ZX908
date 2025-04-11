"""
Function:
The module provides a bare flash area and a dedicated read/write interface for you to store important information, which won't be lost after the firmware burning.
(If you burn the firmware that does not provide the secure data area, it cannot be ensured that information won't be lost.)
Besides, the module also provides a storage and read interface but deletion interface is not provided.

Descriptions taken from:
https://python.quectel.com/doc/API_reference/en/syslib/securedata.html
"""


def Store(index, databuf, len):
    """Data Storage

    Store the one with the shorter data length between databuf and len.

    :param index: Integer type.
    Index Serial Number	Maximum Storage
    1 - 8	52 bytes
    9 - 12	100 bytes
    13 - 14	500 bytes
    15 - 16	1000 bytes
    :param databuf: Bytearray type. A data array to be stored.
    :param len: Integer type. The length of data to be written.
    :return: -1: Parameter error.; 0: Normal execution.
    """


def Read(index, databuf, len):
    """Data Reading

    If the stored data is not larger than the input parameter len, the actual stored data length is returned.

    :param index: Integer type. Index range: 1-16; Index number of the data to be read.
    :param databuf: Bytearray type. Store the read data.
    :param len: Integer type. Length of data to be read.
    :return: -2: Both storage and backup data do not exist.-1: Parameter error.Other values: Length of data actually read.
    """
