"""
Function:
Establishing a cellular network channel refers to the activation of PDP context, and after a successful activation, the PDN gateway of the core network will assign an IP address to the QuecPython module.
The dataCall module contains features of configuring, obtaining, activating and deactivating PDP context, and feature of obtaining the module's IP information.
After burning the QuecPython firmware into the module, it will automatically establish a cellular network channel upon startup. If you have configured the APN, the module will use the configured APN information for establishment; otherwise, it will use the default APN.

When using a SIM card from a different operator, you should configure the APN information of the corresponding operator.
Failure to configure or incorrect configuration may result in the module's failure to register to the network, failure to establish the network channel, inability to obtain an IP address, and failure to access the Internet.
For information on configuring the APN, refer to the dataCall.setPDPContext method.

Descriptions taken from:
https://python.quectel.com/doc/API_reference/en/iotlib/dataCall.html
"""


def setPDPContext(profileID, ipType, apn, username, password, authType):
    """Configures the relevant information of the PDP context, and saves the configuration information when power is off. When establishing the channel, use the parameters configured by this method to activate the PDP context.

    For BG95 series modules, the range of profileID is 1–2 in the NB network mode.
    Only BG95 series modules support the value 3 of authType .When setting the username and password as non-empty strings, and the authType is 0, it will automatically change to 2. When setting the username and password as empty strings, and the authType is non-zero, it will automatically change to 0.
    As the first route of the LTE network is established during the registration phase, when changing the ipType of the first route, a cfun0/1 operation or a restart is required for it to take effect.
    Modules that support this method: EC100Y/EC200N/EC600N/EC600S/EC800N/EG912N/EG915N/EC600M/EC800M/EG810M/EC200A/EC200U/EC600U/EG912U/EG915U/EC600G/EC800G/EC600E/EC800E/BG95 series module.

    :param profileID: Integer type. PDP context ID. Range: 1–3. It is usually set to 1.
    :param ipType: Integer type. IP protocol type. See the table below for possible values:
    Value	Description
    0	IPv4
    1	IPv6
    2	IPv4 and IPv6
    :param apn: String type. Access Point Name. It can be null, in which case it should be written as ''. Range: 0–64. Unit: byte.
    :param username: String type. Username. It can be null, in which case it should be written as ''. Range: 0–64. Unit: byte.
    :param password: String type. Password. It can be null, in which case it should be written as ''. Range: 0–64. Unit: byte.
    :param authType: Integer type. APN authentication method. See the table below for possible values:
    Value	Description
    0	None
    1	PAP
    2	CHAP
    3	PAP and CHAP
    :return: 0 - Successful execution; -1 - Failed execution.
    """

def getPDPContext(profileID):
    """Gets the relevant information of the PDP context for the specified profileID.

    Modules that support this method: EC100Y/EC200N/EC600N/EC600S/EC800N/EG912N/EG915N/EC600M/EC800M/EG810M/EC200A/EC200U/EC600U/EG912U/EG915U/EC600G/EC800G/EC600E/EC800E/BG95 series module.

    :param profileID: Integer value. PDP context ID. Range: 1–3.
    :return: Returns -1 for failed execution and returns a tuple containing PDP context information for successful execution.
    The format of the tuple is as: (ipType, apn, username, password, authType)
    See the parameter of dataCall.setPDPContext method for the tuple parameter.
    """

def setAutoActivate(profileID, enable):
    """Sets whether the PDP context for the specified profileID is automatically activated during startup.

    If you have not called dataCall.setAutoActivate and dataCall.setAutoConnect method, then the PDP context whose profileID is 1 is automatically activated and reconnected at startup by default; otherwise, it is executed according to your configuration.
    Modules that support this method: EC100Y/EC200N/EC600N/EC600S/EC800N/EG912N/EG915N/EC600M/EC800M/EG810M/EC200A/EC200U/EC600U/EG912U/EG915U/EC600G/EC800G/EC600E/EC800E/BG95 series module.

    :param profileID: Integer value. PDP context ID. Range: 1–3.
    :param enable: Integer type. Controls whether the module automatically activates the PDP context during startup. 0 indicates disable and 1 indicates enable.
    """

def setAutoConnect(profileID, enable):
    """Enables or disables the automatic reconnection feature for the specified profileID.

    Automatic reconnection feature refers to the behavior of the module to automatically reconnect when the module disconnects from the network due to abnormal network conditions, poor signal, or other exceptional scenarios, and the network conditions return to normal.
    If you have not called dataCall.setAutoActivate and dataCall.setAutoConnect method, then the PDP context whose profileID is 1 is automatically activated and reconnected at startup by default; otherwise, it is executed according to your configuration.
    Modules that support this method: EC100Y/EC200N/EC600N/EC600S/EC800N/EG912N/EG915N/EC600M/EC800M/EG810M/EC200A/EC200U/EC600U/EG912U/EG915U/EC600G/EC800G/EC600E/EC800E/BG95 series module.

    :param profileID: Integer value. PDP context ID. Range: 1–3.
    :param enable: Integer type. Controls whether to enable automatic reconnection. 0 indicates disable and 1 indicates enable.
    """

