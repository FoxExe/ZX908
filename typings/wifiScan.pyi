"""
Function:
wifiScan provides both synchronous and asynchronous modes to scan the Wi-Fi hotspot information around the module.
The following modules support the wifiScan feature.
EC100Y/EC200N/EC600N/EC600S/EC600M/EC800M/EC800N/EG912N/EG915N/EG810M/EC600G/EC800G/EC200U/EC600U/EG912U/EG915U series module.
In EC600M series module: EC600MCN_LA/EC600MCN_LE/EC600MEU_LA support the wifiScan feature.
In EC800M series module: EC800MCN_GA/EC800MCN_LA/EC800MCN_LE/EC800MCN_LF/EG810MCN_GA support the wifiScan feature.
In EC600U series module: EC600UCN_LB/EC600UEU_AB support the wifiScan feature.
In E200U series module: EC200UAU_AA/EC200UAU_AB/EC200UCN_AA/EC200UCN_LA/EC200UCN_LB/EC200UEU_AA/EC200UEU_AB support the wifiScan feature.
In EG912U series module: EG912UGL_AA support the wifiScan feature.
In EG915U series module: EG915UEU_AB/EG915ULA_AB support the wifiScan feature.

Descriptions taken from:
https://python.quectel.com/doc/API_reference/en/gnsslib/wifiScan.html
"""


def control(option):
    """Enables or disables Wi-Fi scan.

    :param option:Integer type. Wi-Fi scan control option.
        0 - Disable Wi-Fi scan
        1 - Enable Wi-Fi scan
    :return:0 - Successful execution;-1 - Failed execution
    """


def getState():
    """Gets the current status of Wi-Fi scan.

    :return:True - The Wi-Fi scan is enabled.;False - The Wi-Fi scan is disabled.
    """


def setCfgParam(timeout, round, maxNums, priority):
    """Sets the scan parameters of Wi-Fi scan.

    EC200U/EC600U/EG912U/EG915U/EC600G/EC800G series module does not support priority, so priority can be omitted.

    :param timeout:Integer type. Timeout. When a timeout is triggered, the system automatically reports the detected hot spots. If the specified number of hot spots is detected before the timeout, the system stops scanning and returns the scanning result. Range: 4–60. Unit: s.
    :param round:Integer type. Number of scan rounds. When the number of scan rounds is reached, the scan ends and the scan result is returned. Range: 1–3. Unit: time.
    :param maxNums:Integer type. The maximum number of scanned hotspots. When the number of scanned hotspots reaches the upper limit, the scan ends and the scan result is returned. Range: 4–30.
    :param priority:Integer type. Priority of businesses.
        0 - Network business first. Wi-Fi scan will be interrupted when a data service is initiated.
        1 - Wi-Fi scan first. When a data service is initiated, the RRC connection is not set up. To ensure that the Wi-Fi scan is performed properly, the RRC connection is set up only after the scan is complete.
    :return:0 - Successful execution;-1 - Failed execution
    """


def getCfgParam():
    """Gets the scan parameters of Wi-Fi scan.

    :return:A tuple (timeout, round, maxNums, priority) - Successful execution;-1 - Failed execution
    """


def setCallback(fun):
    """Registers the callback function. When asynchronous scanning is used, you need to register the callback function, and the scan result is returned to the user through the callback function.

    :param fun:Callback function name. The callback function format and parameters are described below.
        def wifiscanCallback(args):
            pass
    arameter	Type	Description
    args	Tuple	    (nums, [(mac, rssi),...,(mac, rssi)])
                        nums - Integer type. The number of scanned Wi-Fi hotspots.
                        mac - String type. MAC address of the Wi-Fi hotspots.
                        rssi - Integer type. Signal strength of the Wi-Fi hotspots.
    :return: 0 - Successful execution;-1 - Failed execution
    """


def asyncStart():
    """Starts scanning in Wi-Fi scan asynchronous mode. The scan result is returned through the registered callback function.

    :return:0 - Successful execution;-1 - Failed execution
    """


def start():
    """Starts scanning in Wi-Fi scan synchronous mode. The scan result is returned after the scan is complete. Because the interface is synchronous, the program will be blocked in the interface when the scan does not end.

    :return:A tuple (wifiNums, [(mac, rssi), ... , (mac, rssi)]) - Successful execution;-1 - Failed execution
    Parameter	Type	Description
    wifiNums	Integer	The number of scanned Wi-Fi hotspots.
    mac	String	MAC address of the Wi-Fi hotspots.
    rssi	Integer	Signal strength of the Wi-Fi hotspots.
    """
