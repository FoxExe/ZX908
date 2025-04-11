"""
Function:
This feature provides voice call APIs.
The modules supporting voice call are listed below.
    EC100Y series: EC100YCN_AA
    EC200N series: EC200NCN_AA/EC200NCN_AC/EC200NCN_LA
    EC600N series: EC600NCN_AA/EC600NCN_LC/EC600NCN_LD/EC600NCN_LF
    EC600S series: EC600SCN_LA
    EG912N series: EG912NEN_AA
    EG915N series: EG915NEU_AG
    EC200A series: EC200AAU_HA/EC200ACN_DA/EC200ACN_HA/EC200ACN_LA/EC200AEU_HA
    EC200U series: EC200UAU_AB/EC200UCN_AA/EC200UEU_AA/EC200UEU_AB
    EC600U series: EC600CEU_AB
    EG912U series: EG912UGL_AA
    EG915U series: EG915UEU_AB/EG915ULA_AB
BC25/EC600G/EC800G/BG95 series module does not support voice call.
For other modules, a custom version is required to support voice call.

Descriptions taken from:
https://python.quectel.com/doc/API_reference/en/iotlib/voiceCall.html
"""

def setAutoAnswer(seconds):
    """Sets automatic answering time of a voice call.

    :param seconds: Integer type. Automatic answering time of a voice call. Range: 0–255. Unit: s.
    :return:0 - Successful execution; -1 - Failed execution
    """

def callStart(phonenum):
    """Dials a voice call.

    :param phonenum: String type. Phone number of the recipient.
    :return:0 - Successful execution; -1 - Failed execution
    """

def callAnswer():
    """Answers a voice call.

    :return:0 - Successful execution; -1 - Failed execution
    """

def callEnd():
    """Ends a voice call.

    :return:0 - Successful execution; -1 - Failed execution
    """

def setCallback(voicecallFun):
    """Registers the callback function of different voice call statuses.

    :param voicecallFun: Callback function name.
    :return: 0 - Successful execution; -1 - Failed execution
    """

def setAutoCancel(enable):
    """Enables auto hang-up when receiving calls.

    EC200AAU_HA/EC200ACN_DA/EC200ACN_HA/EC200ACN_LA/EC200AEU_HA series module supports this method.

    :param enable: Enable or disable auto hang-up when receiving calls.0 -Disable (default); 1 - Enable.
    :return: 0 - Successful execution; -1 - Failed execution.
    """

def getAutoCancelStatus():
    """Gets the enablement status of auto hang-up.

    EC200AAU_HA/EC200ACN_DA/EC200ACN_HA/EC200ACN_LA/EC200AEU_HA series module supports this method.

    :return: 0: Auto hang-up is disabled; 1: Auto hang-up is enabled
    """

def startDtmf(dtmf, duration):
    """Sets DTMF tone.

    This method takes effect only during a voice call.

    :param dtmf: String type. DTMF symbols. Valid symbols:0-9, A, B, C, D, * and #. Maximum number of characters: 32.
    :param duration: Integer type. Duration. Range: 100–1000. Unit: ms.
    :return: 0 - Successful execution; -1 - Failed execution
    """

def dtmfDetEnable(enable):
    """Enables the feature of DTMF detection. DTMF detection is disabled by default.

    EC600N/EC600S/EC800N/EG912N/EG915N series module supports this method.

    :param enable: Integer type. Enable or disable DTMF detection.0 - Disable DTMF detection; 1 - Enable DTMF detection.
    :return: 0 - Successful execution; -1 - Failed execution
    """

def dtmfSetCb(dtmfFun):
    """Registers the callback function of DTMF detection.

    EC600N/EC600S/EC800N/EG912N/EG915N series module supports this method.

    :param dtmfFun: Callback function name. The callback function format and parameters are described below.
        def dtmfFun(args):
            pass
        Parameter	Type	Description
        args	String	DTMF characters entered by the peer end.
    :return:0 - Successful execution; -1 - Failed execution.
    """

def setFw(reason, fwmode, phonenum):
    """Sets up call forwarding.

    :param reason: Integer type. Call forwarding conditions, as described below.
    Value	Description
    0	Unconditional
    1	Busy
    2	No reply
    3	Not reachable
    :param fwmode: Integer type. Call forwarding operations, as described below.
    Value	Description
    0	Deactivate call forwarding.
    1	Activate call forwarding.
    2	Query call forwarding status.
    3	Register call forwarding.
    4	Erase call forwarding.
    :param phonenum: String type. The number to which calls are forwarded.
    :return: 0 - Successful execution; -1 - Failed execution.
    """

