"""
Function:
For L76K module or GNSS modules with similar data type, you can get information such as whether the positioning is successful,
the latitude and longitude, UTC time, the positioning mode, the number of satellites used for positioning,
the number of visible satellites, the azimuth angle of positioning, the ground speed and the geodetic height.
Currently, for L76K module, the data got through the interface provided by this module is read from the GNGGA, GNRMC and GPGSV sentences in the original GNSS data package read through the UART.
Note: Currently, only EC600S/EC600N/EC800N/EC200U/EC600U/EC600M/EC800M series module supports this method.

Descriptions taken from:
https://python.quectel.com/doc/API_reference/en/gnsslib/gnss.html
"""


class GNSS(object):

    def read_gnss_data(self, max_retry=1, debug=0):
        """Reads the GNSS data through the UART and returns the length of the GNSS data.

        :param max_retry:Integer type. It is an optional parameter. When the GNSS data is invalid, this parameter indicates the maximum times of automatic data-reading. Exit when the data length is 0, that is, no data has been read. Default value: 1.
        :param debug:Integer type. It is an optional parameter indicating that whether the debugging information is output in the progress of reading and analyzing the GNSS data. 0 – Not output. 1 – Output. Default value: 0.
        :return:Integer type. Length of the GNSS data read through the UART. Unit: byte.
        """

    def getOriginalData(self):
        """This interface gets the original GNSS data read through the UART. You can get the original GNSS data through this interface for data processing or confirmation. The original GNSS data will be returned after gnss.read_gnss_data(max_retry=1, debug=0) is called.

        :return:String type. The original GNSS data read from the UART.
        """

    def checkDataValidity(self):
        """This interface checks the validity of GNGGA, GNRMC and GPGSV sentences in the GNSS data package read. The GNSS module provides an interface for reading GNGGA, GNRMC and GPGSV sentences in the original GNSS data package through the UART.

        Return Value:
        A list (gga_valid, rmc_valid, gsv_valid).
        gga_valid - Whether the GNGGA sentence is read and has been analyzed successfully. 0 – The GNGGA sentence is not read or the data is invalid. 1 – The GNGGA sentence is valid.
        rmc_valid - Whether the GNRMC sentence is read and has been analyzed successfully. 0 – The GNRMC sentence is not read or the data is invalid. 1 – The GNRMC sentence is valid.
        gsv_valid - Whether the GPGSV sentence is read and has been analyzed successfully. 0 – The GPGSV sentence is not read or the data is invalid. 1 – The GPGSV sentence is valid.
        If you only want to get the positioning result, that is whether the GNGGA sentence is valid, you can set gga_valid as 1 or check whether the positioning is successful through gnss.isFix() . The GNRMC sentence is analyzed to get the ground speed and the GPGSV sentence is analyzed to get the number of visible satellites and the corresponding azimuth angles of these satellites. Therefore, rmc_valid and gsv_valid can be omitted.
        """

    def isFix(self):
        """Checks whether the valid GNSS data is read through the specified UART.

        :return:1 – Successful execution;0 – Failed execution
        """

    def getUtcTime(self):
        """Gets UTC time in the GNSS data.

        :return:UTC time in string type – Successful execution;-1 – Failed execution
        """

    def getLocationMode(self):
        """Gets the positioning mode in the GNSS data.

        :return:
        -1	Failed execution. No data is read through the UART or the data read through the UART is invalid.
        0	Unavailable or invalid positioning data
        1	Valid positioning. Positioning mode: GPS or SPS mode.
        2	Valid positioning. Positioning mode: DGPS or DSPS mode.
        6	Estimation (dead reckoning) mode
        """

    def getUsedSateCnt(self):
        """Gets the number of satellites in use in the GNSS data.

        :return:The number of satellites in use in integer type – Successful execution;-1 – Failed execution
        """

    def getLocation(self):
        """Gets the latitude and longitude information in the GNSS data.

        :return:Latitude and longitude information (longitude, lon_direction, latitude, lat_direction) – Successful execution
        -1 – Failed execution
        longitude - Longitude in float type.
        lon_direction - Longitude direction in string type. E – east longitude. W – west longitude.
        latitude - Latitude in float type.
        lat_direction - Latitude direction in string type. N – north latitude. S – south latitude.
        """

    def getViewedSateCnt(self):
        """Gets the number of visible satellites in the GNSS data.

        :return:The number of visible satellites in integer type – Successful execution;-1 – Failed execution
        """

    def getCourse(self):
        """Gets the visible azimuth angles of GNSS satellites in the GNSS data.

        :return:All visible azimuth angles of GNSS satellites. Range: 0–359. Take due north as the reference plane. The form of return value is a dictionary in which the key indicates the satellite ID and the value indicates the azimuth angle. Please note that the value may be an integer or empty, which depends on whether there is a value for the azimuth angle in the GPGSV sentences in the original GNSS data.;-1 – Failed execution
        The format of the return value is as follows: {key:value, ..., key:value}
        """

    def getSpeed(self):
        """Gets the ground speed in the GNSS data.

        :return:Ground speed in float type. Unit: km/h. – Successful execution;-1 – Failed execution
        """


def GnssGetData(uartn,baudrate,databits,parity,stopbits,flowctl) -> GNSS:
    """Creates a GNSS object to get the GNSS data. Parameters are the type of UARTs for mounting the GNSS module and communication parameters.

    :param uartn:Integer type.
    0-uart0 - DEBUG PORT
    1-uart1 – BT PORT
    2-uart2 – MAIN PORT
    3-uart3 – USB CDC PORT
    :param baudrate:Integer type. Baud rate. Some common baud rates are supported, like 4800, 9600, 19200, 38400, 57600, 115200 and 230400.
    :param databits:Integer type. Data bit. Range: [5–8]. ECX00U series module only supports 8 data bits.
    :param parity:Integer type. Parity check.
    0 – NONE
    1 – EVEN
    2 – ODD
    :param stopbits:Integer type. Stop bit. Range: [1–2].
    :param flowctl:Integer type. Hardware control flow.
    0 – FC_NONE
    1 – FC_HW
    :return:A GNSS object
    """
