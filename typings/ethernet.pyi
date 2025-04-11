"""
Function:
ethernet module contains features related to Ethernet control and network configuration, and provides unified management for different types of Ethernet NIC.

Example:
This section introduces the initialization process of NIC in the terminal mode, gateway mode and static IP address configuration respectively based on different application scenarios.
The following example is only for NIC application configuration on the module. Ethernet NICs can be normally used after the corresponding operation is performed on the peer device.
Some NICs are not applicable to the following examples. Please use NICs according to the corresponding instructions for different NIC drivers.

Descriptions taken from:
https://python.quectel.com/doc/API_reference/en/peripherals/ethernet.html
"""


class W5500(object):
    """W5500 Ethernet NIC Control

    This class controls Ethernet NIC devices of W5500.
    Currently, only EC600N and EC600U module series support this feature.

    Descriptions: https://python.quectel.com/doc/API_reference/en/peripherals/ethernet.W5500.html
    """

    def __init__(self, mac, ip='', subnet='', gateway='', spi_port=-1, spi_cs_pin=-1, extint_pin=-1, reset_pin=-1, work_mode=0):
        """Loads W5500 driver, initializes W5500 Ethernet NIC and returns W5500 NIC object.

        :param mac: Byte stream. MAC address with a length of 6 bytes.
        :param ip: IP address of Ethernet NIC. The default value is an empty string'', indicating that the default IP address is 192.168.1.100 in the program.
        :param subnet: Subnet mask address of Ethernet NIC. The default value is an empty string'', indicating that 255.255.255.0 is used as the subnet mask.
        :param gateway: Gateway address of Ethernet NIC. The default value is an empty string'', indicating that the last bit of IP address is replaced with 1 as the gateway address.
        :param spi_port: Connect to SPI port of W5500. The default value is -1, indicating that the last configured value is used and the default configuration in the program is SPI1 port.
        :param spi_cs_pin: Connect to SPI chip select GPIO pin of W5500. The default value is -1, indicating that the last configured value is used and the default configuration in the program is Pin.GPIO34.
        :param extint_pin: Connect to external interrupt GPIO pin of W5500. The default value is -1, indicating that the last configured value is used and the default configuration in the program is Pin.GPIO19.
        :param reset_pin: Connect to reset GPIO pin of W5500. The default value is -1, indicating that the last configured value is used and the default configuration in the program is Pin.GPIO17.
        :param work_mode: Configure Ethernet working mode. The default mode is terminal mode. 0 and 1 respectively represents terminal mode and gateway mode. Terminal mode indicates that the module is used as a terminal device to connect to a network supply device to access the network. Gateway mode indicates that the module is used as a gateway to provide network access for external devices through LTE network.
        """

    def set_addr(self, ip, subnet, gateway):
        """Configures NIC static IP Address.

        :param ip: IP address of Ethernet NIC. The value is an empty string'', indicating that the default IP address is 192.168.1.100 in the program.
        :param subnet: Subnet mask address of Ethernet NIC. The value is an empty string'', indicating that 255.255.255.0 is used as the subnet mask.
        :param gateway: Gateway address of Ethernet NIC. The value is an empty string'', indicating that the last bit of IP address is replaced with 1 as the gateway address.
        :return: 0 - Successful execution; Other values - Failed execution
        """

    def set_dns(self, primary_dns, secondary_dns):
        """Configures NIC DNS server.

        :param primary_dns: Primary address of DNS server.
        :param secondary_dns: Secondary address of DNS server.
        :return: 0 - Successful execution; Other values - Failed execution
        """

    def set_up(self):
        """Enables NIC and then NIC processes network interfaces and messages normally."""

    def set_down(self):
        """Disables NIC and then NIC no longer processes network interfaces and messages."""

    def dhcp(self):
        """Obtains dynamic IP. This method is used in the terminal mode so that IP information can be automatically obtained.

        :return: 0 - Successful execution; Other values - Failed execution
        """

    def ipconfig(self):
        """Obtains NIC network information. MAC address, host name, IP address type, IP address, subnet mask, gateway address and DNS server address can be obtained through this method.

        :return: List type. The format is as follows: [(mac, hostname), (iptype, ip, subnet, gateway, primary_dns，secondary_dns)].
        mac	str	mac address and the format is'XX-XX-XX-XX-XX-XX'.
        hostname	str	NIC name
        iptype	str	ip type. 4 indicates IPv4 and 6 indicates IPv6. Currently, only IPv4 is supported.
        ip	str	IP address
        subnet	str	Subnet mask
        gateway	str	Gateway address
        primary_dns	str	Primary address of DNS server
        secondary_dns	str	Secondary address of DNS server
        """

    def set_default_NIC(self, ip):
        """Configures the default NIC.

        :param ip: Default NIC IP address.
        :return: 0 - Successful execution; Other values - Failed execution
        """


