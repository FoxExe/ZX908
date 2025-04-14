"""
Function:
This module contains features related to the hardware on a particular circuit board.
Most of the features in this module allow direct and unrestricted access to and control of the hardware on the system.

Descriptions taken from:
https://python.quectel.com/doc/API_reference/en/peripherals/machine.html
"""


class Pin(object):
    """Pin

    Descriptions: https://python.quectel.com/doc/API_reference/en/peripherals/machine.Pin.html)

    Description of GPIO corresponding pin numbers: GPIO pin numbers provided in the document correspond to external pin numbers of the module.
    For example, for EC100Y-CN module, GPIO1 corresponds to pin22, which is an external pin number of the module.
    See the provided hardware documents for external pin numbers of the module.
    """

    def __init__(self, GPIOn, direction, pullMode, level):
        """
        :param GPIOn: Integer type. GPIO number. Click here to view the mapping relationship between GPIO pin numbers and physical pins.
        :param direction: Integer type. I/O mode. IN - Input mode. OUT - Output mode.
        :param pullMode: Integer type. Pull selection mode. Descriptions are as follows:
            PULL_DISABLE - Floating mode
            PULL_PU - Pull-up mode
            PULL_PD - Pull-down mode
        :param level: Integer type. Pin level. 0 - Set pin to low level. 1- Set pin to high level.
        """

    def read(self):
        """This method reads the pin level.

        :return: Pin level. 0 - low level. 1 - high level.
        """

    def write(self, value):
        """This method sets the pin level.

        :param value: Integer type. Pin level. 0 - low level. 1 - high level.
        :return: 0,Successful execution; -1,Failed execution
        """

    def set_dir(self, value):
        """This method sets I/O mode of the pin.

        :param value: Integer type. Pin level. 0 - low level. 1 - high level.
        :return: 0,Successful execution; -1,Failed execution
        """

    def get_dir(self):
        """This method gets I/O mode of the pin.

        :return: I/O mode of pins. 0,Input mode; 1,Output mode.
        """

    GPIO1: int = ...
    GPIO2: int = ...
    GPIO3: int = ...
    GPIO4: int = ...
    GPIO5: int = ...
    GPIO6: int = ...
    GPIO7: int = ...
    GPIO8: int = ...
    GPIO9: int = ...
    GPIO10: int = ...
    GPIO11: int = ...
    GPIO12: int = ...
    GPIO13: int = ...
    GPIO14: int = ...
    GPIO15: int = ...
    GPIO16: int = ...
    GPIO17: int = ...
    GPIO18: int = ...
    GPIO19: int = ...
    GPIO20: int = ...
    GPIO21: int = ...
    GPIO22: int = ...
    GPIO23: int = ...
    GPIO24: int = ...
    GPIO25: int = ...
    GPIO26: int = ...
    GPIO27: int = ...
    GPIO28: int = ...
    GPIO29: int = ...
    GPIO30: int = ...
    GPIO31: int = ...
    GPIO32: int = ...
    GPIO33: int = ...
    GPIO34: int = ...
    GPIO35: int = ...
    GPIO36: int = ...
    GPIO37: int = ...
    GPIO38: int = ...
    GPIO39: int = ...
    GPIO40: int = ...
    GPIO41: int = ...
    GPIO42: int = ...
    GPIO43: int = ...
    GPIO44: int = ...
    GPIO45: int = ...
    GPIO46: int = ...
    GPIO47: int = ...
    IN: int = ...
    OUT: int = ...
    PULL_DISABLE: int = ...
    PULL_PU: int = ...
    PULL_PD: int = ...


