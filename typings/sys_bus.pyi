"""
Function:
This feature subscribes to messages and publishes one-to-many broadcasts with multithreading, similar to an internal MQTT protocol.

Descriptions taken from:
https://python.quectel.com/doc/API_reference/en/syslib/sys_bus.html
"""


def subscribe(topic, handler):
    """

    :param topic: String or integer type. The topic to be subscribed to.
    :param handler: Function type. Event handler function. This function will be called to handle the subscribed topics. This function has two parameters, topic and msg (See sys_bus.publish() for details).
    :return:
    """


def publish(topic , msg):
    """Publishes messages. The server will receive the subscribed topics and process the message with multithreading.

    :param topic: String or integer type. The topic to be subscribed to.
    :param msg: The published messages.
    :return:
    """


def sub_table(topic=None):
    """Views the subscription registry, including all topics and the subscribed functions.

    :param topic: String or integer type. Topics. If this parameter is specified, view the registry of the specified topic. If this parameter is omitted, view the registry of all topics.
    :return: Dict or list type. The list or registry of the subscribed functions.
    """


def unsubscribe(topic , cb=None):
    """Unsubscribes from the subscribed topics or a function under the topics. If only topic is specified, unsubscribe from the topics and all subscribed functions under the topics. If both topic and cb are specified, unsubscribe from the callback function under the subscribed topics.

    :param topic: String or integer type. The subscribed topics.
    :param cb: Function type. Callback function. The function to be unsubscribed from. Unsubscribe from the subscribed topics if this parameter is omitted.
    :return:True – Successful execution; False – Failed execution
    """