class DM9051(object):
    """DM9051 Ethernet NIC Control

    This class controls Ethernet NIC devices of DM9051.
    Currently, only EC600N module series support this feature.

    Descriptions: https://python.quectel.com/doc/API_reference/en/peripherals/ethernet.DM9051.html
    """

    def __init__(self, mac, ip='', subnet='', gateway='', spi_port=-1,spi_cs_pin=-1):
        """Loads DM9051 driver, initializes DM9051 Ethernet NIC and returns DM9051 NIC object.

        :param mac: Byte stream. MAC address with a length of 6 bytes.
        :param ip: IP address of Ethernet NIC. The default value is an empty string'', indicating that the default IP address is 192.168.1.100 in the program.
        :param subnet: cSubnet mask address of Ethernet NIC. The default value is an empty string'', indicating that 255.255.255.0 is used as the subnet mask.
        :param gateway: Gateway address of Ethernet NIC. The default value is an empty string'', indicating that the last bit of IP address is replaced with 1 as the gateway address.
        :param spi_port: Connect to SPI port of DM9051. The default value is -1, indicating that the last configured value is used and the default configuration in the program is SPI1 port.
        :param spi_cs_pin: Connect to SPI chip select GPIO pin of DM9051. The default value is -1, indicating that the last configured value is used and the default configuration in the program is Pin.GPIO13.
        """

    def set_addr(self, ip, subnet, gateway):
        """Configures NIC static IP Address.

        :param ip: IP address of Ethernet NIC. The value is an empty string'', indicating that the default IP address is 192.168.1.100 in the program.
        :param subnet: Subnet mask address of Ethernet NIC. The value is an empty string'', indicating that 255.255.255.0 is used as the subnet mask.
        :param gateway: Gateway address of Ethernet NIC. The value is an empty string'', indicating that the last bit of IP address is replaced with 1 as the gateway address.
        :return: 0 - Successful execution; Other values - Failed execution
        """

    def set_dns(self, primary_dns, secondary_dns):
        """Configures NIC DNS server.

        :param primary_dns: Primary address of DNS server.
        :param secondary_dns: Secondary address of DNS server.
        :return: 0 - Successful execution; Other values - Failed execution
        """

    def set_down(self):
        """Disables NIC and then NIC no longer processes network interfaces and messages."""

    def dhcp(self):
        """Obtains dynamic IP. This method is used in the terminal mode so that IP information can be automatically obtained.

        :return: 0 - Successful execution; Other values - Failed execution
        """

    def ipconfig(self):
        """Obtains NIC network information.

        MAC address, host name, IP address type, IP address, subnet mask, gateway address and DNS server address can be obtained through this method.

        :return:List type. The Format is as follows: [(mac, hostname), (iptype, ip, subnet, gateway, primary_dns，secondary_dns)].
        Parameter	Type	Description
        mac	str	mac address and the format is'XX-XX-XX-XX-XX-XX'.
        hostname	str	NIC name
        iptype	str	ip type. 4 indicates IPv4 and 6 indicates IPv6. Currently, only IPv4 is supported.
        ip	str	IP address
        subnet	str	Subnet mask
        gateway	str	Gateway address
        primary_dns	str	Primary address of DNS server
        secondary_dns	str	Secondary address of DNS server
        """


