"""
Function:
The ble module provides BLE GATT Server (slave) and BLE GATT Client (master) features based on the BLE 4.2 protocol.

Descriptions taken from:
https://python.quectel.com/doc/API_reference/en/btlib/ble.html
"""


def gattStart():
    """Enables BLE GATT feature.

    :return: 0- Successful execution; -1- Failed execution.
    """


def gattStop():
    """Disables BLE GATT feature.

    :return: 0- Successful execution; -1- Failed execution.
    """


def getStatus():
    """Gets the BLE status.

    :return: 0 - Disabled; 1 - Enabled ; -1 - Failed to get the status.
    """


def getPublicAddr():
    """Gets the public address used by the BLE protocol stack. This interface can only be called after BLE has been initialized and started successfully.

    For example, you can call the interface after the event of event_id being 0 (indicating a successful start) is triggered in the callback.
    Note: If there is a default Bluetooth MAC address set at the factory, the MAC address got by this interface will be the same as the default Bluetooth MAC address. If there is no default setting, the address got by this interface will be a randomly generated static address after the Bluetooth is enabled. Thus, the address will not be the same every time the Bluetooth feature is enabled after the module is rebooted.

    :return: Returns a bytearray type BLE address (size: 6 bytes) for successful execution and returns -1 for failed execution.
    """


def serverInit(user_cb):
    """Initializes BLE Server and registers a callback function.

    :param user_cb: Function type. Callback function. The meaning of the callback function parameters: args[0] is fixed to represent event_id;args[1] is fixed to represent the status, 0 indicating successful execution and non-0 indicating failed execution. The number of callback function parameters is not fixed at two, but depends on the first parameter args[0]. The following table lists the number of parameters and explanations for different event IDs.
    event_id	Parameter Number	Description
    0	2	args[0]: event_id. Starts BT/BLE.
            args[1]: status. The operation status. 0 - successful operation; other values - failed operation.
    1	2	args[0]: event_id. Stops BT/BLE.
            args[1]: status. The operation status. 0 - successful operation; other values - failed operation.
    16	4	args[0]: event_id. Connects BLE.
            args[1]: status. The operation status. 0 - successful operation; other values - failed operation.
            args[2]: connect_id.
            args[3]: addr. BT/BLE address in bytearray type.
    17	4	args[0]: event_id. Disconnects BLE.
            args[1]: status. The operation status. 0 - successful operation; other values - failed operation.
            args[2]: connect_id.
            args[3]: addr. BT/BLE address in bytearray type.
    18	7	args[0]: event_id. BLE update connection parameter.
            args[1]: status. The operation status. 0 - successful operation; other values - failed operation.
            args[2]: connect_id.
            args[3]: max_interval. Maximum interval. Interval: 1.25 ms. Range: 6–3200. Time range: 7.5 ms–4 s.
            args[4]: min_interval. Minimum interval. Interval: 1.25 ms. Range: 6–3200. Time range: 7.5 ms–4 s.
            args[5]: latency. The time at which the slave ignored the connection status event. It should meet the following condition:（1+latecy)*max_interval*2*1.25<timeout*10
            args[6]: timeout. Disconnect if there is no interaction during the timeout. Interval: 10 ms，Range: 10–3200 ms. Time range: 100 ms–32 s.
    20	4	args[0]: event_id. BLE connection MTU.
            args[1]: status. The operation status. 0 - successful operation; other values - failed operation.
            args[2]: handle.
            args[3]: MTU value.
    21	7	args[0]: event_id. BLE server. When the BLE client writes a characteristic value or descriptor, the server gets the notice.
            args[1]: status. The operation status. 0 - successful operation; other values - failed operation.
            args[2]: data_len. The length of the data to be got.
            args[3]: data. An array that stores the data got.
            args[4]: attr_handle. Integer type. Attribute handle.
            args[5]: short_uuid. Integer type.
            args[6]: long_uuid. A 16-byte array that stores long UUID.
    22	7	args[0]: event_id. When the BLE client reads a characteristic value or descriptor, the server gets the notice.
            args[1]: status. The operation status. 0 - successful operation; other values - failed operation.
            args[2]: data_len. The length of the data to be got.
            args[3]: data. An array that stores the got data.
            args[4]: attr_handle. Integer type, attribute handle.
            args[5]: short_uuid. Integer type.
            args[6]: long_uuid. A 16-byte array that stores long UUID.
    25	2	args[0]: event_id. Server sends notification, and receives notice sent by the peer end.
            args[1]: status. The operation status. 0 - successful operation; other values - failed operation.
    :return: 0- Successful execution; -1- Failed execution.
    """