class UART(object):
    """UART

    Descriptions: https://python.quectel.com/doc/API_reference/en/peripherals/machine.UART.html

    This class transmits data through the UART.
    When UART1 of EC600M/EC800M/EG912N series module is in flowctl=1 state, modules only map UART1 to different pins but flow control is not enabled.
    """

    def __init__(self, UARTn: int, baudrate: int, databits: int, parity: int, stopbits: int, flowctl: int):
        """
        :param UARTn: Integer type. UART number.
        UART0 - DEBUG PORT
        UART1 - BT PORT
        UART2 - MAIN PORT
        UART3 - USB CDC PORT (BG95M3 series module does not support it.)
        UART4 - STDOUT PORT (Only EC200U/EC600U/EG915U series module supports it. )
        :param baudrate: Integer type. Baud rate. Some common baud rates are supported, like 4800, 9600, 19200, 38400, 57600, 115200 and 230400.
        :param databits: Integer type. Data bit. Range: [5–8]. EC600U/EC200U/EG915U series module only supports 8 data bits.
        :param parity: Integer type. Parity check. 0 – NONE, 1 – EVEN, 2 – ODD.
        :param stopbits: Integer type. Stop bit. Range: [1–2].
        :param flowctl: Integer type. Hardware control flow. 0 – FC_NONE, 1 – FC_HW.
        """

    def any(self):
        """This method gets the size of the unread data in the receiving cache.

        :return: Size of data that is unread in the receiving cache.
        """

    def read(self, nbytes):
        """This method reads data from the UART.

        :param nbytes: Integer type. Size of data to be read.
        :return: Size of data that has been read.
        """

    def write(self, data):
        """This method sends data to the UART.

        :param data: Bytes type. Data to be sent.
        :return: Size of data that has been sent.
        """

    def close(self):
        """This method disables the UART.

        :return: 0 - Successful execution; -1 - Failed execution
        """

    def control_485(self, GPIOn, direction):
        """This method controls the direction of RS-485 communication.

        Before and after sending data through the UART, the specified GPIO is pulled up and down to indicate the direction of RS-485 communication.

        :param GPIOn: Integer type. GPIO numbers to be controlled. See class Pin - Control I/O Pins for pin definitions.
        :param direction: Integer type. Pin level change.
        1 - The pin is pulled high before the data is sent through the UART, and pulled low after the data is sent.
        0 - The pin is pulled low before the data is sent through the UART, and pulled high after the data is sent.
        :return: 0 - Successful execution; -1 - Failed execution
        """

    def set_callback(self, fun):
        """This method sets the callback function of the UART. This callback function will be triggered when data is received on the UART.

        :param fun: Callback function of the UART. Prototype: `fun(result_list)`
        Parameter of the callback function:
        result_list[0]：Whether the data is received successfully, 0 - Received successfully; Others - Receiving failed
        result_list[1]：Port for receiving data.
        result_list[2]：How much data is returned.
        :return: 0 - Successful execution; -1 - Failed execution
        """

    UART0: int = ...
    UART1: int = ...
    UART2: int = ...
    UART3: int = ...
    UART4: int = ...


class Timer(object):
    """Control Hardware Timers

    Descriptions: https://python.quectel.com/doc/API_reference/en/peripherals/machine.Timer.html

    This class provides the method of controlling hardware timer.
    Note: For Timer0 to Timer3, each of them can only execute one task at the same time and multiple objects cannot use the same timer.
    """

    def __init__(self, Timern):
        """
        :param Timern: Integer type. Timer number. Timer0 to Timer3 are supported.
        """

    def start(self, period, mode, callback):
        """This method enables the timer.

        :param period: Integer type. Interruption period. Unit: millisecond. The period is greater than or equal to 1.
        :param mode: Integer type. Running mode.
        ONE_SHOT - Single mode indicating the time is executed for only once.
        PERIODIC - Periodic mode indicates periodic execution.
        :param callback: Function type. Timer execution function.
        :return: 0 - Successful execution; -1 - Failed execution
        """

    def stop(self):
        """This method disables the timer.

        :return: 0 - Successful execution; -1 - Failed execution
        """

    Timer0: int = ...
    Timer1: int = ...
    Timer2: int = ...
    Timer3: int = ...
    ONE_SHOT: int = ...  # Single mode indicating the time is executed for only once.
    PERIODIC: int = ...  # Periodic mode indicates periodic execution.


