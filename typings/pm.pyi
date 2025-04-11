"""
Function:
Power Management
When there is no service being processed, the system is in the sleep status and enters a low-power mode.

Descriptions taken from:
https://python.quectel.com/doc/API_reference/en/syslib/pm.html
"""


def create_wakelock(lock_name, name_size):
    """Creates a wakelock.

    Note: BC25 series module does not support this method.

    :param lock_name: String type. Custom lock name.
    :param name_size: Integer type. Length of lock_name. It is an optional parameter.
    :return: The wakelock ID: Successful execution;-1 - Failed execution
    """


def delete_wakelock(lpm_fd):
    """Delete Wakelock

    Note: BC25 series module does not support this method.

    :param lpm_fd: Integer type. ID of the wakelock to be deleted.
    :return: 0 - Successful execution; Other values - Failed execution
    """


def wakelock_lock(lpm_fd):
    """Sets the specified wakelock to lock status. When there is a locked wakelock, the module will not enter the low power mode.

    Note: BC25 series module does not support this method.

    :param lpm_fd:  Integer type. ID of the wakelock to be locked.
    :return:0 - Successful execution;-1 - Failed execution
    """


def wakelock_unlock(lpm_fd):
    """Releases a wakelock. Only when all wakelocks are released will the module enter the low-power mode.

    Note: BC25 series module does not support this method.

    :param lpm_fd: Integer type. ID of the wakelock to be released.
    :return:0 - Successful execution;-1 - Failed execution
    """


def autosleep(sleep_flag):
    """Sets automatic sleep mode.

    :param sleep_flag: Integer type. 0 - Disable automatic sleep mode; 1 - Enable automatic sleep mode.
    :return:0 - Successful execution;-1 - Failed execution
    """


def get_wakelock_num():
    """Gets the number of created wakelocks.

    Note: BC25 series module does not support this method.

    :return: Integer type. The number of created wakelocks.
    """


def set_psm_time(*args):
    """Set PSM Time

    Only BC25/ECX00U/ECX00E series module supports this method.

    set_psm_time(mode)  # Enables or disables PSM <Mode 2>
    mode - Integer type. Whether to enable PSM.
    0 - Disable PSM
    1 - Enable PSM
    2 - (Only for BC25 series module) Disable PSM and delete all parameters of PSM. If there is a default value, this method will reset the default value. (Please note that if you disable PSM in this way, you must call pm.set_psm_time(tau_uint,tau_time,act_uint,act_time) to enable PSM, because calling pm.set_psm_time(mode) is relatively nonsensical when all PSM parameters are deleted.


    set_psm_time(tau_uint,tau_time,act_uint,act_time)  # Sets and enables PSM <Mode 1>
    tau_uint:
        Unit	Type	Description
        0	int	10 minutes
        1	int	1 hour
        2	int	10 hours
        3	int	2 seconds
        4	int	30 seconds
        5	int	1 minute
        6	int	320 hours
        7	int	Disabled
    tau_time: Integer type. Periodic value of TAU (T3412).
    act_uint:
        Unit	Type	Description
        0	int	2 seconds
        1	int	1 minute
        2	int	6 minutes
        7	int	Disabled
    act_time: Integer type. Periodic value of ATC (T3324).

    The TAU and ATC actually set is the product of the unit value and the periodic value.
    """


def get_psm_time():
    """Get PSM Time

    Only BC25/ECX00U/ECX00E series module supports this method.

    :return: List type - Successful execution
    Parameter	Type	Description
    list[0] int	mode    0- Disable PSM.
                        1- Enable PSM.
                        2- (Only for BC25 series module) Disable PSM and delete all parameters of PSM. If there is a default value, this method will reset the default value.
    list[1]	int	TAU unit
    list[2]	int	Periodic value of TAU
    list[3]	int	ACT unit
    list[4]	int	Periodic value of ACT
    """