def serverRelease():
    """Releases BLE server resources.

    :return: 0- Successful execution; -1- Failed execution.
    """


def setLocalName(code, name):
    """Sets the BLE name.

    Note: For BLE, when a device is advertising, if you need the scanning software to discover the name of the advertising device during scanning, it is necessary to include the Bluetooth name in the advertising data or include the device name in the scan response data.

    :param code: Integer type. Encoding scheme. 0 - UTF8，1 - GBK.
    :param name: String type. Encoding scheme. BLE name. The maximum length is 29 bytes.
    :return: 0- Successful execution; -1- Failed execution.
    """


def setAdvParam(min_adv,max_adv,adv_type,addr_type,channel,filter_policy,discov_mode,no_br_edr,enable_adv):
    """Sets advertising parameters.

    :param min_adv: Minimum advertising interval. Range: 0x0020–0x4000. The calculation is as follows:Time interval = min_adv * 0.625. Unit: ms.
    :param max_adv: Maximum advertising interval. Range: 0x0020–0x4000. The calculation is as follows:Time interval = max_adv * 0.625. Unit: ms.
    :param adv_type: Advertising type. The value is as follows:0 - Connectable undirected advertising (default);1 - High duty cycle connectable directed advertising;2 - Scannable undirected advertising;3 - Non-connectable undirected advertising;4 - Low duty cycle connectable directed advertising;
    :param addr_type: Local address type. The value is as follows:0 - Public address;1 - Random address;
    :param channel: Advertising channel. The value is as follows:1 - Channel 37;2 - Channel 384 - Channel 39;7 - All three channels above are selected (default);
    :param filter_policy: Advertising Filter Policy. The value is as follows:0 - Allow scan request from any, allow connect request from any;1 - Allow scan request from white list only, allow connect request from any. (Not supported currently);2 - Allow scan request from any, allow connect request from white list only. (Not supported currently);3 - Allow scan request from white list only, allow connect request from white list only. (Not supported currently);
    :param discov_mode: Discovery mode. Used by GAP protocol. The default value is 2.;1 - Limited discoverable mode;2 - General discoverable mode;
    :param no_br_edr: Disables BR/EDR. The default value is 1. Set it to 0 to enable BR/EDR.
    :param enable_adv: Enables advertising. The default value is 1. Set it to 0 to disable advertising.
    :return:0- Successful execution; -1- Failed execution.
    """


def setAdvData(data):
    """Sets the content of the advertising data.

    :param data: Bytearray type. Advertising data, with a maximum length of 31 bytes. The content of the advertising data is in the format of length+type+data. A combination of multiple sets of data in this format can be included in a single advertising data. In the example below, there are two sets of data combinations: the first one is "0x02, 0x01, 0x05", where 0x02 indicates that there are two data following it, which are 0x01 and 0x05 respectively (0x01 representing the type and 0x05 representing the specific data); the second set is the BLE name data combination, with the length being the BLE name length plus 1, the type being 0x09, and the specific data being the corresponding encoding value of the name. For the specific meanings of the type values, please refer to the official Bluetooth protocol standard document.
    :return:0- Successful execution; -1- Failed execution.
    """


def setAdvRspData(data):
    """Sets the scan response data.

    :param data:Bytearray type. Scan response data with a maximum length of 31 bytes. The format for the scan response data is the same as that of the advertising data set by the setAdvData function.
    :return:0- Successful execution; -1- Failed execution.
    """


