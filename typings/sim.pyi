"""
Function:
This feature provides you with the SIM Card APIs, such as the methods of getting SIM card status, ICCID, IMSI and the phone number.
The IMSI, ICCID, and phone number can be gotten only when the SIM card status is 1. You can call sim.getstatus() to get the current SIM card status.

Descriptions taken from:
https://python.quectel.com/doc/API_reference/en/iotlib/sim.html
"""

def genericAccess(simId, cmd):
    """Accesses generic SIM features to send CSIM commands and interact with SIM cards.

    Only EC100Y/EC200N/EC600N/EC600S/EC800N/EG912N/EG915N series module supports this method.

    :param simId: Integer type. SIM card slot ID. 0 - SIM card 0. 1- SIM card 1. Only 0 is supported now.
    :param cmd: String type. The command passed by the mobile terminal to the SIM in the format described in GSM 51.011.
    :return: A tuple (len，data) - Successful execution
    len - Integer type. Length of data.
    data - String type. The data content returned.
    -1 - Failed execution

    """

def getImsi():
    """Gets the IMSI number of the SIM card.

    :return: IMSI - Successful execution; -1 - Failed execution
    """

def getIccid():
    """Gets the ICCID number of the SIM card.

    :return: ICCID - Successful execution;-1 - Failed execution
    """

def getPhoneNumber():
    """Gets the phone number of the SIM card. The phone number of the SIM card must be written into the module first.

    BC25 series module does not support this method.

    :return: Phone number - Successful execution;-1 - Failed execution
    """

def getStatus():
    """Gets the current SIM card status.

    :return: String type. SIM card status codes, as described in details below.
    Code	Description
    0	The SIM card does not exist/has been removed.
    1	The SIM card is ready.
    2	The SIM card has been blocked and waiting for CHV1 password.
    3	The SIM card has been blocked and needs to be unblocked with CHV1 password.
    4	The SIM card has been blocked due to failed SIM/USIM personalized check.
    5	The SIM card is blocked due to an incorrect PCK. An MEP unblocking password is required.
    6	Expecting key for hidden phone book entries
    7	Expecting code to unblock the hidden key
    8	The SIM card has been blocked and waiting for CHV2 password.
    9	The SIM card has been blocked and needs to be unblocked with CHV2 password.
    10	The SIM card has been blocked due to failed network personalization check.
    11	The SIM card is blocked due to an incorrect NCK. An MEP unblocking password is required.
    12	The SIM card has been blocked due to failed personalization check of network lock.
    13	The SIM card is blocked due to an incorrect NSCK. An MEP unblocking password is required.
    14	The SIM card has been blocked due to failed personalization check of the service provider.
    15	The SIM card is blocked due to an incorrect SPCK. An MEP unblocking password is required.
    16	The SIM card has been blocked due to failed enterprise personalization check.
    17	The SIM card is blocked due to an incorrect CCK. An MEP unblocking password is required.
    18	The SIM card is being initialized and waiting for completion.
    19	The SIM card is blocked for the following six reasons.
        1) Use of CHV1 is blocked.
        2) Use of CHV2 is blocked.
        3) Use of the universal PIN is blocked.
        4) Use of code to unblock the CHV1 is blocked.
        5) Use of code to unblock the CHV2 is blocked.
        6) Use of code to unblock the universal PIN is blocked.
    20	The SIM card is invalid.
    21	Unknown status.
    """

def enablePin(pin):
    """Enables PIN verification.

    Once this method is called to enable the PIN verification, you need to enter the correct PIN code for verification.
    Only when the PIN code is verified successfully will the SIM card can be used normally.
    Please note that you have at most 3 attempts.
    The SIM card will be locked and must be unblocked with the PUK code after three consecutive failures.

    :param pin: String type. PIN code. Default value: ‘1234’. The value contains a maximum of 15 digits.
    :return: 0 - Successful execution;-1 - Failed execution
    """

def disablePin(pin):
    """Disables PIN code verification.

    :param pin: String type. PIN code. Default value: ‘1234’. The value contains a maximum of 15 digits.
    :return: 0 - Successful execution;-1 - Failed execution
    """

def verifyPin(pin):
    """Verifies PIN code.

    After the PIN code verification is enabled, if you need to use the SIM card, you can call this method to temporarily make the SIM card work normally, and this method needs to be called again for verification next time when the module is powered on (Or you can call sim.disablePin(pin) to disable the PIN verification, then the PIN verification will not be required when the module is powered on again).

    :param pin: String type. PIN code. Default value: ‘1234’. Length: up to 15 digits.
    :return: 0 - Successful execution;-1 - Failed execution
    """

