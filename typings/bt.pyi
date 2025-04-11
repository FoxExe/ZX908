"""
Function:
Classic Bluetooth
The bt module provides Classic Bluetooth related features, including HFP, A2DP, AVRCP and SPP.
Currently, only EC200U/EC600U/EG915U/EG912U series module supports bt feature.

Descriptions taken from:
https://python.quectel.com/doc/API_reference/en/btlib/bt.html
"""


def init(user_cb):
    """Initializes the Bluetooth and registers a callback function.

    :param user_cb:Function type. Callback function. The meaning of the callback function parameters:
        args[0] is fixed to represent event_id;
        args[1] is fixed to represent the status, 0 indicating successful execution and non-0 indicating failed execution. The number of callback function parameters is not fixed at two, but depends on the first parameter args[0]. The following table lists the number of parameters and explanations for different event IDs.
    event_id	Parameter Number	Description
    0	2	args[0]: event_id. BT/BLE start event.
            args[1]: status. The operation status. 0 - successful operation; other values - failed operation.
    1	2	args[0]: event_id. BT/BLE stop event.
            args[1]: status. The operation status. 0 - successful operation; other values - failed operation.
    6	6	args[0]: event_id. BT inquiry event.
            args[1]: status. The operation status. 0 - successful operation; other values - failed operation.
            args[2]: rssi. Signal strength.
            args[3]: device_class.
            args[4]: device_name. Device name. String type.
            args[5]: addr. The MAC address of the discovered Bluetooth device.
    7	3	args[0]: event_id. BT inquiry end event.
            args[1]: status. The operation status. 0 - successful operation; other values - failed operation.
            args[2]: end_status. 0 - End normally, 8 - End forcefully.
    14	4	args[0]: event_id. BT SPP receive event.
            args[1]: status. The operation status. 0 - successful operation; other values - failed operation.
            args[2]: data_len. The length of the received data.
            args[3]: data. The received data in bytearray type.
    40	4	args[0]: event_id. BT HFP connect event.
            args[1]: status. The operation status. 0 - successful operation; other values - failed operation.
            args[2]: hfp_connect_status. HFP connection status.
                0 - Disconnected
                1 - Connecting
                2 - Connected
                3 - Disconnecting
            args[3]: addr. The address of the BT master in bytearray type.
    41	4	args[0]: event_id. BT HFP disconnect event.
            args[1]: status. The operation status. 0 - successful operation; other values - failed operation.
            args[2]: hfp_connect_status. HFP connection status.
                0 - Disconnected
                1 - Connecting
                2 - Connected
                3 - Disconnecting
            args[3]: addr. The address of the BT master in bytearray type.
    42	4	args[0]: event_id. BT HFP call status event.
            args[1]: status. The operation status. 0 - successful operation; other values - failed operation.
            args[2]: hfp_call_status. HFP call status.
                0 - There are currently no calls in progress
                1 - There is currently at least one call in progress
            args[3]: addr. The address of the BT master in bytearray type.
    43	4	args[0]: event_id. BT HFP call setup status event.
            args[1]: status. The operation status. 0 - successful operation; other values - failed operation.
            args[2]: hfp_call_setup_status. HFP call setup status.
                0 - There are no call to be connected
                1 - There is an incoming call that has not yet been connected
                2 - There is an outgoing call that has not yet been connected
                3 - The other end of the Bluetooth connection for an outgoing call is ringing
            args[3]: addr. The address of the BT master in bytearray type.
    44	4	args[0]: event_id. BT HFP network status event.
            args[1]: status. The operation status. 0 - successful operation; other values - failed operation.
            args[2]: hfp_network_status. AG network status.
                0 - The network is not available
                1 - The network is normal
            args[3]: addr. The address of the BT master in bytearray type.
    45	4	args[0]: event_id. BT HFP network signal event.
            args[1]: status. The operation status. 0 - successful operation; other values - failed operation.
            args[2]: hfp_network_signal. AG signal. Range: 0–5.
            args[3]: addr. The address of the BT master in bytearray type.
    46	4	args[0]: event_id. BT HFP battery level event.
            args[1]: status. The operation status. 0 - successful operation; other values - failed operation.
            args[2]: hfp_battery_level. The AG battery level. Range: 0–5.
            args[3]: addr. The address of the BT master in bytearray type.
    47	4	args[0]: event_id. BT HFP call held status event.
            args[1]: status. The operation status. 0 - successful operation; other values - failed operation.
            args[2]: hfp_call_held_status. HFP call held status.
                0 - There is no call on hold.
                1 - The call is held and either paused or there is an active call/hold call switching.
                2 - The call is held and there is no active call
            args[3]: addr. The address of the BT master in bytearray type.
    48	4	args[0]: event_id. BT HFP audio status event.
            args[1]: status. The operation status. 0 - successful operation; other values - failed operation.
            args[2]: hfp_audio_status. Audio connection status.
                0 - Disconnected
                1 - Connecting
                2 - Connected
                3 - Disconnecting
            args[3]: addr. The address of the BT master in bytearray type.
    49	4	args[0]: event_id. BT HFP volume type event.
            args[1]: status. The operation status. 0 - successful operation; other values - failed operation.
            args[2]: hfp_volume_type.
                0 - The volume type is speaker
                1 - The volume type is microphone
            args[3]: addr. The address of the BT master in bytearray type.
    50	4	args[0]: event_id. BT HFP service type event.
            args[1]: status. The operation status. 0 - successful operation; other values - failed operation.
            args[2]: hfp_service_type. The current AG network service mode.
                0 - Normal network mode
                1 - Roaming mode
            args[3]: addr. The address of the BT master in bytearray type.
    51	4	args[0]: event_id. BT HFP ring event, that is, ringing event on incoming call.
            args[1]: status. The operation status. 0 - successful operation; other values - failed operation.
            args[2]: Reserved parameter.
            args[3]: addr. The address of the BT master in bytearray type.
            args[0]: event_id. BT HFP codec type event.
            args[1]: status. The operation status. 0 - successful operation; other values - failed operation.
            args[2]: hfp_codec_type. Which codec mode is currently in use.
                1 - CVDS, 8 kHz sample rate
                2 - mSBC, 16 kHz sample rate
            args[3]: addr. The address of the BT master in bytearray type.
    61	4	args[0]: event_id. BT SPP connect event.
            args[1]: status. The operation status. 0 - successful operation; other values - failed operation.
            args[2]: spp_connect_status. SPP connection status.
                0 - Disconnected
                1 - Connecting
                2 - Connected
                3 - Disconnecting
            args[3]: addr. The MAC address of the peer device in bytearray type.
    62	4	args[0]: event_id. BT SPP disconnect event.
            args[1]: status. The operation status. 0 - successful operation; other values - failed operation.
            args[2]: spp_connect_status. SPP connection status.
                0 - Disconnected
                1 - Connecting
                2 - Connected
                3 - Disconnecting
            args[3]: addr. The MAC address of the peer device in bytearray type.
    :return:0- Successful execution; -1- Failed execution.
    """


