"""
Function:
This feature provides the APIs of the built-in GNSS feature.
Only EC200UCNAA/EC200UCNLA/EC200UEUAA/EC800MCNGA/EC800GCNGA series module supports this feature.

Descriptions taken from:
https://python.quectel.com/doc/API_reference/en/gnsslib/quecgnss.html
"""


def init():
    """Initializes the built-in GNSS feature.

    :return:0 - Successful execution;-1 - Failed execution
    """


def get_state():
    """Gets the current working status of the built-in GNSS feature.

    :return:
    0	int	GNSS feature is disabled.
    1	int	GNSS firmware is being updated.
    2	int	GNSS is positioning. In this mode, the module can read the GNSS location data. After obtaining the location data, the user needs to analyze the corresponding sentence to determine whether the location data is effective. For example, if the status of GNRMC sentences is A or V, A indicates valid positioning and V indicates invalid positioning.
    """


def gnssEnable(opt):
    """Enables or disables GNSS feature. If you use the built-in GNSS feature for the first time after powering the module on, you need not call this function to enable GNSS feature, but call quecgnss.init() directly. quecgnss.init() will automatically enable the GNSS feature when GNSS feature is initialized.

    :param opt:Integer type. Enable or disable GNSS.0 - Disable the GNSS feature.;1 - Enable the GNSS feature.
    :return:0 - Successful execution;-1 - Failed execution
    """


def read(size):
    """Gets GNSS location data.

    :param size:Integer type. Size of the data to be read. Unit: byte.
    :return:A tuple (size, data) - Successful execution
        size - Size of the data read.
        data - GNSS location data.
    """