def changePin(oldPin, newPin):
    """Changes the PIN code

    :param oldPin: String type. The old PIN code, with a maximum length of 15 digits.
    :param newPin: String type. The new PIN code, with a maximum length of 15 digits.
    :return:0 - Successful execution;-1 - Failed execution
    """

def unblockPin(puk, newPin):
    """Unblocks the SIM card.

    When you enter incorrect PIN codes three times, you need to enter the PUK code to unblock the SIM card. If incorrect PUK codes are entered ten times, the SIM card will be permanently locked and automatically scrapped.

    :param puk: String type. PUK code. Length: 8 to 15 digits.
    :param newPin: String type. New PIN code. Length: up to 15 digits.
    :return:0 - Successful execution;-1 - Failed execution
    """

def readPhonebook(storage, start, end, username):
    """Reads the phone book to get one or more phone number records from the phone book at the specified storage location.

    EC100Y/EC200N/EC600N/EC600S/EC800N/EG912N/EG915N/EC600MCNLE/EC600MCNLA/EC800MCNLA/EC800MCNLE/EC800MCNGA/EG810M/EC200A series module supports this method.
    When you match a phone number record by username, you do not need to enter a full word. As long as there is an existing record in the phone book whose name starts with the username, the name will be matched with the phone number.

    :param storage: Integer type. Storage location of the phone numbers, as described below.
    Value	Description
    0	DC
    1	EN
    2	FD
    3	LD
    4	MC
    5	ME
    6	MT
    7	ON
    8	RC
    9	SM
    10	AP
    11	MBDN
    12	MN
    13	SDN
    14	ICI
    15	OCI
    :param start: Integer type. The start number of the phone number record to be read. start equaling 0 indicates that no number is used to obtain the phone number. start must be less than or equal to end.
    :param end: Integer type. The end number of the phone number record to be read. The condition that must be met: end - start <= 20.
    :param username: String type. The username of a phone number. This parameter is valid when start equals 0. Chinese characters are not supported currently. Length: up to 30 bytes.
    :return: A tuple (record_number, [(index, username, phone_number), ... , (index, username, phone_number)]) - Successful execution;-1 - Failed execution
    The parameters are described below:
    Parameter	Type	Description
    record_number	Integer	The number of phone number records read.
    index	Integer	Index of the number in the phone book.
    username	String	Username of the phone number.
    phone_number	String	Phone number.
    """

def writePhonebook(storage, index, username, number):
    """Writes phone book, that is, write a phone record to the specified storage location.

    EC100Y/EC200N/EC600N/EC600S/EC800N/EG912N/EG915N/EC600MCNLE/EC600MCNLA/EC800MCNLA/EC800MCNLE/EC800MCNGA/EG810M/EC200A series module supports this method.

    :param storage: Integer type. Storage location of the phone numbers. For details, see storage of sim.readPhonebook.
    :param index: Integer type. Index of the number in the phone book. Range: 1 – 500.
    :param username: String type. The username of a phone number. Chinese characters are not supported currently. Length: up to 30 bytes.
    :param number: String type. Phone number. Length: up to 20 bytes.
    :return: 0 - Successful execution;-1 - Failed execution
    """

def setSimDet(switch, triggerLevel):
    """Sets the hot-swap-related features of the SIM card.

    The EC100Y/EC200N/EC600S/EC600N/EG912N/EC600M/EC800M/EC200A series modules support SIM card hot-swapping. Configurations take effect immediately and the related settings have power-off preservation.
    In EC600N series module, EC600NCN_AA module does not support this feature.
    In EC200A series module, EC200ACN_GA module does not support this feature.
    The EC600G/EC800G/EC200U/EC600U/EG912U/EG915U series modules support SIM card hot-swapping. Configurations take effect immediately, and the related settings have power-off preservation. (Firmware versions after August 23, 2023, support power-off preservation, while earlier versions do not.)
    The EC600E series/EC800E series modules support SIM card hot-swapping. Configurations take effect immediately, and the related settings have power-off preservation. (Firmware versions after September 12, 2023, support power-off preservation, while earlier versions do not.)
    The BG95M1/BG95M2/BG95M3/BG95M6/BG95M8 series modules support SIM card hot-swapping. Configurations require a restart to take effect, and they support the power-off preservation feature.

    :param switch: Integer type. Enable or disable the hot swap feature of the SIM card. 0 - Disable; 1 - Enable
    :param triggerLevel:  Integer type. This parameter is set according to the actual level of the SIM card. If the present level is high when the SIM card is inserted, this parameter should be set to 1. If the present level is low, this parameter should be set to 0.
    :return: 0 - Successful execution; -1 - Failed execution
    """

