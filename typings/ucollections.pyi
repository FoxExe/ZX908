"""
Function:
Module features: ucollections module can create a container type that saves various objects.
This module realizes subsets of the corresponding CPython module.
See CPython file collections for more detailed information: https://docs.python.org/3/library/collections.html

Descriptions taken from:
https://python.quectel.com/doc/API_reference/zh/stdlib/ucollections.html
"""


def namedtuple(name: str, fields: tuple):
    """Creates a namedtuple container type with a specific name and a set of fields.

    namedtuple is a subclass of the tuple that allows its fields to be accessed by index.

    :param name: String type. Type name of the new container.
    :param fields: Tuple type. The new container type contains fields of the subtype.
    """

class deque(object):
    """Creates a bidirectional queue for deque."""

    def __init__(self, iterable: tuple, maxlen: int, flag: int = 0):
        """
        :param iterable: Tuple type. It must be an empty tuple.
        :param maxlen: Integer type. Specifies maxlen and limits the bidirectional queue to its maximum length.
        :param flag: Integer type. Optional parameter.
        0 (default): Not check whether the queue overflows.If the queue continues to increase when it reaches the maximum length, the previous value will be discarded.
        1: When the queue reaches the maximum specified length, IndexError: full will be displayed.
        """

    def append(self, data):
        """Inserts values into the queue.

        :param data: Basic data type. Values need to be added to the queue.
        """

    def popleft(self):
        """Removes the data on the left side of deque and returns the removed data. If deque is empty, it will lead to an index error.

        :return: Returns the popped value.
        """
