"""
Function:
ussl realizes the encrypted communication using TLS/SSL protocol, mainly for unidirectional and bidirectional authentication.

Descriptions taken from:
https://python.quectel.com/doc/API_reference/en/networklib/ussl.html
"""
from usocket import socket


def wrap_socket(sock,server_hostname=None,cert=None,key=None) -> socket:
    """Create Secure Channel over SSL

    :param sock:The usocket.socket object to be wrapped. Required parameter.
    :param server_hostname:String type. Server IP address. Optional parameter.
    :param cert:String type. Digital certificate. Optional parameter.
    :param key:String type. Private key. Optional parameter.
    :return: A wrapped usocket.socket object.
    """
