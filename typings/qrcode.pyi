"""
Function:
QR Code Display
Feature introduction: generate a corresponding QR code according to the input content.

Descriptions taken from:
https://python.quectel.com/doc/API_reference/en/medialib/qrcode.html#Display-QR-Code
"""


def show(qrcode_str, magnification, start_x, start_y, Background_color, Foreground_color):
    """Displays QR codes to LCD.

    :param qrcode_str: String type. QR code content.
    :param magnification: Integer type. Magnification. Range: 1–6.
    :param start_x: Integer type. The start x coordinate of the displayed QR code.
    :param start_y: Integer type. The start y coordinate of the displayed QR code.
    :param Background_color: Integer type. Background color. Default value: 0xffff.
    :param Foreground_color: Integer type. Foreground color. Default value: 0x0000.
    :return:
    0 - Successful execution
    -1 - QR code generation failed
    -2 - Magnification failed
    -3 - Display failed
    """