def addService(primary, server_id, uuid_type, uuid_s, uuid_l):
    """Adds a service.

    :param primary:Integer type. Service type. 1 indicates primary service and other values indicate non-primary service.
    :param server_id:Integer type. Server ID to identify a service.
    :param uuid_type:Integer type. The UUID type. 0 - long UUID (128 bit); 1 - short UUID (16 bit).
    :param uuid_s:Integer type. Short UUID with 2 bytes (16 bit). When uuid_type is set to 0, the value is 0.
    :param uuid_l:Bytearray type. Long UUID with 16 bytes (128bit). When uuid_type is set to 1, the value is bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]).
    :return:0- Successful execution; -1- Failed execution.
    """


def addChara(server_id, chara_id, chara_prop, uuid_type, uuid_s, uuid_l):
    """Adds a characteristic in the service.

    :param server_id:Integer type. Server ID to identify a service.
    :param chara_id:Integer type. Characteristic ID.
    :param chara_prop:Integer type. Characteristic property. Hexadecimal number. You can specify multiple attributes at the same time by OR, and the specific meanings of the values are as shown in the following table:
    Value	Description
    0x01	Advertising
    0x02	Readable
    0x04	Writable and does not require link-layer response
    0x08	Writable
    0x10	Notification
    0x20	Indication
    0x40	Authenticated signed writes
    0x80	Extended property
    :param uuid_type:Integer type. The UUID type. 0 - long UUID (128 bit); 1 - short UUID (16 bit).
    :param uuid_s:Integer type. Short UUID with 2 bytes (16 bit). When uuid_type is set to 0, the value is 0.
    :param uuid_l:Bytearray type. Long UUID with 16 bytes (128bit). When uuid_type is set to 1, the value is bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]).
    :return:0- Successful execution; -1- Failed execution.
    """


def addCharaValue(server_id, chara_id, permission, uuid_type, uuid_s, uuid_l, value):
    """Adds a characteristic value in the characteristic.

    :param server_id:Integer type. Server ID to identify a service.
    :param chara_id:Integer type. Characteristic ID.
    :param permission:Integer type. Permission for characteristic value. 2 bytes. Hexadecimal number. You can specify multiple attributes at the same time by OR, and the specific meanings of the values are shown in the following table:
    Value	Description
    0x0001	Readable permission
    0x0002	Writable permission
    0x0004	Authentication permission for read
    0x0008	Authorization permission for read
    0x0010	Encryption permission for read
    0x0020	Authorization and authentication permission for read
    0x0040	Authentication permission for write
    0x0080	Authorization permission for write
    0x0100	Encryption permission for write
    0x0200	Authorization and authentication permission for write
    :param uuid_type:Integer type. The UUID type. 0 - long UUID (128 bit); 1 - short UUID (16 bit).
    :param uuid_s:Integer type. Short UUID with 2 bytes (16 bit). When uuid_type is set to 0, the value is 0.
    :param uuid_l:Bytearray type. Long UUID with 16 bytes (128bit). When uuid_type is set to 1, the value is bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]).
    :param value:Bytearray type. Characteristic value data.
    :return:0- Successful execution; -1- Failed execution.
    """


def changeCharaValue(server_id, chara_id, value):
    """Changes characteristic value.

    :param server_id:Integer type. Server ID to identify a service.
    :param chara_id:Integer type. Characteristic ID.
    :param value:Bytearray type. Characteristic value data.
    :return:0- Successful execution; -1- Failed execution.
    """


