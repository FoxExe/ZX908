"""
Function:
A log is a tool used to record the runtime state of an application in program development, as well as help developers diagnose and troubleshoot problems. Developers can quickly identify the root causes of problems and better understand the behaviors and performance of applications by viewing logs. log feature can output different log levels, including the DEBUG level, WARNING level, and ERROR level.

Descriptions taken from:
https://python.quectel.com/doc/API_reference/en/syslib/log.html
"""


# Constant of log level. The most detailed information is recorded at the DEBUG level and this level is usually used in development and debugging.
DEBUG: int = ...
# Constant of log level. The information recorded at the INFO level indicates that everything is running normally.
INFO: int = ...
# Constant of log level. The information recorded at the WARNING level indicates that something unexpected has occurred or potentially harmful events, but the application can continue to function normally.
WARNING: int = ...
# Constant of log level. The information recorded at the ERROR level indicates that an application is no longer able to execute certain functions due to some serious problems.
ERROR: int = ...
# Constant of log level. The information recorded at the CRITICAL level indicates a critical error in the application that may stop the application from running.
CRITICAL: int = ...


def basicConfig(level):
    """Sets the log output level. Default level: log.INFO. The system will only output logs whose levels are greater than or equal to that level.

    :param level: Log level.
    :return: None
    """


def set_output(out):
    """Destination where the logs are output. Currently only uart and usys.stdout are supported.

    :param out: The destination where the logs are output. Set the parameter to a specified serial port or the interaction port. Default value: the interaction port.
    :return: None
    """


def getLogger(name) -> Logger:
    """Gets the log object which supports logs of different levels.

    :param name: String type. The topic of the current log object
    :return: A log handle (log object) with the method of outputting logs.
    """


class Logger(object):

    def __init__(self, name):
        """
        :param name: logger name
        """

    def debug(self, msg):
        """Outputs the DEBUG-level logs.

        :param msg: String type. The content of logs.
        :return:
        """

    def info(self, msg):
        """Outputs the INFO-level logs.

        :param msg: String type. The content of logs.
        :return:
        """

    def warning(self, msg):
        """Outputs the WARNING-level logs.

        :param msg: String type. The content of logs.
        :return:
        """

    def error(self, msg):
        """Outputs the ERROR-level logs.

        :param msg: String type. The content of logs.
        :return:
        """

    def critical(self, msg):
        """Outputs the CRITICAL-level logs.

        :param msg: String type. The content of logs.
        :return:
        """