def setChannel(device):
    """Sets the voice output channel during a call. Default value: 0 (handset).

    :param device: Integer type. Output channel, as described below.
    Value	Description
    0	Handset
    1	Headset
    2	Loudspeaker
    :return: 0 - Successful execution; -1 - Failed execution.
    """

def getVolume():
    """Gets the current call volume.

    :return: Integer type. Volume.
    """

def setVolume(volume):
    """Sets call volume.

    :param volume: Integer type. Volume. Range: 0–11. The higher the value, the higher the volume.
    :return: 0 - Successful execution; -1 - Failed execution
    """

def setAutoRecord(enable, recordType, recordMode, filename):
    """Enables automatic recording. Automatic recording is disabled by default. The automatic recording must be enabled before the call.

    For EC200U/EC600U/EG912U/EG915U series modules, the recordMode parameter currently only supports the value 2.
    QuecPython currently does not support automatic creation of subdirectories when creating files.
    For example, filename is 'U:/record/test.amr', if there is no 'record' directory in the usr directory, the user needs to use uos.mkdir('/usr/record') to create a 'record' directory .

    :param enable: Integer type. Enable or disable automatic recording. 0 - Disable; 1 - Enable.
    :param recordType: Integer type. Recording file type, as described below.
    Value	Description
    0	AMR
    1	WAV
    :param recordMode: Integer type. Mode, as described below.
    alue	Description
    0	The recording is the audio stream of the downlink channel.
    1	The recording is the audio stream of the uplink channel.
    2	The recording is a mixed audio stream of uplink and downlink channels.
    :param filename: String type. The desired file name, which must contain the full path.
    :return: 0 - Successful execution; -1 - Failed execution; "NOT SUPPORT" - The interface is not supported.
    """

def startRecord(recordType, recordMode, filename):
    """Starts recording the call.

    For EC200U/EC600U/EG912U/EG915U series modules, the recordMode parameter currently only supports the value 2.
    QuecPython currently does not support automatic creation of subdirectories when creating files.
    For example, filename is 'U:/record/test.amr', if there is no 'record' directory in the usr directory, the user needs to use uos.mkdir('/usr/record') to create a 'record' directory .

    :param recordType: Integer type. Recording file type, as described below.
    Value	Description
    0	AMR
    1	WAV
    :param recordMode: Integer type. Mode, as described below.
    Value	Description
    0	The recording is the audio stream of the downlink channel.
    1	The recording is the audio stream of the uplink channel.
    2	The recording is a mixed audio stream of uplink and downlink channels.
    :param filename: String type. The desired file name, which must contain the full path.
    :return: 0 - Successful execution; -1 - Failed execution; "NOT SUPPORT" - The interface is not supported.
    """

def stopRecord():
    """Stops recording the call.

    :return: 0 - Successful execution; -1 - Failed execution; "NOT SUPPORT" - The interface is not supported.
    """

def readRecordStream(readBuf, bufLen):
    """Reads recording data stream.

    The first packet of data in the recording stream is the header of the file in the corresponding format.
    The first packet of recording streams in WAV format does not contain the file size.
    You need to calculate the file size after the recording is complete.

    :param readBuf: Buffer used to save the data read.
    :param bufLen: Length of the string to be read, which cannot be longer than the data length requested by readBuf.
    :return: Length of the data read - Successful execution; -1 - Failed execution
    """

def startRecordStream(recordType, recordMode, callbackFun):
    """Starts recording the call in stream format.

    The first packet of data in the recording stream is the header of the file in the corresponding format.
    The first packet of recording streams in WAV format does not contain the file size. You need to calculate the file size after the recording is completed.

    :param recordType: Integer type. Recording file type, as described below.
    Value	Description
    0	AMR
    1	WAV
    :param recordMode: Integer type. Mode, as described below.
    Value	Description
    0	RX
    1	TX
    2	MIX
    :param callbackFun: Callback function name. The callback function format and parameters are described below.
        def recordStreamCallback(args):
            pass
        Parameter	Type	Description
        args[0]	String	Recording data stream
        args[1]	Integer	Length of the recording data stream.
        args[2]	Integer	Recording status
        -1: Recording error
        0: Start recording
        1: Return recording data
        2: Stop recording
        3: Recording ends
        4: No remaining space.
    :return: 0 - Successful execution; -1 - Failed execution; "NOT SUPPORT" - The interface is not supported.
    """