class ExtInt(object):
    """This class configures I/O pins to interrupt when external events occur.

    Descriptions: https://python.quectel.com/doc/API_reference/zh/peripherals/machine.ExtInt.html
    """

    def __init__(self, GPIOn, mode, pull, callback):
        """
        :param GPIOn: Integer type. GPIO pin number to be controlled. See Pin Modules for pin definitions (excluding BG95M3). Click here to view pin correspondences of BG95M3 platform.
        :param mode: Integer type. Trigger mode. IRQ_RISING – Trigger rising edge; IRQ_FALLING – Trigger falling edge; IRQ_RISING_FALLING – Trigger rising and falling edge
        :param pull: Integer type. Pull selection mode. PULL_PU – Pull-up mode; PULL_PD – Pull-down mode; PULL_DISABLE – Floating mode
        :param callback: Integer type. The interrupt triggers the callback function.
        arguments is A tuple with the length of 2 bytes
        args[0]: GPIO number
        args[1]: Trigger edge (0: rising edge 1: falling edge)
        """

    def enable(self):
        """This method enables interrupts that is to enable external interrupt of an extint object.

        When the interrupt pin receives the rising edge signal or falling edge signal, it will call a callback function to execute the interrupt.

        :return: 0 - Successful execution; -1 - Failed execution
        """

    def disable(self):
        """This method disables interrupts associated with extint objects.

        :return: 0 - Successful execution; -1 - Failed execution
        """

    def line(self):
        """This method reads the line number mapped by the pin.

        :return: The line number mapped by the pin.
        """

    def read_count(self, is_reset):
        """This method returns number of times an interrupt was triggered.

        :param is_reset: Integer type. Whether to reset the count after reading. 0 indicates that the count is not resetted and 1 indicates a count resetting.
        :return: The list [rising_count, falling_count]
        rising_count: Number of times that the rising edge triggers an interrupt
        falling_count: Number of times that the falling edge triggers an interrupt
        """

    def count_reset(self):
        """This method clears number of times an interrupt is triggered.

        :return: 0 - Successful execution; -1 - Failed execution
        """

    def read_level(self):
        """This method reads the current pin level.

        :return: Pin level. 0 - low level; 1 - high level.
        """


class RTC(object):
    """This class provides methods of getting and setting RTC.

    Descriptions: https://python.quectel.com/doc/API_reference/zh/peripherals/machine.RTC.html

    For BC25PA series module, it provides the feature of waking up modules from deep sleep and software power-off state.
    Only EC600U and EC200U series modules support automatic power-on. It means that if you power off the module after RTC alarm is set, the module will power on automatically when the alarm time expires.
    """

    def __init__(self):
        pass

    def datetime(self, args: tuple = ()):
        """This method sets or gets RTC time.

        If this function contains parameters, this method sets the time otherwise these methods gets the time.
        When setting the time, you need not set week. microsecond is reserved, and it is not currently used and its default value is 0.

        :param args: (year, month, day, week, hour, minute, second, microsecond)
        year - Integer type. Year.
        month - Integer type. Month. Range: [1–12].
        day - Integer type. Day. Range: [1–31].
        week - Integer type. Week. Range: [0–6]. 0 indicates Sunday. 1 to 6 indicates Monday to Saturday respectively. This parameter is reserved when setting time and it only takes effect when getting the time.
        hour - Integer type. Hour. Range: [0–23].
        minute - Integer type. Minute. Range: [0–59].
        second - Integer type. Second. Range: [0–59].
        microsecond - Integer type. Microsecond. This parameter is reserved and it is not currently used. Set to 0 when you set the time.
        :return: A tuple containing a date and time: (year, month, day, week, hour, minute, second, microsecond); Set RTC time: 0 - Successful execution; -1 - Failed execution
        """

    def set_alarm(self, data_e):
        """This method sets RTC expiration time. The registered callback function will be called when the time expires.

        Note: This method supports EC600U, EC200U, EC600N, EC800N and BC25 series modules.

        :param data_e: (year, month, day, week, hour, minute, second, microsecond)
        :return: 0 - Successful execution; -1 - Failed execution
        """

    def register_callback(self, fun):
        """This method registers callback function of RTC alarm.

        Note: This method supports EC600U, EC200U, EC600N, EC800N and BC25 series modules.

        :param fun: Function type. Callback function of RTC alarm.
        :return: 0 - Successful execution; -1 - Failed execution
        """

    def enable_alarm(self, on_off):
        """This method enables and disables RTC alarm.

        This method supports EC600U, EC200U, EC600N, EC800N and BC25 series modules.
        For BC25 series module, only when the callback function is set can RTC alarm be enabled.

        :param on_off: Integer type. 1 means to enable RTC alarm and 0 means to disable RTC alarm.
        :return: 0 - Successful execution; -1 - Failed execution
        """