def release():
    """Releases Bluetooth resources.

    :return:0- Successful execution; -1- Failed execution.
    """


def start():
    """Enables Bluetooth feature.

    :return:0- Successful execution; -1- Failed execution.
    """


def stop():
    """Disables Bluetooth feature.

    :return:0- Successful execution; -1- Failed execution.
    """


def getStatus():
    """Gets the Bluetooth status.

    :return:Returns Bluetooth status in integer type. 0-Stopped, 1- Working normally, -1- Failed execution.
    """


def getLocalAddr():
    """Gets the Bluetooth address.

    Note: This interface needs to be called after Bluetooth has been initialized and successfully started, such as after receiving an event with event_id set to 0 in the callback, that is, after the start is successful.

    :return:Returns a Bluetooth address (6 bytes) in bytearray type for successful execution or -1 for failed execution.
    """


def setLocalName(code, name):
    """Sets the Bluetooth name.

    :param code:Integer type. Encoding scheme. 0 - UTF8，1 - GBK.
    :param name:String type. The Bluetooth name. Maximum length: 22 bytes.
    :return:Returns a Bluetooth address (6 bytes) in bytearray type for successful execution or -1 for failed execution.
    """


def getLocalName():
    """Gets the Bluetooth name.

    :return:Returns a tuple (code, name) containing the name encoding scheme and the Bluetooth name for successful execution, or -1 for failed execution.
    """


