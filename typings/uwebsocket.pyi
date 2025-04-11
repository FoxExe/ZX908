"""
Function:
This feature establishes a WebSocket connection.

Descriptions taken from:
https://python.quectel.com/doc/API_reference/en/networklib/uwebsocket.html
"""


CLOSE_OK: int = 1000


class Websocket(object):
    """
    Basis of the Websocket protocol.

    This can probably be replaced with the C-based websocket module, but
    this one currently supports more options.
    """
    is_client = False

    def recv(self):
        """Receive data from the websocket.

        This is slightly different from 'websockets' in that it doesn't
        fire off a routine to process frames and put the data in a queue.
        If you don't call recv() sufficiently often you won't process control
        frames.
        :return: String type. The returned result. When this value is null or None, the connection is closed.
        """

    def send(self, buf):
        """Send data to the websocket.

        :param buf:
        :return:
        """

    def close(self, code=CLOSE_OK, reason=''):
        """Close the websocket.

        :param code:
        :param reason:
        :return:
        """


class WebsocketClient(Websocket):
    is_client = True


class Client(object):

    @classmethod
    def connect(cls, url, headers=None, debug=False) -> WebsocketClient:
        """

        :param url:String type. WebSocket connection URL, usually in the form of "ws://xxx/" or "wss://xxx/".
        :param headers:Dict type. The additional header to be added, used in the scenarios where both the standard header and the additional header passed by users are allowed.
        :param debug:Bool type. True – Output logs. False – Not output logs. Default value: False.
        :return:
        """

