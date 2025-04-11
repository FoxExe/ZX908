"""
Function:
Miscellaneous Features, Module feature: shutdown, software restart, PWM and ADC.

Descriptions taken from:
https://python.quectel.com/doc/API_reference/zh/peripherals/misc.html
"""


def antennaSecRXOffCtrl(*args):
    """Configures and queries the diversity of antennas. (EC200A series module supports this interface).

    :param args: When the number of parameter is 0, query through: misc.antennaSecRXOffCtrl(); When the number of parameter is 1, set through: misc.antennaSecRXOffCtrl(SecRXOff_set). Integer type. Range: 0/1. 0: Do not close diversity antennas 1: Close diversity antennas.
    :return: Query: If successful, it returns the diversity antenna configuration. If failed, it returns integer -1; Set: If successful, it returns integer 0; If failed, it returns integer -1.
    """


class PowerKey(object):
    """PowerKey Callback and Registration.

    Descriptions: https://python.quectel.com/doc/API_reference/en/peripherals/misc.PowerKey.html

    This class provides the feature of triggering the callback function when registering the powerkey event.
    """

    def powerKeyEventRegister(self, usrFun):
        """This method registers the callback function for the powerkey event.

        Note: For EC600S and EC600N series modules: The callback function will be triggered when pressing and releasing the powerkey. For EC200U and EC600U series modules: The callback function will be triggered only when releasing the powerkey and the key have been pressed for at least 500 ms.

        :param usrFun: Callback function whose prototype is usrfun (status). The parameter is status with 0 indicating to release and 1 indicating to press. The callback will be triggered when pressing or releasing the powerkey.
        :return: 0 - Successful registration; -1 - Failed registration
        """


class PWM(object):
    """Pulse Width Modulation.

    Descriptions: https://python.quectel.com/doc/API_reference/en/peripherals/misc.PWM.html

    This class provides the feature of PWM output.
    Note: BC25 series module does not support this feature.
    """

    def __init__(self, PWMn, ABOVE_xx, highTime, cycleTime):
        """
        :param PWMn: Integer type. PWM channel. Click here to learn more for supported channels and corresponding pins.
        :param ABOVE_xx: Integer type. Time range.
        For EC200U, EC600U and EG915U series modules:
        PWM.ABOVE_MS ms-level time range: (0,10]
        PWM.ABOVE_1US us-level time range: (0,10000]
        PWM.ABOVE_10US us-level time range: (1,10000]
        PWM.ABOVE_BELOW_US ns-level time range: [100,65535]
        :param highTime: Integer type. High level time.
        For ms-level time, unit: ms.
        For us-level time, unit: us.
        For ns-level: it needs to be calculated by users.
        Frequency = 13Mhz / cycleTime
        Duty cycle = highTime/ cycleTime
        :param cycleTime: Integer type. Cycle time.
        For ms-level time, unit: ms.
        For us-level time, unit: us.
        For ns-level: it needs to be calculated by users.
        Frequency = 13Mhz / cycleTime
        Duty cycle = highTime/ cycleTime
        """

    def open(self):
        """These methods enables PWM output.

        :return: 0 - Successful execution; -1 - Failed execution
        """

    def close(self):
        """These methods disables PWM output.

        :return: 0 - Successful execution; -1 - Failed execution
        """

    PWM0: int = ...  # EC600S / EC600N / EC100Y / EC600U / EC200U / EC800N / EC600M / EG915U / EC800M / EG912N
    PWM1: int = ...  # EC600S / EC600N / EC100Y / EC800N / EC600M / EC800M / EG912N
    PWM2: int = ...  # EC600S / EC600N / EC100Y / EC800N / EC600M / EC800M / EG912N
    PWM3: int = ...  # EC600S / EC600N / EC100Y / EC800N / EC600M / EC800M / EG912N


class ADC(object):
    """Voltage Collection.

    Descriptions: https://python.quectel.com/doc/API_reference/en/peripherals/misc.ADC.html

    This class collects voltage signals.
    """

    def open(self):
        """This method initializes ADC.

        :return: 0 - Successful execution; -1 - Failed execution
        """

    def read(self, ADCn):
        """This method reads voltage values of a specified channel. Unit: mV.

        :param ADCn: Integer type. ADC channel. Click here to learn more for supported channels and corresponding pins.
        :return: If successful, a specified channel voltage value is returned. -1 - Failed execution.
        """

    def close(self):
        """
        :return: 0 - Successful execution; -1 - Failed execution
        """

    ADC0: int = ...  # EC600S / EC600N / EC100Y / EC600U / EC200U / BC25PA / EC800N / BG95M3 / EC200A / EC600M / EG915U / EC800M / EG912N
    ADC1: int = ...  # EC600U / EC200U / EC200A / EC600M / EG915U / EC800M / EG912N
    ADC2: int = ...  # EC600U / EC200U
    ADC3: int = ...  # EC600U


class USB(object):
    """USB Plug-in/Out Detection

    Descriptions: https://python.quectel.com/doc/API_reference/en/peripherals/misc.USB.html

    This class provides USB plug-in/out detection.
    Note: EC600S, EC600N, EC800N, EG912N, EC200U, EC600U, EG915U, EC600M, EC800M, EC200A series modules support this feature.
    """

    def getStatus(self):
        """This method gets the current USB connection status.

        :return: -1 - Failed execution; 0 - Currently not connected to USB; 1 - USB connected
        """

    def setCallback(self, usrFun):
        """This method registers USB plug-in/out callback function. When USB is inserted or unplugged, a callback function will be triggered to notify you of the current USB status.

        Note: please do not perform blocking operations in this callback function.

        :param usrFun: Callback function whose prototype is usrFun (conn_status). The parameter is conn_status with 0 indicating not connected and 1 indicating connected.
        :return: 0 - Successful registration; -1 - Failed registration
        """