def addCharaDesc(server_id, chara_id, permission, uuid_type, uuid_s, uuid_l, value):
    """Adds a characteristic description in the characteristic. Note that the characteristic description and the characteristic value share the same characteristic.

    :param server_id:Integer type. Server ID to identify a service.
    :param chara_id:Integer type. Characteristic ID.
    :param permission:Integer type. Permission for characteristic value. 2 bytes. Hexadecimal number. You can specify multiple attributes at the same time by OR, and the specific meanings of the values are as shown in the following table:
    Value	Description
    0x0001	Readable permission
    0x0002	Writable permission
    0x0004	Authentication permission for read
    0x0008	Authorization permission for read
    0x0010	Encryption permission for read
    0x0020	Authorization and authentication permission for read
    0x0040	Authentication permission for write
    0x0080	Authorization permission for write
    0x0100	Encryption permission for write
    0x0200	Authorization and authentication permission for write
    :param uuid_type:Integer type. The UUID type. 0 - long UUID (128 bit); 1 - short UUID (16 bit).
    :param uuid_s:Integer type. Short UUID with 2 bytes (16 bit). When uuid_type is set to 0, the value is 0.
    :param uuid_l:Bytearray type. Long UUID with 16 bytes (128bit). When uuid_type is set to 1, the value is bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]).
    :param value:Bytearray type. Characteristic value data.
    :return:0- Successful execution; -1- Failed execution.
    """


def addOrClearService(option, mode):
    """Adds all the service information that has been added to the module, or clears all the service information that has been added in the module.

    :param option:Integer type. Operation type. 0 - Clear all services; 1 - Add all services.
    :param mode:Integer type. Whether to keep the default system GAP and GATT service. 0 - Delete; 1 - Keep.
    :return:0- Successful execution; -1- Failed execution.
    """


def sendNotification(connect_id, attr_handle, value):
    """Sends notification.

    :param connect_id:Integer type. Connection ID.
    :param attr_handle:Integer type. Attribute handle.
    :param value:Bytearray type. The data to be sent. The maximum length is MTU.
    :return:0- Successful execution; -1- Failed execution.
    """


def sendIndication(connect_id, attr_handle, value):
    """Sends indication.

    :param connect_id:Integer type. Connection ID.
    :param attr_handle:Integer type. Attribute handle.
    :param value:Bytearray type. The data to be sent. The maximum length is MTU.
    :return:0- Successful execution; -1- Failed execution.
    """


def advStart():
    """Starts advertising.

    :return:0- Successful execution; -1- Failed execution.
    """


def advStop():
    """Stops advertising.

    :return:0- Successful execution; -1- Failed execution.
    """