def setVisibleMode(mode):
    """Sets the Bluetooth visible mode, which means that it configures whether the module can be discovered or connected as a slave when scanning.

    :param mode:Integer type. Visible mode. The specific meanings of the values are shown in the following table:
    Value	Description
    0	Undiscoverable, unconnectable
    1	Discoverable, unconnectable
    2	Undiscoverable, connectable
    3	Discoverable, connectable
    :return:Returns Bluetooth address (6 bytes) in bytearray type for successful execution, or -1 for failed execution.
    """


def getVisibleMode():
    """Gets the Bluetooth visible mode.

    :return:Returns the current visible mode value of the Bluetooth for successful execution, or -1 for failed execution.
    """


def startInquiry(mode):
    """Starts searching for nearby Bluetooth devices.

    :param mode:Search mode. Indicates which type of device to query, currently set to 15 to search for all.
    :return:0- Successful execution; -1- Failed execution.
    """


def cancelInquiry():
    """Cancels the searching.

    :return:0- Successful execution; -1- Failed execution.
    """


def setChannel(channel):
    """Sets the audio output channel used for answering phone calls or playing audio over Bluetooth.

    :param channel:Integer type. Audio channel. 0 - Earpiece，1 - Headphone，2 - Speaker.
    :return:0- Successful execution; -1- Failed execution.
    """


def reconnect_set(max_count, period):
    """Sets the maximum number of reconnection attempts and the time interval between two consecutive reconnection attempts when the module and Bluetooth device are disconnected due to distance.

    :param max_count:Integer type. The maximum number of reconnection attempts. 0 indicates disabling automatic reconnection.
    :param period:Integer type. The time interval between two consecutive reconnection attempts. Unit: second.
    :return:0- Successful execution; -1- Failed execution.
    """


def reconnect():
    """Actively reconnects to the last paired device, such as a mobile phone.

    This function should be called when the module reboots and reinitializes the Bluetooth connection, or when the Bluetooth is turned off and then turned back on again without rebooting the module.

    :return:0- Successful execution; -1- Failed execution.
    """


def hfpInit():
    """Initializes HFP feature.

    :return:0- Successful execution; -1- Failed execution.
    """


def hfpRelease():
    """Releases HFP resources.

    :return:0- Successful execution; -1- Failed execution.
    """


def hfpConnect(addr):
    """Connects to AG and establishes an HFP connection.

    :param addr:Bytearray type. 6-bytes‘ AG Bluetooth address.
    :return:0- Successful execution; -1- Failed execution.
    """


def hfpDisonnect(addr):
    """Disconnects the HFP connection.

    :param addr:Bytearray type. 6-bytes’ AG Bluetooth address.
    :return:0- Successful execution; -1- Failed execution.
    """


def hfpSetVolume(addr, vol):
    """Sets the volume during Bluetooth calls.

    :param addr:Bytearray type. 6-bytes‘ AG Bluetooth address.
    :param vol:Integer type. Call volume. Range: 1–15.
    :return:0- Successful execution; -1- Failed execution.
    """


def hfpRejectAfterAnswer(addr):
    """Hangs up the answered call.

    :param addr:Bytearray type. 6-bytes’ AG Bluetooth address.
    :return:0- Successful execution; -1- Failed execution.
    """


def hfpRejectCall(addr):
    """Rejects a call.

    :param addr:Bytearray type. 6-bytes’ AG Bluetooth address.
    :return:0- Successful execution; -1- Failed execution.
    """


