"""
Function:
This feature is used for advanced operations of files.

Descriptions taken from:
https://python.quectel.com/doc/API_reference/en/syslib/ql_fs.html
"""


def path_exists(file_path):
    """Query Whether File or Folder Exists

    :param file_path: String type. The absolute path of the file or folder.
    :return: True - The file or folder exists.; False - The file or folder does not exist.
    """


def path_dirname(file_path):
    """Get Folder or File Path

    :param file_path: String type. The absolute path of the file or folder.
    :return: String type. File or folder path.
    """


def mkdirs(dir_path):
    """Creates a folder recursively and configures a folder path.

    :param dir_path: String type. The absolute path of the folder to be created.
    :return:
    """


def rmdirs(dir_path):
    """Delete Folder

    :param dir_path: String type. The absolute path of the folder to be created.
    :return:
    """


def path_getsize(file_path):
    """

    :param file_path: String type. The absolute path of the file or folder.
    :return: An integer. Unit: byte.
    """


def touch(file, data):
    """Creates a file or updates file data. If the configured file path already exists, update the file content. If the configured file path does not exist, create a file and write the file content.

    :param file: String type. The absolute path of the file.
    :param data: Dict type. The data to be written. Currently only files in JSON format are supported.
    :return: 0 - Successful execution; -1 - Failed execution
    """


def read_json(file):
    """Files in JSON format will be read directly and returned. The data of string type will be returned for files in other formats.

    :param file: String type. The absolute path of files or folders.
    :return: Dictionary type - Successful execution; None - Failed execution
    """


def file_copy(dst, src):
    """Copies files from the source path to the target path.

    :param dst: String type. The target file path.
    :param src: String type. The source file path.
    :return: True - Successful execution
    """
