"""
Function:
uos module contains file system access and mounting building, and realizes subsets of the corresponding CPython module. See CPython file os for more detailed information.

Descriptions taken from:
https://python.quectel.com/doc/API_reference/zh/stdlib/uos.html
"""
from typing import Callable


def remove(path: str) -> None:
    """Deletes the file.

    :param path: String type. The file name.
    """

def chdir(path) -> None:
    """Changes the current directory.

    :param path: String type. The directory name.
    """

def getcwd() -> str:
    """Gets the current path.

    :return: The return value is in string type, which indicates the current path.
    """

def listdir(dir: str = '/') -> tuple:
    """If the parameter is not provided, the current directory file will be listed. Otherwise, the specified directory file will be listed.

    :param dir: String type. An optional parameter indicates the directory name. Default directory: ‘/’ .
    :return: The return value is in tuple type, which indicates listing all existing objects under the path (directories and files).
    """

def mkdir(path: str) -> None:
    """Creates a directory.

    :param path: indicates the name of the directory to be created. It is in the relative path of the directory.
    """

def rename(old_path: str, new_path: str) -> None:
    """Renames the file.

    :param old_path: String type. The old file or directory name.
    :param new_path: String type. The new file or directory name.
    """

def rmdir(path) -> None:
    """Deletes the specified directory.

    :param path: String type. The directory name. It is in the relative path of the directory.
    """

def ilistdir(dir: str = '') -> tuple:
    """This function returns an iterator that generates the 3-tuple corresponding to the listed entry.

    :param dir: String type. An optional parameter indicating the directory name. If the parameter is not provided, the current directory will be listed by default. Otherwise the directory specified by dir will be listed.
    :return: This function returns an iterator that generates the 3-tuple corresponding to the listed entry.
    The tuple has the form of (name, type, inode[, size]):
    name - String type. The name of the entry. If dir is a byte object, the name is in byte type;
    type - Integer type. The type of the entry. 0x4000 indicates the directory, 0x8000 indicates the regular file;
    inode - is an integer corresponding to the index node of the file, and may be 0 for file systems that don’t have such a notion;
    Some modules may return a 4-tuple that includes the entry's size. For file entries, size is an integer representing the size of the file. If it is unknown, the value will be -1. Its meaning is currently undefined for the directory entry.
    """

def stat(path) -> tuple:
    """Gets the status of the file or directory.

    :param path: String type. The name of the file or directory.
    :return: The return value is a tuple with the form of:
    mode – inode protection mode
    ino – inode node number
    dev – inode device
    nlink – inode number of links
    uid – User ID of the owner
    gid – Group ID of the owner
    size – Size of the file. Unit: byte
    atime – Last access time
    mtime – The last modification time
    ctime – "ctime" reported by the operating system. On some systems it is the latest time of meta-data changing, on others it is the creation time. See the document of the module for details.
    """

def statvfs(path: str) -> tuple:
    """Gets the status of the file system.

    :param path: String type. The name of the file or directory.
    :return: Returns a tuple with the file system information:
    f_bsize – Block size of the file system. Unit: byte.
    f_frsize – Fragment size. Unit: byte.
    f_blocks – Number of data blocks in the file system.
    f_bfree – Number of available blocks.
    f_bavai – Number of available blocks for non-administrator.
    f_files – Number of file inodes.
    f_ffree – Number of available file inodes.
    f_favail – Number of available file inodes for administrator.
    f_flag – Mounting flags.
    f_namemax – The maximum length of the file. Unit: byte.
    """

def uname() -> tuple[str]:
    """Gets the information of the underlying system or its operating system.

    :return: The form of the return value of this interface differs from that of the official Micropython interface. This interface returns a tuple with the form of:
    sysname – String type. The name of the underlying system.
    nodename – String type. Network name (it can be the same as sysname).
    release – String type. The version of the underlying system.
    version – String type. MicroPython version and build date.
    machine – String type. Identifier of the underlying hardware (such as the main board and CPU).
    qpyver – String type. Short QuecPython version number.
    """

