"""
Function:
This feature is used for inter-thread communication.

Descriptions taken from:
https://python.quectel.com/doc/API_reference/en/syslib/Queue.html
"""


class Queue(object):

    def __init__(self, max_size=100):
        """
        :param max_size: Integer type. The maximum queue length. Default value: 100.
        """

    def put(self, data=None):
        """Puts data into the queue.

        :param data: Data or signal put into the queue. Optional parameter. If this parameter is omitted, data=None will be configured by default.
        :return: True - Successful execution; False - Failed execution;
        """

    def get(self):
        """Gets data from the queue by blocking the queue.

        :return: Data in the queue.None - The data in the queue is empty.
        """

    def empty(self):
        """Query Whether Queue Is Empty

        :return: True - Empty; False - Not empty
        """

    def size(self):
        """Query Data Length in Queue

        :return: Integer type. The current data length.
        """
