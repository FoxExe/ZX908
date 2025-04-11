"""
Function:
This module provides base station location feature and gets the latitude and longitude coordinate information of QuecPython modules.
Currently, only EC600S/EC600N/EC800N/EC200U/EC600U/EG912U/EG915U series module supports this feature.

Descriptions taken from:
https://python.quectel.com/doc/API_reference/en/gnsslib/cellLocator.html
"""


def getLocation(serverAddr, port, token, timeout, profileIdx=None):
    """This method gets the module's latitude and longitude coordinate information.

    :param serverAddr:String type. Server domain name with a length less than 255 bytes. Currently only “www.queclocator.com” is supported.
    :param port:Integer type. Server port. Currently only port 80 is supported.
    :param token:String type. A 16-character key, and application is required.
    :param timeout:Integer type. Timeout. Range: 1–300. Unit: s. Default value: 300.
    :param profileIdx:Integer type. PDP context ID. Range: 1–3. It is an optional parameter and the default is the one that has been successfully dialed. Setting other values may require a dedicated APN and password.
    :return:Returns the longitude and latitude coordinate information in tuple format: (longtitude, latitude, accuracy). (0.0, 0.0, 0) indicates invalid coordinate information.
        longtitude: Longitude.
        latitude: Latitude.
        accuracy: Accuracy. Unit: meter.
    The error codes are described as follows:
        1 – Failed initialization
        2 – The server address is too long (more than 255 bytes)
        3 – Key length error (It must be 16 bytes)
        4 – The timeout is out of range. The supported range is 1–300
        5 – The specified PDP is not connected to the network
        6 – Obtaining location error
    """
