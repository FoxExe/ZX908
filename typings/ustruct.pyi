"""
Function:
Module feature: ustruct module realizes subsets of the corresponding CPython module.
See CPython file struct for detailed information: https://docs.python.org/3.5/library/struct.html#module-struct

Descriptions taken from:
https://python.quectel.com/doc/API_reference/zh/stdlib/ustruct.html

The format string is the mechanism used to specify the expected layout when packing and unpacking data.
Format strings are built through the format character of the specified data type that to be packed or unpacked.
In addition, there are special characters that control byte order, size, and alignment.

Byte Order, Size, and Alignment
By default, C types are represented in the machine's native format and byte order, and properly aligned by skipping pad bytes if necessary (according to the rules used by the C compiler).
According to the following table, the first character of the format string can be used to indicate the byte order, size, and alignment of the packed data:
+---------------+---------------+-----------+-------------------------------+
|   Character   |   Byte order  |           |       Size    |   Alignment   |
+===============+===============+===========+===============+===============+
|       @       |   native                  |   native      |   native      |
|       =       |   native                  |   standard    |   none        |
|       <       |   little-endian           |   standard    |   none        |
|       >       |   big-endian              |   standard    |   none        |
|       !       |   network (= big-endian)  |   standard    |   none        |
+---------------+---------------------------+---------------+---------------+
If the first character is not one of the format string, it is assumed to be '@' .

List of Format Character:
+-----------+-------------------+---------------+-------------------+
|   Format  |   C Type          |   Python type |   Standard size   |
+===========+===================+===============+===================+
|   b       |   signed char     |   integer     |       1           |
|   B       |   unsigned char   |   integer     |       1           |
|   h       |   short           |   integer     |       2           |
|   H       |   unsigned short  |   integer     |       2           |
|   i       |   int             |   integer     |       4           |
|   I       |   unsigned int    |   integer     |       4           |
|   l       |   long            |   integer     |       4           |
|   L       |   unsigned long   |   integer     |       4           |
|   q       |   long long       |   integer     |       8           |
|   Q       |   unsigned long   |   long        |       8           |
|   f       |   float           |   float       |       4           |
|   d       |   double          |   float       |       8           |
|   P       |   void *          |   integer     |       4           |
+-----------+-------------------+---------------+-------------------+
"""


def calcsize(fmt):
    """Returns the number of bytes for storing fmt.

    :param fmt: Format character type. See the list of format character above for details.
    """

def pack(fmt, *args):
    """Compresses parameters v1, v2, ... according to the format string fmt.

    :param fmt: Format character type. See the list of format character above for details.
    :param args: The variable name or value which requires data conversion.
    :return: Returns the byte object of the encoded parameter.
    """

def unpack(fmt, data):
    """Decompresses the data according to the format string fmt . The return value is a tuple.

    :param fmt: Format character type. See the list of format character above for details.
    :param data: Data needs to be decompressed.
    :return: Returns the tuple containing the decompression value (even if it contains only one value).
    """

def pack_into(fmt, buffer, offset, *args):
    """Packs values args into a buffer starting with offset according to the format string fmt.

    If you counts from the end of the buffer, the value of offset may be negative.

    :param fmt: Format character type. See the list of format character above for details.
    :param buffer: Buffer for writing data.
    :param offset: Starting position for writing data.
    :param args: Data needs to be written in the buffer.
    """

def unpack_from(fmt, data, offset=0):
    """Parses the decompressed data starting from offset according to the format string fmt.

    If you counts from the end of the buffer, the value of offset may be negative.

    :param fmt: Format character type. See the list of format character above for details.
    :param data: Data buffer. (The unit of the buffer size is byte.)
    :param offset: (Optional) Starting position of decompression. 0 is by default.
    :return: Returns the tuple containing the decompression value (even if it contains only one value).
    """
