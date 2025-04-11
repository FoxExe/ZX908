"""
Function:
ujson module realizes the convertion between the Python data object and the JSON data format, and subsets of the corresponding CPython module.
See CPython file json for more detailed information: https://docs.python.org/3.5/library/json.html#module-json.

Descriptions taken from:
https://python.quectel.com/doc/API_reference/zh/stdlib/ujson.html
"""


def dump(obj, stream):
    """Serializes obj data object, converts it to JSON character string, and writes it to the specified stream."""

def dumps(obj):
    """Converts the data in dictionary type of obj to JSON character string."""

def load(stream):
    """Parses the specified stream into JSON character string and deserializes it into Python object, finally returns the object."""

def loads(string):
    """Parses JSON character string str and returns a Python object."""
