"""
Function:
This feature is used to create MQTT clients to publish and subscribe to topics.

Descriptions taken from:
https://python.quectel.com/doc/API_reference/en/networklib/umqtt.html
"""


class MQTTClient(object):

    def __init__(self, client_id, server, port=0, user=None, password=None,
                 keepalive=0, ssl=False, ssl_params=None, reconn=True,version=4):
        """Creates MQTT clients.

        :param client_id:Client ID. Each client ID is unique.
        :param server:Server address, which can be an IP address or domain name.
        :param port:Server port (optional). Default value: 1883. The default port of MQTT over SSL/TLS is 8883.
        :param user:Username registered on the server (optional).
        :param password:Password registered on the server (optional).
        :param keepalive:Timeout of keep-alive (optional). Default value: 0. Unit: s.
        :param ssl:Enable or disable SSL/TSL encryption.
        :param ssl_params:SSL/TLS parameter (optional).
        :param reconn:Enable or disable the internal reconnection mechanism (optional). Default value: True (enable).
        :param version:The selected MQTT version (optional). version=3 indicates MQTTv3.1. Default value: 4. version=4 indicates MQTTv3.1.1.
        """

    def set_callback(self, callback):
        """Sets the callback function of receiving messages.

        :param callback:The callback function of receiving messages.
        :return:
        """

    def error_register_cb(self, callback):
        """Sets the callback function of error occurrence. When the MQTT internal thread is abnormal, the error message is returned by the callback function. The callback function can be called only when the internal reconnection is not enabled.

        :param callback:The callback function of error occurrences.
        :return:
        """

    def set_last_will(self, topic, msg, retain=False, qos=0):
        """Sets the last will to be sent to the MQTT server. If a client ungracefully disconnects from the server without calling MQTTClient.disconnect(), the last will will be sent to other clients.

        :param topic:Last-will topic.
        :param msg:Last-will content
        :param retain:When retain = True, the MQTT broker will retain the message. Default value: False.
        :param qos:Quality of Service, 0 or 1.
        :return:
        """

    def connect(self, clean_session=True):
        """Connects to MQTT server. Failed connection leads to an MQTT exception.

        :param clean_session:Client session type, optional parameter. If this value is True, the MQTT server will delete all information about the client when the client disconnects from the MQTT server. If this value is False, the client session is persistent, that is, when the client disconnects from the MQTT server, the subscription and queuing information will be retained. Default value: False.
        :return:0 – Successful execution;Error message – Failed execution
        """

    def disconnect(self):
        """Disconnects from the MQTT server.

        :return:
        """

    def close(self):
        """Releases socket resources.

        Please note the differences between MQTTClient.disconnect() and MQTTClient.close(), where MQTTClient.close() only releases socket resources but MQTTClient.disconnect() releases resources including threads.
        Note: This method can be used only when the client needs to reconnect to the MQTT server. See *Example of MQTT Reconnection After Ungraceful Disconnection* below for details. Call MQTTClient.disconnect() to normally disconnect from the MQTT server.

        :return:
        """

    def ping(self):
        """Pings to MQTT server to check the connection when keepalive is not 0. When keepalive is 0, this method is disabled.

        :return:
        """

    def publish(self, topic, msg, retain=False, qos=0):
        """Publishes messages.

        :param topic:Message topic.
        :param msg:Data to be sent.
        :param retain:Default value: False. If this value is set to True when you send a message, the message is retained.
        The MQTT server retains the last received message with a RETAIN flag bit of True on the server. Whenever the MQTT client connects to the MQTT server and subscribes to a topic, if there is a Retained message under that topic, the MQTT server immediately pushes the Retained message to the client.
        Note: The MQTT server will only save the last received message with the RETAIN flag bit of True for each topic, that is, if the MQTT server saves one retained message for a Topic, when the client publishes a new retained message, the original message on the server is overwritten.
        :param qos:MQTT QoS, 0 or 1. Default value: 0.0 – The sender sends a message only once.1 – The sender sends a message at least once and guarantees that the message has been delivered to the MQTT broker.
        :return:
        """

    def subscribe(self, topic, qos):
        """Subscribes to MQTT topics.

        :param topic:topic
        :param qos:MQTT QoS, 0 or 1. Default value: 0.0 – The sender sends a message only once.1 – The sender sends a message at least once and guarantees that the message has been delivered to the MQTT broker.
        :return:
        """

    def check_msg(self):
        """Checks whether the MQTT server has messages to be processed.

        :return:
        """

    def wait_msg(self):
        """Blocks waiting for a message response from the MQTT server.

        :return:
        """

    def get_mqttsta(self):
        """Gets MQTT connection status.

        Note:
        BG95 series module does not support the API.
        If you call MQTTClient.disconnect() before calling MQTTClient.get_mqttsta(), -1 will be returned, because the created object resources are released.

        :return:
        0 – Successful connection
        1 – Connecting
        2 – Server connection closed
        -1 – Connection error
        """
