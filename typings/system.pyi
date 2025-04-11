"""
Function:
This feature is used to configure the system parameter and features.
Applicable modules: EC100Y(V0009) and above; EC600S(V0002) and above.

Descriptions taken from:
https://python.quectel.com/doc/API_reference/en/syslib/system.html
"""


def replSetEnable(flag, **kwargs):
    """Enables or disables interaction protection.

    :param flag: 0 - Disable (default); 1 - Enable; 2 - Query encryption status
    :param kwargs: Password (optional)
    :return: 0 - Successful execution; -1 or errorlist or both - Failed execution;
    """


def replChangPswd(old_password,new_password):
    """Changes the password for interaction protection.

    :param old_password: str, Old password. Length: 6–12 bytes.
    :param new_password: str, New password. Length: 6–12 bytes.
    :return: 0 - Successful execution; -1 or errorlist or both - Failed execution;
    """
