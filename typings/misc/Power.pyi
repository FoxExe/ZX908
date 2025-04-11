"""
Function:
Module features: power off, reboot software, get the power-on reason, get the last power-off reason and get battery voltage.

Descriptions taken from:
https://python.quectel.com/doc/API_reference/en/peripherals/misc.Power.html
"""

def powerDown():
    """This method powers off the module."""

def powerRestart():
    """This method reboots the module."""

def powerOnReason():
    """This method gets the power-on reason.

    :return:
    Value	Description
    0	Failed to get the power-on reason or unknown power-on reason
    1	Press PWRKEY to power on
    2	Press RESET to reboot
    3	Power-on triggered by VBAT
    4	Power-on triggered by RTC
    5	Reboot triggered by watchdog or power-on error
    6	Power-on triggered by VBUS
    7	Power-on triggered by charging
    8	Wake up from PSM
    9	Reboot after dump occurs
    """

def powerDownReason():
    """This method gets the power-off reason.

    Note: BC25PA, EC200U and EC600U series modules do not support this method.

    :return:
    Value	Description
    0	Unknown reason
    1	Power off normally
    2	Power off due to high power supply voltage
    3	Power off due to low power supply voltage
    4	Power off due to high temperature
    5	Power-off triggered by watchdog
    6	Power-off triggered by low VRTC voltage
    """

def getVbatt():
    """This method gets the battery voltage. Unit: mV.

    :return: Integer type. Voltage value.
    """
