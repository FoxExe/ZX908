"""
Function:
This feature is related to the network and provides interfaces of configuring and querying the information of the network mode, such as getting the network registration status and setting the network searching mode.
Note: It is recommended that you should configure the APN information of the corresponding operator when using SIM cards of different operators. If the APN information is not configured or the configuration is incorrect, the module may not register on the network.
See dataCall.setPDPContext for methods of how to configure the APN information.

Descriptions taken from:
https://python.quectel.com/doc/API_reference/en/iotlib/net.html
"""


def csqQueryPoll():
    """This method gets the signal strength.

    Note: Range of the value of signal strength: 0–31. The higher the value, the better the signal strength.

    :return: Value of CSQ signal strength - Successful execution; -1 - Failed execution; 99 - Error.
    """

def getCellInfo():
    """This method gets the information of neighbour cells.

    Note: This interface will block for 3–5 seconds when searching for cells. In areas without signals, the blocking time will be longer.

    :return: List of the information of three network modes （GSM, UMTS, LTE） - Successful execution.;
    -1 - Failed execution.
    An empty list - The information of the corresponding network mode is empty.
    ([(flag, cid, mcc, mnc, lac, arfcn, bsic, rssi)], [(flag, cid, licd, mcc, mnc, lac, uarfcn, psc, rssi)], [(flag, cid, mcc, mnc, pci, tac, earfcn, rssi, rsrq, sinr),...])
    Descriptions of GSM network mode:
    Parameter	Description
    flag	Cell type. Range: 0–3. 0: Current serving cell. 1: Neighbour cell. 2: Intra-frequency neighbour cell. 3: Inter-frequency neighbour cell.
    cid	Cell ID in GSM network. 0 indicates empty. Range: 0–65535.
    mcc	Mobile Country Code. Range: 0–999.
    Note: For EC100Y/EC600S/EC600N/EC600E/EC800E/EC200A/EC600M/EC800M series module, the value needs to be converted to hexadecimal. For example, Decimal number 1120 is 0x460 in hexadecimal in which 460 indicates MCC460. For other series modules, this value is in decimal format.
    mnc	Mobile Network Code. Range: 0–99.
    lac	Location Area Code. Range: 1–65534.
    arfcn	Absolute Radio Frequency Channel Number. Range: 0–65535.
    bsic	Base Station Identification Code. Range: 0–63.
    rssi	In GSM network, this value indicates Rx level and describes the received signal strength. 99 indicates unknown or undetectable.
    RSSI = RXLEV - 111. Unit: dBm. Range of RXLEV: 0–63. Range of RSSI: -111 to -48 dBm.
    Descriptions of UMTS network mode:
    Parameter	Description
    flag	Cell type. Range: 0–3. 0: Current serving cell. 1: Neighbour cell. 2: Intra-frequency neighbour cell. 3: Inter-frequency neighbour cell.
    cid	Cell identity in UMTS network mode. Cell identity = RNC_ID × 65536 + Cell_ID. Range of cell identity: 0x0000000–0xFFFFFFF (The cell identity is 28 bits). It means that the first two bytes of cell identity indicate RNC_ID and the last two bytes indicate Cell_ ID. Range of Cell_ID: 0–65535.
    lcid	URA ID. Range: 0–65535. 0 indicates that the information does not exist.
    mcc	Mobile Country Code. Range: 0–999.
    mnc	Mobile Network Code. Range: 0–99.
    lac	Location Area Code. Range: 1–65534.
    uarfcn	UTRA Absolute Radio Frequency Channel Number. Range: 0–65535.
    psc	Primary Scrambling Code. This parameter determines the primary scrambling code of the scanned cell. Range: 0–511.
    rssi	In UMTS network, this value indicates received signal code power (RSCP), that is CPICH/PCCPCH.
    RSSI = RSCP - 115. Unit: dBm. Range: -121 to -25 dBm.
    Descriptions of LTE network mode:
    Parameter	Description
    flag	Cell type. Range: 0–3. 0: Current serving cell. 1: Neighbour cell. 2: Intra-frequency neighbour cell. 3: Inter-frequency neighbour cell.
    cid	Cell identity, also called E-UTRAN cell identifier (ECI) in LTE network. ECI = eNodeB ID × 256 + Cell ID. Range: 0x0000000–0xFFFFFFF (The cell identity is 28 bits). The first 20 bits indicate eNodeB ID. The last 8 bits indicate LTE Cell ID.
    mcc	Mobile Country Code. Range: 0–999.
    mnc	Mobile Network Code. Range: 0–99.
    pci	Physical-layer cell identity. Range: 0–503.
    tac	Tracking Area Code. Range: 0–65535.
    earfcn	E-UTRA Absolute Radio Frequency Channel Number. Range: 0–65535.
    rssi	In LTE network, RSSI indicates all received signal strength. Range: -140 to -44. Unit: dBm.
    Note: All series modules cannot get RSSI currently but use RSRP, excluding BC25/BG95 series module.
    RSRP indicates received effective signal strength. Range: -140 to -44. Unit: dBm.
    rsrq	Reference signal receiving quality (RSRQ) of the LTE network. Range: -20 to -3.
    Note: Theoretically, RSRQ ranges from -19.5 to -3. But due to the problem of calculation method, the supported RSRQ ranges from -20 to -3.
    Currently, it is meaningful to get this parameter only for BC25/BG95/EC600E/EC800E series module. This parameter is meaningless for other modules.
    """