def clientInit(user_cb):
    """Initializes BLE Client and registers a callback function.

    :param user_cb: Function type. Callback function. The meaning of the callback function parameters: args[0] is fixed to represent event_id;
    args[1] is fixed to represent the status, 0 indicating successful execution and non-0 indicating failed execution. The number of callback function parameters is not fixed at two, but depends on the first parameter args[0]. The following table lists the number of parameters and explanations for different event IDs.
    event_id	Parameter Number	Description
    0	2	args[0]: event_id. Starts BT/BLE
            args[1]: status. The operation status. 0 - successful operation; other values - failed operation.
    1	2	args[0]: event_id. Stops BT/BLE.
            args[1]: status. The operation status. 0 - successful operation; other values - failed operation.
    16	4	args[0]: event_id. Connects BLE.
            args[1]: status. The operation status. 0 - successful operation; other values - failed operation.
            args[2]: connect_id.
            args[3]: addr. BT/BLE address in bytearray type.
    17	4	args[0]: event_id. Disconnects BLE.
            args[1]: status. The operation status. 0 - successful operation; other values - failed operation.
            args[2]: connect_id.
            args[3]: addr. BT/BLE address in bytearray type.
    18	7	args[0]: event_id. BLE update connection parameter.
            args[1]: status. The operation status. 0 - successful operation; other values - failed operation.
            args[2]: connect_id.
            args[3]: max_interval. Maximum interval. Interval: 1.25 ms. Range: 6–3200. Time range: 7.5 ms–4 s.
            args[4]: min_interval. Minimum interval. Interval: 1.25 ms. Range: 6–3200. Time range: 7.5 ms–4 s.
            args[5]: latency. The time at which the slave ignored the connection status event. It should meet the following condition:（1+latecy)*max_interval*2*1.25<timeout*10
            args[6]: timeout. Disconnect if there is no interaction during the timeout. Interval: 10ms，Range: 10–3200 ms. Time range: 100 ms–32 s.
    19	9	args[0]: event_id. BLE scan report.
            args[1]: status. The operation status. 0 - successful operation; other values - failed operation.
            args[2]: event_type.
            args[3]: The name of the scanned device.
            args[4]: Device address type.
            args[5]: Device address in bytearray type.
            args[6]: rssi. Signal strength.
            args[7]: data_len. The length of the raw data scanned.
            args[8]: data. The raw data scanned.
    20	4	args[0]: event_id. BLE connection MTU.
            args[1]: status. The operation status. 0 - successful operation; other values - failed operation.
            args[2]: handle.
            args[3]: MTU value.
    23	4	args[0]: event_id. Client receives notification.
            args[1]: status. The operation status. 0 - successful operation; other values - failed operation.
            args[2]: data_len. Data length.
            args[3]: data. Raw data containing handle and other data. The format and description of the raw data is described in the example at the beginning.
    24	4	args[0]: event_id. Client receives indication.
            args[1]: status. The operation status. 0 - successful operation; other values - failed operation.
            args[2]: data_len. Data length.
            args[3]: data. Raw data containing indication. The format and description of the raw data is described in the example at the beginning.
    26	2	args[0]: event_id. Starts discover service.
            args[1]: status. The operation status. 0 - successful operation; other values - failed operation.
    27	5	args[0]: event_id. Discovers service.
            args[1]: status. The operation status. 0 - successful operation; other values - failed operation.
            args[2]: start_handle. The start handle of the service.
            args[3]: end_handle. The end handle of the service.
            args[4]: UUID, indicating the UUID of the service (Short UUID).
    28	4	args[0]: event_id. Discovers characteristic.
            args[1]: status. The operation status. 0 - successful operation; other values - failed operation.
            args[2]: data_len. Data length.
            args[3]: data. Raw data containing handle, attribute, UUID and other data. The format and description of the raw data is described in the example at the beginning.
    29	4	args[0]: event_id. Discovers characteristic descriptor.
            args[1]: status. The operation status. 0 - successful operation; other values - failed operation.
            args[2]: data_len. Data length.
            args[3]: data. Raw data containing handle, UUID and other data. The format and description of the raw data is described in the example at the beginning.
    30	2	args[0]: event_id. Writes characteristic value with peer response.
            args[1]: status. The operation status. 0 - successful operation; other values - failed operation.
    31	2	args[0]: event_id. Writes characteristic value without peer response.
            args[1]: status. The operation status. 0 - successful operation; other values - failed operation.
    32	4	args[0]: event_id. Reads characteristic value by handle.
            args[1]: status. The operation status. 0 - successful operation; other values - failed operation.
            args[2]: data_len. Data length.
            args[3]: data. Raw data.
    33	4	args[0]: event_id. Reads characteristic value by UUID.
            args[1]: status. The operation status. 0 - successful operation; other values - failed operation.
            args[2]: data_len. Data length.
            args[3]: data. Raw data.
    34	4	args[0]: event_id. Reads multiple characteristic value.
            args[1]: status. The operation status. 0 - successful operation; other values - failed operation.
            args[2]: data_len. Data length.
            args[3]: data. Raw data.
    35	2	args[0]: event_id. Writes characteristic descriptor.
            args[1]: status. The operation status. 0 - successful operation; other values - failed operation.
    36	4	args[0]: event_id. Reads characteristic descriptor.
            args[1]: status. The operation status. 0 - successful operation; other values - failed operation.
            args[2]: data_len. Data length.
            args[3]: data. Raw data.
    37	3	args[0]: event_id. Attribute error.
            args[1]: status. The operation status. 0 - successful operation; other values - failed operation.
            args[2]: errcode. Error code.
    :return:0- Successful execution; -1- Failed execution.
    """


def clientRelease():
    """Releases BLE client resources.

    :return:0- Successful execution; -1- Failed execution.
    """