class I2C(object):
    """Two-wire Serial Protocol

    Descriptions: https://python.quectel.com/doc/API_reference/zh/peripherals/machine.I2C.html

    This class is designed for the two-wire serial protocol for communication between devices.
    """

    def __init__(self, I2Cn, mode):
        """
        :param I2Cn: Integer type. I2C channel index number.
        I2C0 : 0 - Channel 0
        I2C1 : 1 - Channel 1
        I2C2 : 2 - Channel 2
        :param mode: Integer type. I2C working mode.
        STANDARD_MODE : 0 - Standard mode
        FAST_MODE ：1 - Fast mode
        """

    def read(self, slaveaddress, addr,addr_len, r_data, datalen, delay):
        """This method reads data to I2C bus.

        :param slaveaddress: Integer type. I2C device address.
        :param addr: Bytearray type. I2C register address.
        :param addr_len: Integer type. Register address length.
        :param r_data: Bytearray type. Byte array for receiving data.
        :param datalen: Integer type. Length of byte array.
        :param delay: Integer type. Delay. Data conversion buffer time (unit: ms).
        :return: 0 - Successful execution; -1 - Failed execution
        """

    def write(self, slaveaddress, addr, addr_len, data, datalen):
        """This method writes data to I2C bus.

        :param slaveaddress: Integer type. I2C device address.
        :param addr: Bytearray type. I2C register address.
        :param addr_len: Integer type. Register address length.
        :param data: Bytearray type. Data to be written.
        :param datalen: Integer type. Length of data to be written.
        :return: 0 - Successful execution; -1 - Failed execution
        """

    I2C0: int = ...  # EC100Y/EC600U/EC200U/EC200A/BC25/EC800N/BG95M3/EC600M/EG915U/EC800M
    I2C1: int = ...  # EC600S/EC600N/EC600U/EC200U/BC25/BG95M3/EC600M/EG915U/EC800M/EG912N
    I2C2: int = ...  # BG95M3/EC600M
    STANDARD_MODE: int = ...  # All modules
    FAST_MODE: int = ...  # All modules


class I2C_simulation(object):
    """This class is designed for GPIO simulating standard I2C protocol.

    Descriptions: https://python.quectel.com/doc/API_reference/zh/peripherals/machine.I2C_simulation.html

    Except for creating the object, all other operations (read and write) are consistent with I2C communication.
    """

    def __init__(self, GPIO_clk, GPIO_sda, CLK):
        """
        :param GPIO_clk: Integer type. CLK pin of I2C (See definitions in machine.Pin for GPIO pin numbers that need to be controlled).
        :param GPIO_sda: Integer type. SDA pin of I2C (See definitions in machine.Pin for GPIO pin numbers that need to be controlled).
        :param CLK: Integer type. Frequency of I2C. Range: [1, 1000000 Hz].
        """

    def read(self, slaveaddress, addr,addr_len, r_data, datalen, delay):
        """This method reads data to I2C bus.

        :param slaveaddress: Integer type. I2C device address.
        :param addr: Bytearray type. I2C register address.
        :param addr_len: Integer type. Register address length.
        :param r_data: Bytearray type. Byte array used to receive data.
        :param datalen: Integer type. Length of byte array.
        :param delay: Integer type. Delay. Data conversion buffer time (unit: ms).
        :return: 0 - Successful execution; -1 - Failed execution
        """

    def write(self, slaveaddress, addr, addr_len, data, datalen):
        """This method writes data to I2C bus.

        :param slaveaddress: Integer type. I2C device address.
        :param addr: Bytearray type. I2C register address.
        :param addr_len: Integer type. Register address length.
        :param data: Bytearray type. Data to be written.
        :param datalen: Integer type. Length of data to be written.
        :return: 0 - Successful execution; -1 - Failed execution
        """