def getConfig():
    """This method gets the current network mode and roaming configuration.

    BC25 series module does not support this method.
    BG95-M1 series module only supports CAT-M network mode.
    BG95-M2 series module only supports two network modes: CAT-M and CATNB.
    BG95-M3/M8 series module supports three network modes: CAT-M, CATNB and GSM.

    :return: -1 - Failed execution; A tuple containing the current preferred network mode and roaming enabling status - Successful execution.
    """

def setConfig(mode, roaming):
    """This method sets the network mode and roaming configuration.

    roaming is an optional parameter, which can be omitted for unsupported module models.
    BC25 series module does not support this method.
    EC200U/EC600U/EG915U/EG912U series module does not support the configuration of roaming parameters and only supports network modes GSM, GSM_LTE (automatic) and GSM_LTE (LTE preferred).
    EC600E/EC800E series module only supports LTE network mode.

    :param mode: Integer type. Network mode. See the above table of network modes for details.
    :param roaming: Integer type. Roaming switch. Optional parameter (0: Disable, 1: enable).
    :return: 0 - Successful execution; -1 - Failed execution.
    """

def getNetMode():
    """This method gets the network configuration mode.

    :return: -1 - Failed execution; A tuple (selection_mode, mcc, mnc, act) - Successful execution
    Parameter	Type	Description
    selection_mode	Integer	Method. 0 - Automatically. 1 - Manually.
    mcc	String	Mobile Country Code.
    mnc	String	Mobile Network Code.
    act	Integer	ACT mode of the preferred network.
    Enumeration values of ACT modes:
    Value	ACT Mode
    0	GSM
    1	COMPACT
    2	UTRAN
    3	GSM wEGPRS
    4	UTRAN wHSDPA
    5	UTRAN wHSUPA
    6	UTRAN wHSDPA HSUPA
    7	E UTRAN
    8	UTRAN HSPAP
    9	E UTRAN CA
    10	NONE
    Enumeration values of ACT modes of BG95 series module:
    Value	ACT Mode
    0	GSM
    1	GSM COMPACT
    2	UTRAN
    3	GSM wEGPRS
    4	UTRAN wHSDPA
    5	UTRAN wHSUPA
    6	UTRAN wHSDPA HSUPA
    7	E_UTRAN
    8	UTRAN HSPAP
    9	E_UTRAN_CA
    10	E_UTRAN_NBIOT
    11	E_UTRAN_EMTC
    12	NONE
    """

