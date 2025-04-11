"""
Function:
fota provides the feature of firmware upgrade.

Descriptions taken from:
https://python.quectel.com/doc/API_reference/en/syslib/fota.html
"""


class fota(object):
    """
    EC600N/EC800N/EG912N/EC600M/EC800M/EG810M series module does not support to disable the feature that the module restarts automatically after the upgrade package is downloaded.
    EC600NCNLC/EC600NCNLF/EG912N/EC600U/EC200U/EG915U/EG912U/EC800G/EC600E/EC800E series module supports the features related to local upgrade.
    """

    def __init__(self, reset_disable=1):
        """Creates a FOTA object.

        :param reset_disable: Optional parameter. Whether to disable the feature that the module restarts automatically after the upgrade package is downloaded. 1–Disable; Omitted/0–Enable
        """

    def httpDownload(self, url1, url2, callback):
        """Download, write and verify the upgrade package and restart the module to complete the upgrade.

        Note: For EC600N/EC800N/EG912N/EC600M/EC800M/EG810M/BC25 series module, return values only indicate successful or failed execution of this interface. The upgrade status and results are returned in callback. For other series modules, 0 indicates successful download and verification. -1 indicates failed download and verification.

        :param url1: String type. Optional parameter. URL of the upgrade package. This URL can be in HTTP or FTP format. Note: Only EC200A series module supports the URL in FTP format.
        :param url2: String type. Optional parameter. URL of the upgrade package of the second stage in mini FOTA upgrades. Note: This parameter needs to be passed only in mini FOTA upgrades and it is prohibited to be passed in DFOTA upgrades. Mini FOTA upgrade is a special firmware upgrade method for small storage modules and it is divided into two stages. DFOTA upgrades only have one stage. Only EC600N/EC800N/EG912N/EC600M/EC800M/EG810M series module supports mini FOTA upgrades.
        :param callback: Function type. Optional parameter. This callback function displays the download progress and status. Note: In mini FOTA upgrades, the callback function is not supported. Parameter descriptions of callback function are as follows.
        Parameter	Type	Description
        args[0]	int	Download status. 0/1/2 – Successful download; Other values – Failed download.
        args[1]	int	Download progress. (Note: For EC600N/EC800N/EG912N series module, it indicates percentage when the download status is successful and indicates error codes when the download status is failed. )
        :return: 0 - Successful execution; -1 - Failed execution
        """

    def apn_set(self, fota_apn, ip_type, fota_user, fota_password):
        """Sets APN information used in FOTA download.

        :param fota_apn: String type. Optional parameter. APN.
        :param ip_type: Integer type. Optional parameter. IP type: 0-IPv4; 1-IPv6.
        :param fota_user: String type. Optional parameter. Username.
        :param fota_password: String type. Optional parameter. Password.
        :return:0 - Successful execution; -1 - Failed execution
        """

    def download_cancel(self):
        """Cancels the FOTA upgrade package download in progress.

        :return:0 - Successful execution; -1 - Failed execution
        """

    def write(self, bytesData, file_size):
        """Writes data stream of the upgrade package.

        :param bytesData: Bytes type. The content data of the upgrade package.
        :param file_size: Integer type. Total size of upgrade package files. Unit: byte.
        :return:0 - Successful execution; -1 - Failed execution
        """

    def flush(self):
        """Refreshes data in the RAM to flash.

        Because the size of the upgrade package files is not necessarily an integer multiple of the RAM size in the code, fota_obj.flush needs to be called to write data in the RAM to flash after the last call of fota_obj.write.

        :return: 0 - Successful execution; -1 - Failed execution
        """

    def verify(self):
        """Verifies the upgrade package.

        :return: 0 - Successful execution; -1 - Failed execution
        """