class SPI(object):
    """Serial Peripheral Interface Bus Protocol

    Descriptions: https://python.quectel.com/doc/API_reference/zh/peripherals/machine.SPI.html

    This class provides bus protocol of serial peripheral interface (SPI) .
    """

    def __init__(self, port, mode, clk):
        """BC25 series module does not support SPI working mode of value 1 or 2.

        :param port: Integer type. Channel selection: [0,1].
        :param mode: SPI working mode.
        Clock polarity CPOL: The pin level of clock signal SCLK when SPI is idle (0: low level; 1: high level)
        0 : CPOL=0, CPHA=0
        1 : CPOL=0, CPHA=1
        2: CPOL=1, CPHA=0
        3: CPOL=1, CPHA=1
        :param clk: Clock frequency.
        EC600N/EC600S/EC800N/BG95M3/EC600M/EC800M/EG912N:
        0 : 812.5 kHz
        1 : 1.625 MHz
        2 : 3.25 MHz
        3 : 6.5 MHz
        4 : 13 MHz
        5 : 26 MHz
        6：52 MHz
        EC600U/EC200U/EG915U:
        0 : 781.25 kHz
        1 : 1.5625 MHz
        2 : 3.125 MHz
        3 : 5 MHz
        4 : 6.25 MHz
        5 : 10 MHz
        6 : 12.5 MHz
        7 : 20 MHz
        8 : 25 MHz
        9 : 33.33 MHz
        BC25：
        0 : 5 MHz
        X : X MHz (X in [1,39])
        """

    def read(self, recv_data, datalen):
        """This method reads data.

        :param recv_data: Bytearray type. An array used to receive data.
        :param datalen: Integer type. Length of the data to be read.
        :return: 0 - Successful execution; -1 - Failed execution
        """

    def write(self, data, datalen):
        """This method writes data.

        :param data: Bytearray type. Data to be written.
        :param datalen: Integer type. Length of data to be written.
        :return: 0 - Successful execution; -1 - Failed execution
        """

    def write_read(self, r_data, data, datalen):
        """This method writes and reads data.

        :param r_data: Bytearray type. An array used to receive data.
        :param data: Bytearray type. Data to be sent.
        :param datalen: Integer type. Length of data to be read.
        :return: 0 - Successful execution; -1 - Failed execution
        """


class SoftSPI(object):
    """Software Implementation of SPI Bus Protocol.

    Descriptions: https://python.quectel.com/doc/API_reference/zh/peripherals/machine.SoftSPI.html

    This class provides bus protocol of Serial Peripheral Interface (SPI).
    EC600E/EC800E module supports this feature.
    """


    def __init__(
            self,
            gpio_clk,
            gpio_cs,
            gpio_mosi,
            gpio_miso=None,
            wire_type=WIRE_4,
            speed=1,
            mode=0,
            cs_active_lvl=LOW
    ):
        """
        :param gpio_clk: Integer type. The GPIO corresponding to the CLK.
        :param gpio_cs: Integer type. The GPIO corresponding to the CS.
        :param gpio_mosi: Integer type. The GPIO corresponding to the MOSI.
        :param gpio_miso: Integer type. The GPIO corresponding to the MISO. For 3-wire SPI, this parameter can be omitted and the MOSI can be used for receiving and sending data.
        :param wire_type: Integer type. Set SPI to 3-wire SPI or 4-wire SPI. WIRE_3: 3-wire SPI. WIRE_4: 4-wire SPI. Default value: 4-wire SPI.
        :param speed: Integer type. Transmission speed. 0: 50 kHz. 1: 100 kHz. Default value: 100 kHz.
        :param mode: Integer type. SPI mode. Range: 0–3. Default value: 0.
        0 : CPOL=0, CPHA=0
        1 : CPOL=0, CPHA=1
        2: CPOL=1, CPHA=0
        3: CPOL=1, CPHA=1
        :param cs_active_lvl: Integer type. CS active level. LOW: low level. HIGH: high level. Default value: low level.
        """

    def read(self, recv_data, datalen):
        """This method reads data.

        :param recv_data: Bytearray type. An array used to receive data.
        :param datalen: Integer type. Length of the data to be read.
        :return: 0 - Successful execution; -1 - Failed execution
        """

    def write(self, data, datalen):
        """This method writes data.

        :param data: Bytes type. Data to be written.
        :param datalen: Integer type. Length of data to be written.
        :return: 0 - Successful execution; -1 - Failed execution
        """

    def write_read(self, r_data, data, datalen):
        """This method writes and reads data.

        For 3-wire SPI, in the communicating process, MOSI is set to the output mode first and data will be sent.
        And then MOSI is set to the input mode and the datalen bytes of data will be read.

        :param r_data: Bytearray type. An array used to receive data.
        :param data: Bytes type. Data to be sent.
        :param datalen: Integer type. Length of data to be read.
        :return: 0 - Successful execution; -1 - Failed execution
        """

    WIRE_3: int = ...
    WIRE_4: int = ...
    LOW: int = ...