def getSignal(sinrEnable=0):
    """This method gets the detailed signal strength.

    sinrEnable is an optional parameter, which can be omitted for the unsupported modules. If you do not enter this parameter, sinr won't be got by default.
    All Quectel series modules support to get sinr, excluding BC25 series module.

    :param sinrEnable: Integer type. Optional parameter. Enable or disable to get SINR.
    Value	Description
    0	Disable to get SINR
    1	Enable to get SINR
    :return: -1 - Failed execution; A tuple containing (GW, LTE) - Successful execution
    ([rssi, bitErrorRate, rscp, ecno], [rssi, rsrp, rsrq, cqi, sinr])
    Descriptions of GSM/WCDMA :
    Parameter	Description
    rssi	In GSM and WCDMA network, this value indicates Rx level and describes the received signal strength. 99 indicates unknown or undetectable.
    RSSI = RXLEV - 111. Range of RXLEV: 0–63. Unit: dBm.
    bitErrorRate	Bit error rate. Range: 0–7. 99 indicates unknown or undetectable.
    rscp	Receive Signal Channel Power. Range: -121 to -25 dBm. 255 indicates unknown or undetectable.
    ecno	Range: -24–0. 255 indicates unknown or undetectable.
    Descriptions of LTE :
    Parameter	Description
    rssi	Received Signal Strength Indicator. Range: -140 to -44 dBm. 99 indicates unknown or undetectable.
    rsrp	Reference Signal Receiving Power. Range: -140 to -44 dBm. 99 indicates unknown or undetectable.
    rsrq	Reference Signal Receiving Quality. Range: -20 to -3 dBm. The higher the value, the better the reference signal received quality. 255 indicates unknown or undetectable.
    cqi	    Channel Quality Indication. 255 indicates unknown or undetectable.
    sinr	Signal to interference plus Noise Ratio. Range: -10–40 dBm. 255 indicates unknown or undetectable.
    """

def nitzTime():
    """This method gets the current base station time, which is the time issued by the base station when the module boots and registers on the network successfully.

    :return: -1 - Failed execution; A tuple (date, abs_time, leap_sec) containing the base station time and corresponding timestamps and leap seconds (0 indicates that the current base station time is unavailable.) - Successful execution
    Parameter	Type	Description
    date	String	Base time. The part of the time zone varies with module models. See the example below for details.
    Please use setTimeZone(offset) and getTimeZone() of utime feature if you need to set and get the time zone.
    The unit of these two interfaces is hour for different modules. See utime for details.
    abs_time	Integer	Absolute seconds of the base station time.
    leap_sec	Integer	Leap seconds.
    """

def operatorName():
    """This method gets the operator information of the current network registration.

    :return: -1 - Failed execution; A tuple (long_eons, short_eons, mcc, mnc) containing the operator information of the current network registration - Successful execution
    Parameter	Type	Description
    long_eons	String	Operator's full name.
    short_eons	String	Operator's name abbreviation.
    mcc	String	Mobile Country Code
    mnc	String	Mobile Network Code
    """

def getState():
    """This interface gets the network registration information.

    :return: -1 - Failed execution; A tuple ([voice_state, voice_lac, voice_cid, voice_rat, voice_reject_cause, voice_psc], [data_state, data_lac, data_cid, data_rat, data_reject_cause, data_psc]) containing the information of the phone and network registration - Successful execution
    """

def getCi():
    """This method gets neighbour cells. The result gotten by this interface is the collection of cell IDs in the result gotten by net.getCellInfo().

    :return: An array [id, ……, id] containing cell IDs. List type. The number of array members is not fixed, and different locations, signal strength, and other factors may lead to different results. - Successful execution; -1 - Failed execution.
    """

def getServingCi():
    """This method gets the serving cell ID. The result gotten by this interface is the collection of cell IDs in the result gotten by net.getCellInfo().

    :return: Serving cell ID - Successful execution; -1 - Failed execution.
    """

def getMnc():
    """This method gets MNC of the neighbour cell ID.

    The result gotten by this interface is the collection of MNCs in the result gotten by net.getCellInfo().

    :return: An array [mnc, ……, mnc] containing mnc of cells. List type. The number of array members is not fixed, and different locations, signal strength, and other factors may lead to different results. - Successful execution; -1 - Failed execution.
    """

def getServingMnc():
    """This method gets MNC of the serving cell.

    The result gotten by this interface is the collection of MNCs in the result gotten by net.getCellInfo().

    :return: mnc of the serving cell - Successful execution; -1 - Failed execution.
    """