def hfpAnswerCall(addr):
    """Answers a call.

    :param addr:Bytearray type. 6-bytes’ AG Bluetooth address.
    :return:0- Successful execution; -1- Failed execution.
    """


def hfpEnableVR(addr):
    """Enables voice assistant.

    :param addr:Bytearray type. 6-bytes’ AG Bluetooth address.
    :return:0- Successful execution; -1- Failed execution.
    """


def hfpDisableVR(*args):
    """Disables voice assistant.

    hfpDisableVR(addr)
        addr-Bytearray type. 6-bytes’ AG Bluetooth address.

    hfpDisableVR(addr, cmd)
        addr- Bytearray type. 6-bytes AG Bluetooth address.
        cmd- Integer type. Control command.

    :return: 0- Successful execution; -1- Failed execution.
    """


def a2dpavrcpInit():
    """Initializes the A2DP and AVRCP features.

    :return:0- Successful execution; -1- Failed execution.
    """


def a2dpavrcpRelease():
    """Releases the A2DP and AVRCP resources.

    :return:0- Successful execution; -1- Failed execution.
    """


def a2dpDisconnect(addr):
    """Disconnects the A2DP connection.

    :param addr:Bytearray type. 6 bytes' Bluetooth address of the A2DP host.
    :return:0- Successful execution; -1- Failed execution.
    """


def a2dpGetAddr():
    """Gets the Bluetooth address of the A2DP host.

    :return:Returns a Bluetooth address of the A2DP host (6 bytes) in bytearray type for successful execution or -1 for failed execution.
    """


def a2dpGetConnStatus():
    """Gets the A2DP connection status.

    :return:Returns the A2DP connection status. The specific meanings of the values are shown in the following table:
    Value	Type	Description
    -1	int	Failed execution
    0	int	Disconnected
    1	int	Connecting
    2	int	Connected
    3	int	Disconnecting
    """


def avrcpStart():
    """Controls the host to start playing.

    :return:0- Successful execution; -1- Failed execution.
    """


def avrcpPause():
    """Controls the host to stop playing.

    :return:0- Successful execution; -1- Failed execution.
    """


def avrcpPrev():
    """Controls the host to play the previous one.

    :return:0- Successful execution; -1- Failed execution.
    """


def avrcpNext():
    """Controls the host to play the next one.

    :return:0- Successful execution; -1- Failed execution.
    """


def avrcpSetVolume(vol):
    """Sets the host's playback volume.

    :param vol:Integer type. Playback volume. Range: 0–11.
    :return:0- Successful execution; -1- Failed execution.
    """


def avrcpGetVolume():
    """Gets the host's playback volume.

    :return:Returns the volume value in integer type for successful execution or -1 for failed execution.
    """


def avrcpGetPlayStatus():
    """Gets the host's playback status.

    :return:Returns the playback status. The specific meanings of the values are shown in the following table:
    Value	Type	Description
    -1	int	Failed execution
    0	int	No playback
    1	int	Play
    2	int	Pause
    3	int	Switching to the previous one
    4	int	Switching to the next one
    """


def avrcpGetConnStatus():
    """Gets the host connection status through the AVRCP protocol.

    :return:Returns the connection status. The specific meanings of the values are shown in the following table:
    Value	Type	Description
    -1	int	Failed execution
    0	int	Disconnected
    1	int	Connecting
    2	int	Connected
    3	int	Disconnecting
    """


def sppInit():
    """Initializes SPP feature.

    :return:0- Successful execution; -1- Failed execution.
    """


def sppRelease():
    """Releases SPP resources.

    :return:0- Successful execution; -1- Failed execution.
    """


def sppConnect(addr):
    """Establishes an SPP connection.

    :param addr:Bytearray type. 6 bytes' Bluetooth address.
    :return:0- Successful execution; -1- Failed execution.
    """


def sppDisconnect():
    """Disconnects the SPP connection.

    :return:0- Successful execution; -1- Failed execution.
    """


def sppSend(data):
    """Sends data through SPP.

    :param data:Bytearray type. The data to be sent.
    :return:0- Successful execution; -1- Failed execution.
    """