def uname2() -> tuple:
    """Gets the information of the underlying system or its operating system.

    :return: The form of the return value of this interface is the same as that of the official Micropython interface. Please note the difference from the return value of uos.uname(). The return value with the form of:
    (sysname, nodename, release, version, machine, qpyver)
    sysname – String type. The name of the underlying system.
    nodename – String type. Network name (it can be the same as sysname).
    release – String type. The version of the underlying system.
    version – String type. MicroPython version and build date.
    machine – String type. Identifier of the underlying hardware (such as the mainboard and CPU).
    qpyver – String type. QuecPython short version number.
    """

def urandom(n: int) -> bytes:
    """Returns a bytes object with n random bytes.

    If the module is equipped with a hardware random number generator, the object will be generated by the hardware random number generator.

    :param n: Integer type. Number of random bytes.
    :return: A bytes object with n random bytes.
    """

def VfsFat(spi_port: int, spimode: int, spiclk, spics):
    """Initializes the SD card through SPI prototype and SD card communication.

    :param spi_port: Integer type. Channel selection [0,1].
    :param spimode: Integer type. SPI work mode (mode 0 is the most commonly used):
    Parameter	Work Mode
    0	CPOL=0, CPHA=0
    1	CPOL=0, CPHA=1
    2	CPOL=1, CPHA=0
    3	CPOL=1, CPHA=1
    Clock polarity CPOL: The pin level of the clock signal SCLK when SPI is idle. (0: low level when idle; 1: high level when idle).
    :param spiclk: Integer type.
    Parameter	Clock Frequency
    0	812.5 KHz
    1	1.625 MHz
    2	3.25 MHz
    3	6.5 MHz
    4	13 MHz
    :param spics: Integer type. Assigns the CS pin as any GPIO. Hardware CS can connect this specified pin or the default SPI CS pin.
    1-n: Assigns Pin.GPIO1 - Pin.GPIOn as the CS pin.
    :return: If the execution is successful, VfsFat object will be returned. If the execution is failed, it will be stuck.
    """

def VfsSd(s: str = 'sf_fs'):
    """Initializes the SD card through SDIO prototype.

    :param s: String type. Inputs "sd_fs".
    :return: If the execution is successful, vfs object will be returned. If the execution is failed, the error will be reported.
    """

def set_det(GPIOn: int, mode: int) -> int:
    """Assigns the pin and mode for detecting the insertion and removal of the SD card.

    :param GPIOn: Integer type. GPIO pin number for detecting the insertion and removal of the SD card. Please refer to the definition of Pin module.
    :param mode: Integer type.
    0: After the SD card is inserted, the detection port is in low level. After the SD card is removed, the detection port is in high level.
    1: After the SD card is inserted, the detection port is in high level. After the SD card is removed, the detection port is in low level.
    :return: 0 - Successful execution; -1 - Failed execution.
    """

def set_callback(fun: Callable) -> int:
    """Sets the user callback function when the card is inserted or removed.

    :param fun: Function type. When the card is inserted or removed, fun(ind_type) will be called.
    ind_type - Event type. 0: Removing the card; 1: Inserting the card.
    :return: 0 - Successful execution; -1 - Failed execution.
    """

def VfsLfs1(readsize: int, progsize: int, lookahead: int, pname: str, spi_port: int, spi_clk: int):
    """Communicates with the external NOR FLASH through SPI. The storage device is mounted as the littleFS file system through SPI.

    :param readsize: Integer type. Reserved. It is not used yet.
    :param progsize: Integer type. Reserved. It is not used yet.
    :param lookahead: Integer type. Reserved. It is not used yet.
    :param pname: String type. The partition name is fixed to "ext_fs". It will be expanded later.
    :param spi_port: Integer type. See SPI chapter for supported ports.
    :param spi_clk: Integer type.
    Parameter	Clock Frequency
    0	6.25 MHz
    1	12.5 MHz
    2	25 MHz
    3	50 MHz
    4	3.125 MHz
    5	1.5625 MHz
    6	781.25 KHz
    :return: VfsLfs1 object - Successful execution; OSError 19 - Failed execution.
    """

def mount(vfs_obj, path: str):
    """Mounts the file system in substantial form (such as littleFS or FATFS) to the virtual file system(VFS).

    :param vfs_obj: vfs object. The object of the file system.
    :param path: String type. The root directory of the file system.
    """
