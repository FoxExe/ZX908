"""
Function:
USB Network Card
Module feature: USB network card.
Note: EC600S, EC600N, EC800N, EC200U, EC600U and EC600M series modules support this feature.

Descriptions taken from:
https://python.quectel.com/doc/API_reference/en/peripherals/misc.USBNET.html
"""


def set_worktype(type):
    """
    Note: It takes effect after the module is rebooted.

    :param type: USBNET working type. Integer type. Type_ECM: ECM mode. Type_RNDIS: RNDIS mode.
    :return: 0 - Successful execution; -1 - Failed execution
    """

def get_worktype():
    """
    :return: If successful, it returns current work type of USBNET. If failed, it returns integer type -1; 1 indicates ECM mode. 3 indicates RNDIS mode.
    """

def get_status():
    """

    :return: If successful, it returns the USBNET current state. If failed, it returns the integer -1; 0 indicates no connection. 1 indicates successful connection.
    """

def open():
    """
    :return: 0 - Successful execution; -1 - Failed execution
    """

def close():
    """
    :return: 0 - Successful execution; -1 - Failed execution
    """

def getNat(simid, pid):
    """Gets NAT enabling status of a specified network card (whether IPv6 dial-up is supported).

    Note: Only EC200U and EC600U series modules support this function.

    :param simid: Integer type. Range: 0 and 1. Currently only 0 is supported.
    :param pid: Integer type. PDP index. Range: 1-7.
    :return: If successful, it returns NAT enable situation. Integer type: 0 and 1. 0: Enable and IPv6 dial-up is supported. 1: Disable and IPv6 dial-up is not supported.If failed, it returns integer -1.
    """

def setNat(simid, pid, nat):
    """Sets NAT.

    After NAT is set successfully, the configuration takes effect after the module is rebooted. The nat value changes to 1 when you call USBNET.set_worktype(), in which case pid cannot perform IPv6 dial-up, thus this function can be called to disable NAT to turn IPv6 dial-up back to normal after USBNET is disabled.
    Note: Only EC200U and EC600U series modules support this function.

    :param simid: Integer type. Range: 0 and 1. Currently only 0 is supported.
    :param pid: Integer type. PDP index. Range: 1-7.
    :param nat: Integer type. Range: 0 and 1. 0: IPv6 dial-up is supported; 1: IPv6 dial-up is not supported.
    :return: 0 indicates successful setting. -1 indicates setting failure.
    """

Type_ECM: int = ...  # ECM mode.
Type_RNDIS: int = ...  # RNDIS mode.
