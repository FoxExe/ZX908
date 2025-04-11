"""
Function:
This class pings IPv4 request packages.
Note: 1. It may occur that the socket cannot be set up at the host address, causing a connection error. 2. Determine the ping period by initializing COUNT and INTERVAL.

Descriptions taken from:
https://python.quectel.com/doc/API_reference/en/networklib/uping.html
"""


def ping(HOST, SOURCE=None, COUNT=4, INTERVAL=1000, SIZE=64, TIMEOUT=5000, quiet=False):
    """Pings packages periodically.

    :param HOST:The IP address to be pinged, such as "baidu.com".
    :param SOURCE:Source IP address, used for binding and with no need for input.
    :param COUNT:Default value: 4. Unit: time.
    :param INTERVAL:Interval. Default value: 1000. Unit: ms.
    :param SIZE:Size of the package read every time. Default value: 64. Unit: byte. No change is required.
    :param TIMEOUT:Timeout. Default value: 5000. Unit: ms.
    :param quiet:False: print and output directly.True: The default value printed by start is converted to an object and returned.Default: false.
    :return:
    """