class CH395(object):
    """CH395 Ethernet NIC Control.

    This class controls Ethernet NIC devices of CH395.
    Currently, only EC600N module series support this feature.

    Descriptions: https://python.quectel.com/doc/API_reference/en/peripherals/ethernet.CH395.html
    """

    def __init__(self, mac, ip='', subnet='', gateway='', spi_port=-1, spi_cs_pin=-1, extint_pin=-1, reset_pin=-1, work_mode=0):
        """Loads CH395 driver, initializes CH395 Ethernet NIC and returns CH395 NIC object.

        :param mac: Byte stream. MAC address with a length of 6 bytes.
        :param ip: IP address of Ethernet NIC. The default value is an empty string'', indicating that the default IP address is 192.168.1.100 in the program.
        :param subnet: Subnet mask address of Ethernet NIC. The default value is an empty string'', indicating that 255.255.255.0 is used as the subnet mask.
        :param gateway: Gateway address of Ethernet NIC. The default value is an empty string'', indicating that the last bit of IP address is replaced with 1 as the gateway address.
        :param spi_port: Connect to SPI port of CH395. The default value is -1, indicating that the last configured value is used and the default configuration in the program is SPI1 port.
        :param spi_cs_pin: Connect to SPI chip select GPIO pin of CH395. The default value is -1, indicating that the last configured value is used and the default configuration in the program is Pin.GPIO4.
        :param extint_pin: Connect to external interrupt GPIO pin of CH395. The default value is -1, indicating that the last configured value is used and the default configuration in the program is Pin.GPIO24.
        :param reset_pin: Connect to reset GPIO pin of CH395. It indicates that the last configured value is used and the default configuration in the program is Pin.GPIO30.
        :param work_mode: Configure Ethernet working mode. The default mode is terminal mode. 0 and 1 respectively represents terminal mode and gateway mode. Terminal mode indicates that the module is used as a terminal device to connect to a network supply device to access the network. Gateway mode indicates that the module is used as a gateway to provide network access for external devices through LTE network.
        """

    def set_addr(self, ip, subnet, gateway):
        """Configures NIC static IP Address.

        :param ip: IP address of Ethernet NIC. The value is an empty string'', indicating that the default IP address is 192.168.1.100 in the program.
        :param subnet: Subnet mask address of Ethernet NIC. The value is an empty string'', indicating that 255.255.255.0 is used as the subnet mask.
        :param gateway: Gateway address of Ethernet NIC. The value is an empty string'', indicating that the last bit of IP address is replaced with 1 as the gateway address.
        :return: 0 - Successful execution; Other values - Failed execution
        """

    def set_dns(self, primary_dns, secondary_dns):
        """Configures NIC DNS server.

        :param primary_dns: Primary address of DNS server.
        :param secondary_dns: Secondary address of DNS server.
        :return: 0 - Successful execution; Other values - Failed execution
        """

    def set_up(self):
        """Enables NIC and then NIC processes network interfaces and messages normally."""

    def set_down(self):
        """Disables NIC and then NIC no longer processes network interfaces and messages."""

    def dhcp(self):
        """Obtains dynamic IP. This method is used in the terminal mode so that IP information can be automatically obtained.

        :return: 0 - Successful execution; Other values - Failed execution
        """

    def ipconfig(self):
        """Obtains NIC network information. MAC address, host name, IP address type, IP address, subnet mask, gateway address and DNS server address can be obtained through this method.

        :return: Returns list type. The Format is as follows: [(mac, hostname), (iptype, ip, subnet, gateway, primary_dns，secondary_dns)].
        Parameter	Type	Description
        mac	str	mac address and the format is'XX-XX-XX-XX-XX-XX'.
        hostname	str	NIC name
        iptype	str	ip type. 4 indicates IPv4 and 6 indicates IPv6. Currently, only IPv4 is supported.
        ip	str	IP address
        subnet	str	Subnet mask
        gateway	str	Gateway address
        primary_dns	str	Primary address of DNS server
        secondary_dns	str	Secondary address of DNS server
        """

    def set_default_NIC(self, ip):
        """Configures the default NIC.

        :param ip: Default NIC IP address.
        :return: 0 - Successful execution; Other values - Failed execution
        """

    def status(self):
        """Obtains NIC current status.

        :return: Tuple type. The Format is as follows: (dev, active, link).
        Parameter	Type	Description
        dev	bool	Whether NIC device is normally connected. True and False respectively indicate that NIC device is connected and is not connected.
        active	bool	Whether NIC is activated. True and False respectively indicate enable and disable, which correspond to set_up and set_down.
        link	bool	Whether the network cable of NIC is connected. True and False respectively indicate the network cable is connected and is not connected.
        """


