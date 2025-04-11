"""
Function:
This feature is used for time synchronization.

Note: You need to confirm with the carrier whether the current SIM card supports this feature.

Descriptions taken from:
https://python.quectel.com/doc/API_reference/en/networklib/ntptime.html
"""


# the current NTP server address. Default value: "ntp.aliyun.com".
host: str = ...


def sethost(host):
    """Sets NTP server address.

    :param host:NTP server address0 - Successful execution
    :return:0 - Successful execution;-1 - Failed execution
    """


def settime(timezone=0):
    """Synchronize NTP server time.

    :param timezone:Range: -12 to 12. Default value: 0.
    :return:0 - Successful execution;-1 - Failed execution
    """
