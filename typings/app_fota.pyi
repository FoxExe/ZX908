"""
Function:
The app_fota module is used for user file upgrades.

Descriptions taken from:
https://python.quectel.com/doc/API_reference/en/syslib/app_fota.html
"""


class new(object):

    def __init__(self):
        """Creates an app_fota object."""

    def download(self, url, file_name):
        """Downloads a single file.

        :param url: String type. The URL of the file to be downloaded.
        :param file_name: String type. The absolute path of the local file to be upgraded.
        :return: 0-Successful execution; -1-Failed execution.
        """

    def bulk_download(self, info):
        """Downloads bulk files.

        :param info: List type. The bulk download lists. Each element of the list is a dictionary containing url and file_name.
        :return: Returns the list of failed downloads in list type when the download fails.Returns NULL when the download succeeds.
        """

    def set_update_flag(self):
        """Sets the upgrade flag.

        fter the upgrade flag is set, call the restart interface to restart the module.
        After that, the upgrade process can be started.
        You can enter the application once the upgrade completes.
        """
