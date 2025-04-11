"""
Function:
This module provides a method for sending AT commands, allowing the QuecPython module to send AT commands through Python code.

Descriptions taken from:
https://python.quectel.com/doc/API_reference/en/syslib/atcmd.html
"""


def sendSync(atcmd, resp, include_str, timeout):
    """Sends an AT command to the module.

    :param atcmd: String type. The AT command to be sent, and '\r\n' should be included.
    :param resp: String type. The string content returned by the AT command.
    :param include_str: String type. Keyword. The specific values are shown in the table below
    Value	Description
    Empty string	Gets all data returned by the AT command (excluding result data such as 'OK') and puts the data into the resp parameter.
    None-empty string	Filter data containing the keyword and puts the data into the resp parameter.
    :param timeout: Integer type. Timeout. Unit: second.
    :return: Returns an integer value. 0 indicates successful execution and other values indicate failed execution.
    """