def getMcc():
    """This method gets MCCs of the neighbour cells.

    The result gotten by this interface is the collection of MCCs in the result gotten by net.getCellInfo().

    For EC100Y/EC600S/EC600N/EC600E/EC800E/EC200A/EC600M/EC800M series module, the value needs to be converted to hexadecimal. For example, Decimal number 1120 is 0x460 in hexadecimal in which 460 indicates MCC460. For other series modules, this value is in decimal format.

    :return: An array [mnc, ……, mnc] containing mnc of cells. List type. The number of array members is not fixed, and different locations, signal strength, and other factors may lead to different results. - Successful execution; -1 - Failed execution.
    """

def getServingMcc():
    """This method gets MCC of the serving cell.

    The result gotten by this interface is the collection of MCCs in the result gotten by net.getCellInfo().

    For EC100Y/EC600S/EC600N/EC600E/EC800E/EC200A/EC600M/EC800M series module, the value needs to be converted to hexadecimal. For example, Decimal number 1120 is 0x460 in hexadecimal in which 460 indicates MCC460. For other series modules, this value is in decimal format.

    :return: mcc of the serving cell - Successful execution; -1 - Failed execution.
    """

def getLac():
    """This method gets LACs of the neighbour cells.

    The result gotten by this interface is the collection of LACs in the result gotten by net.getCellInfo().

    :return: An array [lac, ……, lac] containing lac of cells. List type. The number of array members is not fixed, and different locations, signal strength, and other factors may lead to different results. - Successful execution; -1 - Failed execution.
    """

def getServingLac():
    """This method gets LACs of the serving cells.

    The result gotten by this interface is the collection of LACs in the result gotten by net.getCellInfo().

    :return: lac of the serving cell - Successful execution; -1 - Failed execution.
    """

def getModemFun():
    """This method gets the current work mode.

    :return: The current work mode of the module - Successful execution; -1 - Failed execution.
    Mode	Description
    0	Minimum functionality. In this mode, the entire radio frequency network protocol stack is completely closed, and the power supply to the SIM card is stopped.
    1	Full functionality (default). In this mode, the device can send and receive RF signals.
    4	Disable UE from both transmitting and receiving RF signals.
    """

def setModemFun(fun, rst=0):
    """This method sets the current work mode of the module.

    :param fun: Integer type. Work mode of the module.
    Mode	Description
    0	Minimum functionality. In this mode, the entire radio frequency network protocol stack is completely closed, and the power supply to the SIM card is stopped.
    1	Full functionality (default). In this mode, the device can send and receive RF signals.
    4	Disable UE from both transmitting and receiving RF signals.
    :param rst: Integer type. Reboot flag. Optional parameter.
    Value	Description
    0	Do not reboot the module after setting the current work mode (default).
    1	Reboot the module after setting the current work mode.
    :return: 0 - Successful execution; -1 - Failed execution.
    """

def setBand(netRat, gsmBand, bandTuple):
    """This method sets the required band, that is, lock the band specified by the user if the module supports this method.

    Currently, BG95 series module/EG912N-ENAA module supports this method.
    BG95 series module does not support the band of LTE network.
    EG912N-ENAA module only supports the band of GSM network and LTE network.

    :param netRat: Integer type. Network mode. It indicates the kind of network mode whose band is to be set.
    :param gsmBand: Integer type. The band value of GSM network. See the band value comparison table above.
    :param bandTuple:  The band value of other network modes excluding GSM network and it is a tuple containing 4 elements (band_hh, band_hl, band_lh, band_ll), each of which cannot exceed 4 bytes.
    :return: 0 - Successful execution; -1 - Failed execution.
    """

def getBand(netRat):
    """This method gets the band value in the current network mode.

    Currently, BG95 series module/EG912N-ENAA module supports this method.
    BG95 series module does not support the band of LTE network.
    EG912N-ENAA module only supports the band of GSM network and LTE network.

    :param netRat: Integer type. Network mode. It indicates that the band of which network mode you want to set.
    RAT Value	Description
    0	GSM network
    1	LTE network
    2	Cat M network
    3	NB-IoT network
    :return: Band value in hexadecimal.
    """

def bandRst():
    """This method restores the initial set value of the band.

    Note: EG912N-ENAA series module supports this method.

    :return: 0 - Successful execution; -1 - Failed execution.
    """
