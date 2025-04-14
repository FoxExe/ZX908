"""
Function:
uio contains additional types of stream (file-like) objects and helper functions. This feature implements a subset of the corresponding CPython feature, as described below.
For more information, refer to the original CPython documentation: https://docs.python.org/3.5/library/io.html#module-io.

Descriptions taken from:
https://python.quectel.com/doc/API_reference/zh/stdlib/uio.html


Additional structures, based on QuecPython firmware for EC800NCN_LA:

>>> dir(uio)
['__class__', '__name__', 'open', 'BytesIO', 'FileIO', 'IOBase', 'StringIO', 'TextIOWrapper']
>>> dir(uio.IOBase)
['__class__', '__name__', '__bases__', '__dict__']
>>> dir(uio.BytesIO)
['__class__', '__enter__', '__exit__', '__name__', 'close', 'read', 'readinto', 'readline', 'write', '__bases__', '__dict__', 'flush', 'getvalue', 'seek', 'tell']
>>> dir(uio.StringIO)
['__class__', '__enter__', '__exit__', '__name__', 'close', 'read', 'readinto', 'readline', 'write', '__bases__', '__dict__', 'flush', 'getvalue', 'seek', 'tell']
>>> dir(uio.FileIO)
['__class__', '__enter__', '__exit__', '__name__', 'close', 'read', 'readinto', 'readline', 'write', '__bases__', '__del__', '__dict__', 'flush', 'readlines', 'seek', 'tell']
>>> dir(uio.TextIOWrapper)
['__class__', '__enter__', '__exit__', '__name__', 'close', 'read', 'readinto', 'readline', 'write', '__bases__', '__del__', '__dict__', 'flush', 'readlines', 'seek', 'tell']
"""


def open(name, mode='r', buffering=-1, encoding=None):
	"""Opens a file. This is an alias for the built-in open() function.

	:param name: String type. File name.
	:param mode: String type. Open mode.
	Open Mode	Description
	'r'	Open a file for reading.
	'w'	Open a file for writing only. Overwrites the file if the file exists.
	'a'	Opens a file for appending. The file pointer is at the end of the file, so the content is added to the end.
	:param kwargs: Variable-length parameter list.
	:return:uio object – Successful execution
	:raise: OSError - Failed execution
	"""


class IOBase:
	def __enter__(self):
		"""Called on entry to a `with` block."""

	def __exit__(self, exc_type, exc_value: BaseException | None, traceback) -> bool | None:
		"""Called on exit of a `with` block."""

	def close(self) -> None:
		"""Flushes the write buffers and closes the IO stream"""

	def flush(self) -> None:
		"""Flushes the write buffers of the IO stream."""

	def read(self, size: int | None = -1) -> str | bytes | None:
		"""Read up to `size` bytes from the object and return them as a `str` (text file) or `bytes` (binary file)"""

	def readinto(self, b: bytes | bytearray | memoryview) -> int | None:
		"""Read bytes into a pre-allocated, writable bytes-like object b, and return the number of bytes read. """

	def readline(self, size: int = -1) -> str | bytes:
		"""Read and return, as a `str` (text file) or `bytes` (binary file), one line from the stream. """

	def write(self, b: bytes | bytearray | memoryview) -> int | None:
		"""Write the given bytes-like object, `b`, to the underlying raw stream, and return the number of bytes written. """

	def seek(self, offset: int, whence: int = 0) -> int:
		"""Change the stream position to the given byte `offset`"""

	def tell(self) -> int:
		"""Return the current stream position"""


class BytesIO(IOBase):
	def getvalue(self) -> str:
		"""Get the current contents of the underlying buffer which holds data"""


class StringIO(BytesIO):
	pass


class FileIO(IOBase):
	def readlines(self, hint: int | None = -1) -> list[str]:
		"""Read and return a list of lines, as a `list[str]` (text file) or `list[bytes]` (binary file), from the stream"""


class TextIOWrapper(FileIO):
	pass