class YT8512H(object):
    """YT8512H PHY Control

    This class controls Ethernet NIC devices of YT8512H and SZ18201.
    Currently, only EC600A module series support this feature.

    Descriptions: https://python.quectel.com/doc/API_reference/en/peripherals/ethernet.YT8512H.html
    """

    def __init__(self, mac, ip='', subnet='', gateway=''):
        """Loads YT8512H driver, initializes YT8512H phy device and returns YT8512H NIC object.

        :param mac: Byte stream. MAC address with a length of 6 bytes.
        :param ip: IP address of Ethernet NIC. The default value is an empty string'', indicating that the default IP address is 192.168.1.100 in the program.
        :param subnet: Subnet mask address of Ethernet NIC. The default value is an empty string'', indicating that 255.255.255.0 is used as the subnet mask.
        :param gateway: Gateway address of Ethernet NIC. The default value is an empty string'', indicating that the last bit of IP address is replaced with 1 as the gateway address.
        """

    def set_addr(self, ip, subnet, gateway):
        """Configures NIC static IP Address.

        :param ip: address of Ethernet NIC. The value is an empty string'', indicating that the default IP address is 192.168.1.100 in the program.
        :param subnet: Subnet mask address of Ethernet NIC. The value is an empty string'', indicating that 255.255.255.0 is used as the subnet mask.
        :param gateway: Gateway address of Ethernet NIC. The value is an empty string'', indicating that the last bit of IP address is replaced with 1 as the gateway address.
        :return: 0 - Successful execution; Other values - Failed execution
        """

    def set_dns(self, primary_dns, secondary_dns):
        """Configures NIC DNS server.

        :param primary_dns: Primary address of DNS server.
        :param secondary_dns: Secondary address of DNS server.
        :return: 0 - Successful execution; Other values - Failed execution
        """

    def set_up(self):
        """Enables NIC and then NIC processes network interfaces and messages normally."""

    def set_down(self):
        """Disables NIC and then NIC no longer processes network interfaces and messages."""

    def dhcp(self):
        """Obtains dynamic IP. This method is used in the terminal mode so that IP information can be automatically obtained.

        :return: 0 - Successful execution; Other values - Failed execution
        """

    def ipconfig(self):
        """Obtains NIC network information.

        MAC address, host name, IP address type, IP address, subnet mask, gateway address and DNS server address can be obtained through this method.

        :return: List type. The format is as follows: [(mac, hostname), (iptype, ip, subnet, gateway, primary_dns，secondary_dns)].
        Parameter	Type	Description
        mac	str	mac address and the format is'XX-XX-XX-XX-XX-XX'.
        hostname	str	NIC name
        iptype	str	ip type. 4 indicates IPv4 and 6 indicates IPv6. Currently, only IPv4 is supported.
        ip	str	IP address
        subnet	str	Subnet mask
        gateway	str	Gateway address
        primary_dns	str	Primary address of DNS server
        secondary_dns	str	Secondary address of DNS server
        """

    def set_default_NIC(self, ip):
        """Configures the default NIC.

        :param ip: Default NIC IP address.
        :return: 0 - Successful execution; Other values - Failed execution
        """

    def status(self):
        """Obtains NIC current status.

        :return: Tuple type. The format is as follows: (dev, active, link).
        Parameter	Type	Description
        dev	bool	Whether NIC device is normally connected. True and False respectively indicate that NIC device is connected and is not connected.
        active	bool	Whether NIC is activated. True and False respectively indicate enable and disable, which correspond to set_up and set_down.
        link	bool	Whether the network cable of NIC is connected. True and False respectively indicate the network cable is connected and is not connected.
        """