def setScanParam(scan_mode, interval, scan_window, filter_policy, addr_type):
    """Sets the scan parameters.

    The scan_window should not be greater than the interval. If they are equal, it indicates continuous scanning, and the BLE controller will run continuously, occupying system resources and preventing other tasks from being executed. Therefore, continuous scanning is not allowed. It is also not recommended to set the time interval too short, because more frequent scanning consumes more power.

    :param scan_mode:Integer type. Scan mode. 0 indicates passive scanning and 1 indicating active scanning. Default value: 1.
    :param interval:Integer type. Scan interval. Range: 0x0004–0x4000. Time interval = interval * 0.625. Unit: ms.
    :param scan_window:Integer type. Scanning time for a single scan. Range: 0x0004–0x4000. Scan time = scan_window* 0.625. Unit: ms.
    :param filter_policy:Integer type. Scan filter policy. Default value: 0. 0 - Allow all advertisement packets except directed advertising packets not addressed to this device. 1 - Allow only advertisement packets from devices where the advertiser’s address is in the Whitelist. and directed advertising packets which are not addressed for this device shall be ignored. 2 - Allow all undirected advertisement packets, and directed advertising packets where the initiator address is a resolvable private address, and directed advertising packets addressed to this device. 3 - Allow all advertisement packets from devices where the advertiser’s address is in the Whitelist, and directed advertising packets where the initiator address is a resolvable private address, and directed advertising packets addressed to this device.
    :param addr_type:Integer type. Local address type. 0 - Public address; 1 - Random address.
    :return:0- Successful execution; -1- Failed execution.
    """


def scanStart():
    """Starts scanning.

    :return:0- Successful execution; -1- Failed execution.
    """


def scanStop():
    """Stops scanning.

    :return:0- Successful execution; -1- Failed execution.
    """


def setScanFilter(act):
    """Enables or disables scan filtering.

    If enabled, only one advertising data packet from the same device will be reported during the scan; if disabled, all advertising data packets from the same device will be reported.

    :param act:Integer type. Controls whether to enable scan filtering. 0 - Disable; 1 - Enable. Default value: 1.
    :return:0- Successful execution; -1- Failed execution.
    """


def connect(addr_type, addr):
    """Connects the device according to the specified device address.

    :param addr_type:Integer type. Address type. 0 - Public address; 1 - Random address.
    :param addr:Bytearray type. BLE address. Size: 6 bytes.
    :return:0- Successful execution; -1- Failed execution.
    """


def cancelConnect(addr):
    """Cancels the connection that is being established.

    :param addr:Bytearray type. BLE address. Size: 6 bytes.
    :return:0- Successful execution; -1- Failed execution.
    """


def disconnect(connect_id):
    """Disconnects the connection that has been established.

    :param connect_id:Integer type. The connection ID obtained when the connection was established.
    :return:0- Successful execution; -1- Failed execution.
    """


def discoverAllService(connect_id):
    """Discovers all services.

    :param connect_id:Integer type. The connection ID obtained when the connection was established.
    :return:0- Successful execution; -1- Failed execution.
    """


def discoverByUUID(connect_id, uuid_type, uuid_s, uuid_l):
    """Discovers the services of specified UUID.

    :param connect_id:Integer type. The connection ID obtained when the connection was established.
    :param uuid_type:Integer type. UUID type. 0 - Long UUID (128 bit); 1 - Short UUID (16 bit)
    :param uuid_s:Integer type. Short UUID, 2 bytes (16 bit). When uuid_type is set to 0, the uuid_s is 0.
    :param uuid_l:Bytearray type. Long UUID, 16 bytes (128 bit). When uuid_type is set to 1, the uuid_l is bytearray ([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]).
    :return:0- Successful execution; -1- Failed execution.
    """


def discoverAllIncludes(connect_id, start_handle, end_handle):
    """Discovers all includes. The start_handle and end_handle should be in the same service.

    :param connect_id:Integer type. The connection ID obtained when the connection was established.
    :param start_handle:Integer type. Start handle. Start discovering includes from this handle.
    :param end_handle:Integer type. End handle. Stop discovering includes from this handle.
    :return:0- Successful execution; -1- Failed execution.
    """


