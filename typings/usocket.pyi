"""
Function:
This module provides access to the BSD socket interface, and realizes subsets of the corresponding CPython module.
See CPython file socket for more detailed information: https://docs.python.org/3.5/library/socket.html#module-socket

Descriptions taken from:
https://python.quectel.com/doc/API_reference/zh/stdlib/usocket.html
"""


AF_INET = ...  # IPV4 type. Address family.
AF_INET6 = ...  # IPV6 type. Address family.
SOCK_STREAM = ...  # socket type. A TCP-based stream socket.
SOCK_DGRAM = ...  # socket type. A UDP-based datagram socket
SOCK_RAW = ...  # socket type. A raw socket
IPPROTO_TCP = ...  # Protocol number. TCP protocol.
IPPROTO_UDP = ...  # Protocol number. UDP protocol.
IPPROTO_TCP_SER = ...  # Protocol number. TCP server.
TCP_CUSTOMIZE_PORT = ...  # Protocol number. TCP client can customize address.
SOL_SOCKET = ...  # The level of the socket option.
SO_REUSEADDR = ...  # The socket feature option. The port multiple is enabled.
TCP_KEEPALIVE = ...  # The socket feature option. Sets intervals of the TCP keep-alive packet.


class socket(object):

    def __init__(self, af=AF_INET, type=SOCK_STREAM, proto=IPPROTO_TCP):
        """Creates a socket object based on the specified address family, socket type, and protocol type parameters.

        Note that it is not necessary to specify proto in most cases, nor is it recommended,
        because some MicroPython ports may omit the IPPROTO_* constant.

        :param af: The address family (please refer to the Constants).
        :param type: The socket type (please refer to the Constants).
        :param proto: The protocol number (please refer to the Constants).
        """

    def bind(self, address: tuple):
        """This method binds the socket to the specified address. The socket must not yet be bound.

        1. When the socket is a server, it must be bound to fix the address of the server.
        2. When the socket is a client, it should be bound to address to specify the socket for data processing (It should be used with usocket.TCP_CUSTOMIZE_PORT).

        :param address: The list or tuple containing addresses and port numbers.
        """

    def listen(self, backlog: int):
        """This method allows the socket server to listen to the client connection and specify the maximum connection number of the client.

        :param backlog: The maximum number for accepting the socket, at least 0.
        """

    def accept(self):
        """This method allows the socket server to accept the connection request.

        @return: If successful, a tuple, which contains the new socket, client address and client port, will be returned. The form is : (conn, address, port).
        conn: The new socket object which is used to interact with the client.
        address: The client address connected to the server.
        port: The client port connected to the server.
        """

    def connect(self, address: tuple):
        """This method allows the socket to connect the server of the specified address parameter.

        :param address: The list or tuple containing addresses and port numbers.
        """

    def read(self, size: int = None):
        """This method reads size byte data from the socket and returns a byte object.

        :param size: If size is not specified, all readable data will be read from the socket until there is no more data to be read. At this time, this function is the same as socket.readall().
        :return: bytes。
        """

    def readinto(self, buf, nbytes: int = None):
        """This method reads bytes from the socket into the buffer buf.

        :param buf: bytearray
        :param nbytes: If nbytes is specified, the most maximum bytes can be read is the number of nbytes. If nbytes is not specified, len(buf) bytes can be read at most. The return value is the actual number of read bytes.
        :param return: bytes number.
        """

    def readline(self):
        """This method reads data from a socket by line and stops reading when a newline character is encountered, and returns the read line."""

    def write(self, buf):
        """This method allows the socket to send the data in buffer, and buf is the data to be sent. Then the actual sent bytes number is returned."""

    def send(self, buf):
        """This method allows the socket to send data and returns the actual sent bytes number."""

    def sendall(self, buf):
        """This method allows the socket to send all data to the socket.

        Unlike send(), this method attempts to send all the data block by block.
        Note: The operation of this method on the non-blocking socket is indeterminate, so in MicroPython, it is recommended to use write().
        The write() method has the same "No-short-writing" policy to block the socket, and will return the number of bytes sent on the non-blocking socket.
        """

    def sendto(self, buf, address):
        """This method allows the socket to send data to the specified address, and returns the actual sent bytes number.

        :param buf: The data in bytes type.
        :param address: The list or tuple containing addresses and port numbers.
        """

    def recv(self, size: int):
        """This method receives the data from the socket. The return value is a byte object which indicates the received data. The maximum data size received at a time is determined by bufsize.

        :param size: The maximum data size received at a time.
        """

    def recvfrom(self, size: int):
        """This method receives the data from the socket.

        The return value is a tuple which contains the byte object and address.
        The form of the return value is: (bytes, address).

        :param size: The maximum data size received at a time.
        :return: (bytes, address)
        bytes -The byte object that receives the data.
        address -The address of the socket that sends the data.
        """

    def close(self):
        """This method marks the socket as closed and releases all resources."""

    def setsockopt(self, level, optname, value):
        """This method sets the value of the socket option.

        :param level: The level of the socket option.
        :param optname: The feature option of the socket.
        :param value: It can be either an integer or an object in bytes type which represents the buffer.
        """

    def setblocking(self, flag: bool):
        """This method sets the socket as either blocking mode or non-blocking mode. This method is a simplification of settimeout().

        :param flag: Sets whether the socket mode is blocking (default mode: blocking mode).
        """

    def settimeout(self, timeout: int):
        """This method sets timeouts of the send and received data of the socket. Unit: second.

        :param timeout: It can be a non-negative floating point which represents second or None. If the parameter value is 0, the socket will be set to non-blocking mode, otherwise the socket will be in blocking mode.
        """

    def makefile(self, mode='rb'):
        """This method returns the file object associated with the socket.

        The type of the return value is related to the specified parameter.
        The mode parameter only supports binary pattern (rb and wb).
        """

    def getsocketsta(self):
        """This method gets the status of TCP socket.

        Note:
        1. BG95 series module does not support this API.
        2. After calling socket.close() , -1 will be returned if socket.getsocketsta() is called, because the created object resources and other things have been released.

        @return: the status value of TCP socket
        Status Value	Status	Description
        0	CLOSED	The socket is created but not used.
        1	LISTEN	The socket is listening to the connection.
        2	SYN_SENT	The socket is trying to establish a connection actively. That is, ACK has not been received after sending the SYN.
        3	SYN_RCVD	The socket is in the initial synchronization status of the connection. That is, the SYN sent from the opposite has been received, but the ACK of the sent SYN has not been received.
        4	ESTABLISHED	The socket has successfully established the connection.
        5	FIN_WAIT_1	The socket is closed and the TCP connection is closing. That is, the FIN is sent actively, but the ACK or FIN sent from the party closed passively has not been received.
        6	FIN_WAIT_2	The local socket is closed and the remote socket is waiting to be closed. That is, the ACK corresponding to the sent FIN is received in the FIN_WAIT_1 status.
        7	CLOSE_WAIT	The remote socket is closed and the local socket is waiting to be closed. The passively closed party receives the FIN.
        8	CLOSING	The local socket is closed and the remote socket is closing. The close confirmation is suspended. That is, the FIN sent from the passively closed party has been received in FIN_WAIT_1 status.
        9	LAST_ACK	The remote socket is closed , and the close confirmation of the local socket is being waited. The passively closed party sends the FIN in CLOSE_WAIT status.
        10	TIME_WAIT	The remote socket is closed and the local socket is waiting to be closed. That is, the four-way wavehand FIN, ACK, FIN, and ACK are complete. The TCP connection is disconnected after 2MSL time.
        """


def getaddrinfo(host: str, port: int):
    """Parses the domain name of DNS.

    Parses the domain name of the host (host) and port (port) into a 5-tuple sequence used to create the socket. The structure of the tuple is below:
    (family, type, proto, canonname, sockaddr)

    @param host: The domain name of the host.
    @param port: The port.
    @return: (family, type, proto, canonname, sockaddr)
    """
