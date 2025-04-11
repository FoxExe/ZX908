"""
Function:
The module provides a timer interface for the underlying OS. The OS timer timeout will trigger the bound callback function.

Descriptions taken from:
https://python.quectel.com/doc/API_reference/en/syslib/osTimer.html
"""


class osTimer(object):
    """Creates an OS timer object.

    Compared with machine.Timer, there is no limit on the number of created timers.
    """

    def start(self, initialTime, cyclialEn, callback):
        """Start Timer

        :param initialTime: Integer type. The timeout for the timer. Unit: ms.
        :param cyclialEn: Integer type. Loop or not. 0 - Once. 1 - Loop.
        :param callback: Function type. Callback function triggered when the timer expires. Prototype: callback(arg). arg is not actually used and None can be configured directly.
        :return: Integer type.0 - Successful execution;Other values - Failed execution
        """

    def stop(self):
        """Stops the timer.

        :return: Integer type. 0 - Successful execution;Other values - Failed execution
        """
