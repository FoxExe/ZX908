"""
Function:
utime module gets the current time, measures the time interval and provides the feature of sleep, and realizes subsets of the corresponding CPython module.
See CPython file time for more detailed information: https://docs.python.org/3.5/library/time.html#module-time

Descriptions taken from:
https://python.quectel.com/doc/API_reference/zh/stdlib/utime.html
"""


def localtime(secs=None):
    """Converts a time in seconds to a time in date format and returns it, or returns the local RTC time when secs is provided.

    :param secs: Integer type. The time in seconds.
    :return: (year, month, mday, hour, minute, second, weekday, yearday) - Tuple type.
    Contains year, month, day, hour, minute, second, week, the day of the year.
    Returns the converted time when secs is provided. Returns the local RTC time when secs is not provided.
    The meaning of return values is below：
    Tuple Members	Range	Meaning
    year	Integer type	Year
    month	Integer type, 1–12	Month
    mday	Integer type, 1–31	Day, the date of the month
    hour	Integer type, 0–23	Hour
    minute	Integer type, 0–59	Minute
    second	Integer type, 0–59	Second
    weekday	Integer type, 0–6	Week
    yearday	Integer type	The day of the year
    """

def mktime(date):
    """Converts a time in date format stored in the tuple to a time in seconds and returns it.

    :param date: Tuple type. The time in date format. Format: (year, month, mday, hour, minute, second, weekday, yearday).
    :return: Integer type. The time in seconds.
    """

def time():
    """Returns seconds since the device was enabled."""

def getTimeZone():
    """Gets the current time zone.

    Unit: hour. Range: [-12, 12].
    Negative values indicate the western time zone, positive values indicate the eastern time zone, and 0 indicates the zero time zone.
    """

def setTimeZone(offset):
    """Sets the time zone. After the time zone is set, the local time will change to the time in the corresponding time zone.

    Unite: hour. Range: [-12, 12].
    Negative values indicate the western time zone, positive values indicate the eastern time zone, and 0 indicates the zero time zone.
    """

def ticks_ms():
    """Returns an ascending millisecond counter. It will recount when the value exceeds 0x3FFFFFFF.

    :return: Millisecond count value. The count value itself has no specific meaning and is only suitable for ticks_diff().
    """

def ticks_us():
    """Returns an ascending microsecond counter. It will recount when the value exceeds 0x3FFFFFFF.

    :return: Microsecond count value. The count value itself has no specific meaning and is only suitable for ticks_diff().
    """

def ticks_cpu():
    """Returns an ascending CPU counter. The unit depends on the underlying clock of the hardware platform.

    :return: Count value. The count value itself has no specific meaning and is only suitable for ticks_diff().
    """

def ticks_diff(ticks1, ticks2):
    """Calculates the time interval between calling ticks_ms, ticks_us, or ticks_cpu for the first time and the second time.

    Because the count value of ticks_xxx may be looped, it cannot be directly subtracted so ticks_diff should be called.
    Generally,ticks_diff should be called in the event loop with a timeout.
    The order of ticks2 and ticks1 cannot be reversed, otherwise the result cannot be determined.
    This function should not be used to calculate long intervals, that is, the tick difference between ticks2 and ticks1 cannot exceeds 0x1FFFFFFF, otherwise the result cannot be determined.

    :param ticks1: Tick value obtained by calling ticks_ms, ticks_us, or ticks_cpu for the second time.
    :param ticks2: Tick value obtained by calling ticks_ms, ticks_us, or ticks_cpu for the first time.
    :return: Time interval. The time interval between calling ticks_ms, ticks_us, or ticks_cpu for the first time and the second time. The unit is the same as that of the passed ticks2 and ticks1.
    """

def sleep(seconds):
    """The given seconds of sleep.

    :param seconds: The duration of sleep. Unit: second.
    """

def sleep_ms(ms):
    """The given millisecond of sleep.

    :param ms: The duration of sleep. Unit: millisecond.
    """

def sleep_us(us):
    """The given microsecond of sleep.

    :param us: The duration of sleep. Unit: microsecond.
    """