def setDNSServer(profileID, simID, priDNS, secDNS):
    """Sets the DNS server address.

    After establishing the cellular network channel successfully, the module will automatically obtain the DNS server address, and generally it is unnecessary to reconfigure it.
    If the DNS server address automatically obtained by the module is unavailable, you can reconfigure it with this method.

    Modules that support this method:
    EC100Y/EC200N/EC600N/EC600S/EC800N/EG912N/EG915N/EC200A/EC200U/EC600U/EG912U/EG915U series module.

    :param profileID: Integer value. PDP context ID. Range: 1–3.
    :param simID: Integer type. SIM card slot number. 0 indicates SIM0; 1 indicates SIM1. Currently only 0 is supported.
    :param priDNS: String type. Primary DNS server address.
    :param secDNS: String type. Secondary DNS server address.
    :return: 0 - Successful execution; -1 - Failed execution.
    """

def setCallback(fun):
    """Registers a callback function.

    When the network status changes, such as when the network is disconnected or the reconnection is successful, this callback function will be triggered to inform the user of the network status.

    Modules that support this method:
    EC100Y/EC200N/EC600N/EC600S/EC800N/EG912N/EG915N/EC600M/EC800M/EG810M/EC200A/EC200U/EC600U/EG912U/EG915U/EC600G/EC800G/EC600E/EC800E/BG95 series module.

    :param fun: The name of the callback function. The format and parameters of the callback function is described as follows:
        def netCallback(args):
            pass
        Parameter	Type	Description
        args[0]	Integer	PDP context ID, indicating which PDP network state has changed
        args[1]	Integer	Network status. 0 means the network is disconnected and 1 means the network is connected
    :return: 0 - Successful execution; -1 - Failed execution.
    """

def activate(profileID):
    """Activates the PDP context specified by profileID.

    The PDP context is automatically activated by the module at startup, so you don't have to activate it manually.
    If you have disabled the automatic PDP context activation feature, you need to call this method to activate the PDP context.

    Modules that support this method:
    EC100Y/EC200N/EC600N/EC600S/EC800N/EG912N/EG915N/EC600M/EC800M/EG810M/EC200A/EC200U/EC600U/EG912U/EG915U/EC600G/EC800G/EC600E/EC800E/BG95 series module.

    :param profileID: Integer value. PDP context ID. Range: 1–3.
    :return: 0 - Successful execution; -1 - Failed execution.
    """

def deactivate(profileID):
    """Deactivates the PDP context specified by profileID.

    Modules that support this method:
    EC100Y/EC200N/EC600N/EC600S/EC800N/EG912N/EG915N/EC600M/EC800M/EG810M/EC200A/EC200U/EC600U/EG912U/EG915U/EC600G/EC800G/EC600E/EC800E/BG95 series module.

    :param profileID: Integer value. PDP context ID. Range: 1–3.
    :return: 0 - Successful execution; -1 - Failed execution.
    """

def getInfo(profileID, ipType):
    """Gets cellular network channel establishment information, including establishment status, IP address, DNS server address, etc.

    :param profileID: Integer value. PDP context ID. Range: 1–3.
    :param ipType: Integer type. IP protocol type. The value range is as follows:
        Value	Description
        0	IPv4
        1	IPv6
        2	IPv4 and IPv6
    :return: Returns -1 for failed execution and returns a tuple containing establishment information for successful execution. See the following description:
    ipType can be set to 0 or 1. The return value format is as follows: (profileID, ipType, [state, reconnect, addr, priDNS, secDNS])
    Parameter	Type	Description
    profileID	Integer	PDP context ID
    ipType	Integer	IP protocol type, with the following values:
    0 indicates IPv4
    1 indicates IPv6
    2 indicates IPv4 and IPv6
    state	Integer	Establishment status of IPv4 or IPv6:
    0 indicates that the establishment has not been performed or has failed
    1 indicates successful establishment
    reconnect	Integer	Reconnection flag. It is a reserved parameter and is not currently used.
    addr	String	The address of IPv4 or IPv6, depending on the input value of ipType.
    If ipType is 0, addr is IPv4
    If ipType is 1, addr is IPv6
    priDNS	String	Primary DNS server address
    secDNS	String	Secondary DNS server address
    If ipType is set to 2, the return value format is as follows:
    (profileID, ipType, [state, reconnect, ipv4Addr, priDNS, secDNS], [state, reconnect, ipv6Addr, priDNS, secDNS])
    In the returned tuple, the first list contains IPv4 channel establishment information, and the second list contains IPv6 channel establishment information.
    The return value (1, 0, [0, 0, '0.0.0.0', '0.0.0.0', '0.0.0.0']) indicates that the establishment has not been performed or has failed.
    Modules that support this method: EC100Y/EC200N/EC600N/EC600S/EC800N/EG912N/EG915N/EC600M/EC800M/EG810M/EC200A/EC200U/EC600U/EG912U/EG915U/EC600G/EC800G/EC600E/EC800E/BG95/BC25/BC95 series module.
    Since it should be compatible with the old version of dataCall.getInfo, the maximum value of the actual profileID is greater than 3, and the actual profileID that can be queried shall prevail.
    """