def getSimDet():
    """Gets the hot-swap-related settings of the SIM card.

    The EC100Y/EC200N/EC600S/EC600N/EG912N/EC600M/EC800M/EC200A series modules support SIM card hot-swapping. Configurations take effect immediately and the related settings have power-off preservation.
    In EC600N series module, EC600NCN_AA module does not support this feature.
    In EC200A series module, EC200ACN_GA module does not support this feature.
    The EC600G/EC800G/EC200U/EC600U/EG912U/EG915U series modules support SIM card hot-swapping. Configurations take effect immediately, and the related settings have power-off preservation. (Firmware versions after August 23, 2023, support power-off preservation, while earlier versions do not.)
    The EC600E series/EC800E series modules support SIM card hot-swapping. Configurations take effect immediately, and the related settings have power-off preservation. (Firmware versions after September 12, 2023, support power-off preservation, while earlier versions do not.)
    The BG95M1/BG95M2/BG95M3/BG95M6/BG95M8 series modules support SIM card hot-swapping. Configurations require a restart to take effect, and they support the power-off preservation feature.

    :return: A tuple (detenable, insertlevel) - Successful execution.The parameters are described below. -1 - Failed execution
    Parameter	Type	Description
    detenable	Integer	Enable or disable the hot swap feature of the SIM card. 0 - Disable; 1 - Enable.
    insertlevel	Integer	High level or low level (0/1).
    """

def getCurSimid():
    """Gets the SIM card slot ID of the current SIM card.

    The modules that support this method are as follows:
    EC600MCN_CC/EC600MCN_LA/EC600MCN_LC/EC600MCN_LE/EC600MCN_LF/EC800MCN_LA/EC800MCN_LC/EC800MCN_LE/EC600ECN_LD/EC800ECN_LD/EG912UGL_AA

    :return: simId - Successful execution; 0 - SIM1; 1 - SIM2; -1 - Failed execution
    """

def switchCard(simId):
    """Switches the SIM card.

    The modules that support this method are as follows:
    EC600MCN_CC/EC600MCN_LA/EC600MCN_LC/EC600MCN_LE/EC600MCN_LF/EC800MCN_LA/EC800MCN_LC/EC800MCN_LE/EC600ECN_LD/EC800ECN_LD/EG912UGL_AA

    :param simId:  Integer type. SIM card slot ID. 0 - SIM1; 1 - SIM2
    :return:0 - Successful execution; -1 - Failed execution
    """

def setCallback(usrFun):
    """Registers the callback function of hot swap features.When the hot-swap feature is enabled, the callback function registered by this method will be called when the SIM card is inserted or removed.

    The EC100Y/EC200N/EC600S/EC600N/EG912N/EC600M/EC800M/EC200A series modules support SIM card hot-swapping. Configurations take effect immediately and the related settings have power-off preservation.
    In EC600N series module, EC600NCN_AA module does not support this feature.
    In EC200A series module, EC200ACN_GA module does not support this feature.
    The EC600G/EC800G/EC200U/EC600U/EG912U/EG915U series modules support SIM card hot-swapping. Configurations take effect immediately, and the related settings have power-off preservation. (Firmware versions after August 23, 2023, support power-off preservation, while earlier versions do not.)
    The EC600E series/EC800E series modules support SIM card hot-swapping. Configurations take effect immediately, but they do not support the power-off preservation feature.
    The BG95M1/BG95M2/BG95M3/BG95M6/BG95M8 series modules support SIM card hot-swapping. Configurations require a restart to take effect, and they support the power-off preservation feature.

    :param usrFun: Callback function name. The callback function format and parameters are described below.
        def usrFun(args):
            pass
        Parameter	Type	Description
        args	Integer	Current status of The SIM card.
        1 - The SIM card is inserted.
        2 - The SIM card is removed.
    :return: 0 - Successful execution; -1 - Failed execution
    """

def setSwitchcardCallback(usrFun):
    """Registers the callback function of SIM card switch status to respond to the SIM card switch operation.

    The modules that support this method are as follows:
    EC600MCN_CC/EC600MCN_LA/EC600MCN_LC/EC600MCN_LE/EC600MCN_LF/EC800MCN_LA/EC800MCN_LC/EC800MCN_LE/EC600ECN_LD/EC800ECN_LD/EG912UGL_AA
    Note:
    1. The target SIM card does not exist or is in an abnormal status.
    2. The target SIM card is the current SIM card.
    When the two situations mentioned above occur, -1 will be returned when sim.switchCard is called, and the callback function registered by this method will not be called.

    :param usrFun: Callback function name. The callback function format and parameters are described below.
        def usrFun(args):
            pass
        Parameter	Type	Description
        args	Integer	The result of SIM switch.
        7 - Successful switch
        8 - Failed switch
    :return: 0 - Successful execution; -1 - Failed execution
    """