class LCD(object):
    """LCD Driver

    Descriptions: https://python.quectel.com/doc/API_reference/zh/peripherals/machine.LCD.html

    This class controls LCD.
    Supported module models are as follows:
    EC200U series module, EC600U series module, EC600N series module, EC800N series module,
    EC600M-CNLA, EC600M-CNLE
    EC800M-CNLA, EC800M-CNLE, EC800M-CNGA, EC800G-CNGA
    EG912N-ENAA, EG912U-GLAA
    EG915N-EUAG, EG915U-EUAB
    """

    def __init__(self):
        pass

    def lcd_init(self, *args):
        """This method initializes LCD.

        :param args: two Interface args list as below:

        Interface 1: The device connects to LCM interfaces of modules: (lcd_init_data, lcd_width, lcd_hight, lcd_clk, data_line, line_num, lcd_type, lcd_invalid, lcd_display_on, lcd_display_off, lcd_set_brightness)
        lcd_init_data	bytearray	Write command for LCD initialization.
        lcd_width	int	Width of LCD screen. The width cannot exceed 500 pixels.
        lcd_hight	int	Height of LCD screen. The height cannot exceed 500 pixels.
        lcd_clk	int	LCD SPI clock frequency:
        6500: 6.5 MHz
        13000: 13 MHz
        26000: 26 MHz
        52000: 52 MHz
        data_line	int	Number of data lines. Parameter values are 1 and 2.
        line_num	int	Number of lines. Parameter values are 3 and 4.
        lcd_type	int	Screen type. 0-rgb; 1-fstn.
        lcd_invalid	bytearray	Write command for LCD region settings.
        lcd_display_on	bytearray	Write command for turning on the LCD screen.
        lcd_display_off	bytearray	Write command for turning off the LCD screen.
        lcd_set_brightness	bytearray	Write command for LCD screen brightness:None indicates that LCD_BL_K controls brightness.

        Interface 2: The device connects to module SPI: (lcd_init_data, lcd_width, lcd_hight, lcd_clk, data_line, line_num, lcd_type, lcd_invalid, lcd_display_on, lcd_display_off, lcd_set_brightness, lcd_interface, spi_port, spi_mode, cs_pin, dc_pin, rst_pin)
        lcd_init_data	bytearray	Write command for LCD initialization.
        lcd_width	int	Width of LCD screen. The width cannot exceed 500 pixels.
        lcd_hight	int	Height of LCD screen. The height cannot exceed 500 pixels.
        lcd_clk	int	See machine.SPI 漏了超链接 for creating SPI objects parameter descriptions.
        data_line	int	Number of data lines. Parameter values are 1 and 2.
        line_num	int	Number of lines. Parameter values are 3 and 4.
        lcd_type	int	Screen type. 0-rgb; 1-fstn.
        lcd_invalid	bytearray	Write command for LCD region settings.
        lcd_display_on	bytearray	Write command for turning on LCD screen.
        lcd_display_off	bytearray	Write command for turning off LCD screen.
        lcd_set_brightness	bytearray	Write command for LCD screen brightness:
        None indicates that LCD_BL_K controls the brightness.
        lcd_interface	int	LCD interface type. 0 - LCM; 1 - SPI
        spi_port	int	Channel selection [0,1]. See machine.SPI 漏了超链接 for port description.
        spi_mode	int	SPI work mode (Work mode 0 is commonly used):
        CPOL: The level of clock signal of SCLK when SPI is idle (0: low level; 1: high level)
            0 : CPOL=0, CPHA=0
            1 : CPOL=0, CPHA=1
            2 : CPOL=1, CPHA=0
            3 : CPOL=1, CPHA=1
        cs_pin	int	CS pin. See machine.Pin for descriptions of GPIO pin number.
        dc_pin	int	DC pin. See machine.Pin for descriptions of GPIO pin number.
        rst_pin	int	RST pin. See machine.Pin for descriptions of GPIO pin number.

        :return: as below:
        0 - Successful execution.
        -1 - LCD Initialized.
        -2 - Parameter error. Parameter is empty or too large (more than 1000 pixels).
        -3 - Failed cache request.
        -5 - Parameter configuration error.
        """

    def mipi_init(self, initbuf, **kwargs):
        """This method initializes MIPI and passes parameters according to key-value pairs.

        Please set parameters according to initialization parameters provided by the screen manufacturer.
        1. Only EC200U and EC600U series modules support this function.
        2. In the parameter list below, initbuf is a required parameter. Other parameters are optional parameters. If values are consistent with default values, you needn’t pass this parameter.

        :param initbuf: as below:
        initbuf	bytearray	Required. Write command for passing MIPI.

        :param kwargs:
        width	int	Width of LCD screen. Default value: 480. Example: width = 400.
        hight	int	Height of LCD screen. Default value: 854. Example: height = 800.
        bpp	int	Bits per pixel. Default value: 16.
        DataLane	int	Data channel. Default value: 2.
        MipiMode	int	Mode:
            0: DSI_VIDEO_MODE
            1: DSI_CMD_MODE
            Default value: 0
        PixelFormat	int	Pixel format:
            0: RGB_PIX_FMT_RGB565
            16: RGB_PIX_FMT_RGB888
            32: RGB_PIX_FMT_XRGB888
            48: RGB_PIX_FMT_RGBX888
        Default value: 0
        DsiFormat	int	DSI format:
            0: DSI_FMT_RGB565
            1: DSI_FMT_RGB666
            2: DSI_FMT_RGB666L
            3: DSI_FMT_RGB888
        Default value: 0
        TransMode	int	Transform mode:
            0: DSI_CMD
            1: DSI_PULSE
            2: DSI_EVENT
            3: DSI_BURST
        Default value: 3
        RgbOrder	int	RGB order:
            0: RGB
            8: BGR
            Default value: 8
        BllpEnable	bool	Enable blank low power. Default value: true.
        HSync	int	Horizontal synchronization. Default value: 10.
        HBP	int	Horizontal back porch. Default value: 10.
        HFP	int	Horizontal front porch. Default value: 10.
        VSync	int	Vertical Synchronization. Default value: 4.
        VBP	int	Vertical back porch. Default value: 10.
        VFP	int	Vertical front porch. Default value: 14.
        FrameRate	int	Frame rate. Default value: 60.
        TESel	bool	TE selection. Default value: false.
        RstPolarity	int	Reset polarity. Default value: 1.
        :return: 0 - Successful execution; Error codes - Failed execution
        """

    def lcd_clear(self, color):
        """This method clears LCD screen.

        :param color: String type in hexadecimal. The color used to clear the LCD screen.
        :return: 0 - Successful execution; -1 - Failed execution
        """

    def lcd_write(self, color_buffer, start_x, start_y, end_x, end_y):
        """This method writes LCD screen in a specified area.

        :param color_buffer: Bytearray type. Cache of screen color value.
        :param start_x: Integer type. The start x coordinate.
        :param start_y: Integer type. The start y coordinate.
        :param end_x: Integer type. The end x coordinate.
        :param end_y: Integer type. The end y coordinate.
        :return: as below:
        0 - Successful execution.
        -1 - LCD screen is not initialized.
        -2 - Width and height setting errors.
        -3 - Empty data cache.
        """

    def lcd_brightness(self, level):
        """This method sets the screen brightness level.

        :param level: Integer type. Brightness level. The description is as follows:
        lcd_set_brightness in lcd.lcd_init() will be called. If the parameter is None, the brightness is controlled by LCD_BL_K. Range: [0,5].

        :return: 0 - Successful execution; -1 - Failed execution
        """

    def lcd_display_on(self):
        """This method turns on the screen display. lcd_display_on in lcd.lcd_init() will be called after you call this interface.

        :return: 0 - Successful execution; -1 - Failed execution
        """

    def lcd_display_off(self):
        """This method turns off the screen display. lcd_display_off in lcd.lcd_init() will be called after you call this interface.

        :return: 0 - Successful execution; -1 - Failed execution
        """

    def lcd_write_cmd(self, cmd_value, cmd_value_len):
        """This method writes commands.

        :param cmd_value: String type in hexadecimal. Command value.
        :param cmd_value_len: Integer type. Command value length.
        :return: 0 - Successful execution; Other Values - Failed execution
        """

    def lcd_write_data(self, data_value, data_value_len):
        """This method writes commands.

        :param data_value: String type in hexadecimal. Data value.
        :param data_value_len: Integer type. Data value length.
        :return: 0 - Successful execution; Other Values - Failed execution
        """

    def lcd_show(self, file_name, start_x, start_y, width, hight):
        """This method displays images by reading files.

        This file is a bin file generated by Image2Lcd. If the image header file is checked, you needn’t to enter width and height.

        :param file_name: String type. Image name to be displayed.
        :param start_x: Integer type. The start x coordinate.
        :param start_y: Integer type. The start y coordinate.
        :param width: Integer type. Image width (If the image file contains header information, you can leave image width blank).
        :param hight: Integer type. Image height (If the image file contains header information, you can leave image height blank).
        :return: 0 - Successful execution; Other Values - Failed execution
        """

    def lcd_show_jpg(self, file_name, start_x, start_y):
        """This method displays JPEG images by reading files.

        :param file_name: String type. Image name needs to be displayed.
        :param start_x: Integer type. The start x coordinate.
        :param start_y: Integer type. The start y coordinate.
        :return: 0 - Successful execution; Other Values - Failed execution
        """


