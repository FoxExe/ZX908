"""
Function:
This module provides the class of Wi-Fi positioning and gets the module longitude and latitude coordinate.
Currently, only EC600S/EC600N/EC800N/EC200U/EC600U/EG912U/EG915U series module supports this feature.

Descriptions taken from:
https://python.quectel.com/doc/API_reference/en/gnsslib/wifilocator.html
"""


class wifilocator:

    def __init__(self, token=None):
        """Creates a wifilocator object and configures the suite token of Wi-Fi positioning. Creates a wifilocator object and uses a specified token to configure the Wi-Fi positioning suite.

        :param token:String type. Secret key. It consists of 16 bit characters and you can apply for it from Quectel.
        """

    def getwifilocator(self):
        """This method gets the module longitude and latitude coordinate.

        :return:If successful, it returns the module longitude and latitude coordinate. Tuple format: (longtitude, latitude, accuracy);
            longtitude : longitude.
            latitude : latitude.
            accuracy : accuracy. Unit: meter.
            If failed, it returns the error code. The error code description is as follows:
            1 – Network error. Please confirm whether the dial is normal.
            2 – Secret key length error. The length must be 16 bytes.
            3 – Error in getting coordinates.
        """
