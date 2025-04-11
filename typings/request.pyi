"""
Function:
The request feature is used for sending an HTTP request to a server, fetching data from a server, or submitting data to a server. Multiple request methods, including GET, POST, and PUT are supported.

Descriptions taken from:
https://python.quectel.com/doc/API_reference/en/networklib/request.html
"""


class Response(object):
    """Response Class

    After the request library sends a request, a response object will be returned which contains all information sent by the server, such as response status codes, response headers, and response bodies.
    """

    def __init__(self, *args, **kwargs):
        self.status_code: int = ...   # Integer type. The request status codes.
        self.headers: dict = ...  # Dict type. The request header.

    @property
    def text(self):
        """Gets the text data of the response body.

        :return:A generator object reading all returned text data through a for loop.
        """

    @property
    def content(self):
        """Gets the response body.

        :return:A generator object reading all returned response body data through a for loop.
        """

    def json(self):
        """Gets the response body in JSON format.

        :return:The response data in dictionary type.
        """


def get(url, data=None, headers=None, decode=True, sizeof=255, ssl_params=None) -> Response:
    """Sends a GET request.

    :param url:Required parameter. The server IP address in the request.
    :param data:Optional parameter. Parameters to be carried in JSON format in the request.Dictionary type. Optional parameter. The header information in the request.
    :param headers:Dictionary type. Optional parameter. The header information in the request.
    :param decode:Boolean type. Optional parameter. Decode the response result with UTF-8 after the request is successful. True: Decode. False: Not decode. Default value: True. Bytes will be returned if False is entered. This parameter is only used for response.content.
    :param sizeof:Optional parameter. The size of the data blocks in the buffer. Recommended value: 255–4096. Default value: 255. The larger the value, the faster the read speed. Unit: byte.
    :param ssl_params:Optional parameter. The secret key information in the SSL authentication. Format: {"cert": certificate_content, "key": private_content}.
    :return:A response object containing all information returned by the server, such as response status codes, response headers, and response bodies.
    """


def post(url, data=None, headers=None, decode=True, sizeof=255) -> Response:
    """Sends a POST request.

    :param url:Required parameter. The server IP address in the request.
    :param data:Optional parameter. Parameters to be carried in JSON format in the request.
    :param headers:Dictionary type. Optional parameter. The header information in the request.
    :param decode:Boolean type. Optional parameter. Decode the response result with UTF-8 after the request is successful. True: Decode. False: Not decode. Default value: True. Bytes will be returned if False is entered. This parameter is only used for response.content.
    :param sizeof:Optional parameter. The size of the data blocks in the buffer. Recommended value: 255–4096. Default value: 255. The larger the value, the faster the read speed. Unit: byte.
    :return:A response object containing all information returned by the server, such as response status codes, response headers, and response bodies.
    """


def put(url, data=None, headers=None, decode=True, sizeof=255) -> Response:
    """Sends a PUT request.

    :param url:Required parameter. The server IP address in the request.
    :param data:Optional parameter. Parameters to be carried in JSON format in the request.
    :param headers:Dictionary type. Optional parameter. The header information in the request.
    :param decode:Boolean type. Optional parameter. Decode the response result with UTF-8 after the request is successful. True: Decode. False: Not decode. Default value: True. Bytes will be returned if False is entered. This parameter is only used for response.content.
    :param sizeof:Optional parameter. The size of the data blocks in the buffer. Recommended value: 255–4096. Default value: 255. The larger the value, the faster the read speed. Unit: byte.
    :return:A response object containing all information returned by the server, such as response status codes, response headers, and response bodies.
    """


def head(url, data=None, headers=None, decode=True, sizeof=255) -> Response:
    """Sends a HEAD request.

    :param url:Required parameter. The server IP address in the request.
    :param data:Optional parameter. Parameters to be carried in JSON format in the request.
    :param headers:Dictionary type. Optional parameter. The header information in the request.
    :param decode:Boolean type. Optional parameter. Decode the response result with UTF-8 after the request is successful. True: Decode. False: Not decode. Default value: True. Bytes will be returned if False is entered. This parameter is only used for response.content.
    :param sizeof:Optional parameter. The size of the data blocks in the buffer. Recommended value: 255–4096. Default value: 255. The larger the value, the faster the read speed. Unit: byte.
    :return:A response object containing all information returned by the server, such as response status codes, response headers, and response bodies.
    """