class WDT(object):
    """Watchdog Timer

    Descriptions: https://python.quectel.com/doc/API_reference/zh/peripherals/machine.WDT.html

    This class provides system restart operation when application program exception occurs.
    """

    def __init__(self, period):
        """Creates a software watchdog object.

        :param period: Integer type. Set software watchdog detection time. Unit: second.
        """

    def feed(self):
        """This method feeds the watchdog.

        :return: Returns integer 0 when the execution is successful.
        """

    def stop(self):
        """This method disables the software watchdog.

        :return: Returns integer 0 when the execution is successful.
        """


class KeyPad(object):
    """Matrix Keyboard

    Descriptions: https://python.quectel.com/doc/API_reference/zh/peripherals/machine.KeyPad.html

    This class provides the matrix keyboard interface.
    EC600SCN_LB, EC800NCN_LA, EC600NCN_LC, EC200UCN_LB, EC600UCN_LB, EC600MCN_LA, EC800MCN_LA, EC800MCN_GA, EG912NEN_AA series module is supported this feature.
    """

    def __init__(self, row, col):
        """
        If you do not set the row and column value, the default value is 4X4.

        :param row: Integer type. Row number. It shall be greater than 0 and cannot exceed the maximum value supported by the module.
        :param col: Integer type. Column number. It shall be greater than 0. The value cannot exceed the maximum value supported by the module.
        """

    def init(self):
        """This method initializes keypad settings.

        :return: 0 - Successful execution; -1 - Failed execution
        """

    def set_callback(self, usrFun):
        """This method sets callback function.

        After the external keyboard button is connected to the module, this callback function will be triggered when the external keyboard button is pressed and released.

        :param usrFun: Matrix keyboard callback function. Prototype: `usrFun(result_list)`
        Parameter of callback function:
        result_list[0]: Key status (1 indicates the button is pressed and 0 indicates the button is released).
        result_list[1]: Row number
        result_list[2]: Column number

        :return: 0 - Successful execution; -1 - Failed execution
        """

    def deinit(self):
        """This method deinitializes to release initialized resources and callback function settings.

        :return: 0 - Successful execution; -1 - Failed execution
        """