def discoverAllChara(connect_id, start_handle, end_handle):
    """Discovers all characteristics. The start_handle and end_handle should be in the same service.

    :param connect_id:Integer type. The connection ID obtained when the connection was established.
    :param start_handle:Integer type. Start handle. Start discovering characteristics from this handle.
    :param end_handle:Integer type. End handle. Stop discovering characteristics from this handle.
    :return:0- Successful execution; -1- Failed execution.
    """


def discoverAllCharaDesc(connect_id, start_handle, end_handle):
    """Discovers all characteristic descriptions. The start_handle and end_handle should be in the same service.

    :param connect_id:Integer type. The connection ID obtained when the connection was established.
    :param start_handle:Integer type. Start handle. Start discovering characteristic descriptions from this handle.
    :param end_handle:Integer type. End handle. This Stop discovering characteristic descriptions from this handle.
    :return:0- Successful execution; -1- Failed execution.
    """


def readCharaByUUID(connect_id, start_handle, end_handle, uuid_type, uuid_s, uuid_l):
    """Reads the characteristic value of specified UUID. The start_handle and end_handle must contain a characteristic value handle.

    :param connect_id:Integer type. Connection ID. The connection ID obtained when the connection was established.
    :param start_handle:Integer type. Start handle. The start_handle and end_handle should be in the same service.
    :param end_handle:Integer type. End handle. The start_handle and end_handle should be in the same service.
    :param uuid_type:Integer type. UUID type. 0 - Long UUID (128 bit); 1 - Short UUID (16 bit)
    :param uuid_s:Integer type. Short UUID, 2 bytes (16 bit). When uuid_type is set to 0, the uuid_s is 0.
    :param uuid_l:Bytearray type. Long UUID, 16 bytes (128 bit). When uuid_type is set to 1, the uuid_l is bytearray ([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]).
    :return:0- Successful execution; -1- Failed execution.
    """


def readCharaByHandle(connect_id, handle, offset, is_long):
    """Reads the characteristic value of specified handle.

    :param connect_id:Integer type. The connection ID obtained when the connection was established.
    :param handle:Integer type. Characteristic value handle.
    :param offset:Integer type. Offset.
    :param is_long:Integer type. Long characteristic value flag. 0 indicates short characteristic value which can be finished reading at one time; 1 indicates long characteristic value which needs to be read by multiple times.
    :return:0- Successful execution; -1- Failed execution.
    """


def readCharaDesc(connect_id, handle, is_long):
    """Reads the characteristic description.

    :param connect_id:Integer type. The connection ID obtained when the connection was established.
    :param handle:Integer type. Characteristic value handle.
    :param is_long:Integer type. Long characteristic value flag. 0 indicates short characteristic value which can be finished reading at one time;1 indicates long characteristic value which needs to be read by multiple times.
    :return:0- Successful execution; -1- Failed execution.
    """


def writeChara(connect_id, handle, offset, is_long, data):
    """Writes the characteristic value with peer response.

    :param connect_id:Integer type.The connection ID obtained when the connection was established.
    :param handle:Integer type. Characteristic value handle.
    :param offset:Integer type. Offset.
    :param is_long:Integer type. Long characteristic value flag. 0 indicates short characteristic value which can be finished reading at one time; 1 indicates long characteristic value which needs to be read by multiple times.
    :param data:Bytearray type. Characteristic value data.
    :return:0- Successful execution; -1- Failed execution.
    """


def writeCharaNoRsp(connect_id, handle, data):
    """Writes the characteristic value without peer response.

    :param connect_id:Integer type. The connection ID obtained when the connection was established.
    :param handle:Integer type. Characteristic value handle.
    :param data:Bytearray type. Characteristic value data.
    :return:0- Successful execution; -1- Failed execution.
    """


def writeCharaDesc(connect_id, handle, data):
    """Writes the characteristic description.

    :param connect_id:Integer type. The connection ID obtained when the connection was established.
    :param handle:Integer type. Characteristic description handle.
    :param data:Bytearray type. Characteristic description data.
    :return:0- Successful execution; -1- Failed execution.
    """
