"""
# Regular Expression

https://python.quectel.com/doc/API_reference/en/stdlib/ure.html

### Supported Operators
* `.` – Character type. Match any character.
* `[]` – Character type. Match set of characters. Individual characters and ranges are supported, including negated sets.
* `^` – Character type. Match the start of the string.
* `$` – Character type. Match the end of the string.
* `?` – Character type. Match zero or one of the previous sub-pattern.
* `*` – Character type. Match zero or more of the previous sub-pattern.
* `+` – Character type. Match one or more of the previous sub-pattern.
* `??` – Character type. Non-greedy version of ? , match zero or one.
* `*?` – Character type. Non-greedy version of * , match zero or more.
* `+?` – Character type. Non-greedy version of + , match one or more.
* `\\|` – Character type. Match either the left-hand side or the right-hand side sub-patterns of this operator.
* `\\d` – Character type. Match digit.
* `\\D` – Character type. Match non-digit.
* `\\s` – Character type. Match whitespace.
* `\\S` – Character type. Match non-whitespace.
* `\\w` – Character type. Match "word characters" (ASCII only).
* `\\W` – Character type. Match "word characters" (ASCII only).

###  Not Supported Operators

* `{m,n}` – Counted repetitions.
* `(?P<name>...)` – Named groups.
* `(?:...)` – Non-capturing groups.
* `\\b` – More advanced assertions.
* `\\B` – More advanced assertions.
* `\\r` – Special character escapes – use Python`s own escaping instead.
* `\\n` – Special character escapes – use Python`s own escaping instead.

"""


def compile(regex_str: str, flags: int = ..., /) -> "ure":
	"""Compiles a regular expression and generates a regular-expression object, used by ure.match() and ure.search()"""


def match(regex_str: str, string: str, /) -> "Match[str]":
	"""Matches the compiled regular expression against string . Match always happens from the start position in a string"""


def search(regex_str: str, string: str, /) -> "Match[str]":
	"""Searches for the compiled regular expression in string and returns the first successful match"""


class Match:
	"""A matched object, returned by `ure.match()` and `ure.search()`"""

	def group(self, index: int) -> str:
		"""Return matched group at index :index:"""


class ure:
	"""Compiled regular expression. Instances of this class are created using `ure.compile()`."""

	def match(self, string: str, /) -> Match | None:
		"""Execute compiled regexp to a given string"""

	def search(self, string: str, /) -> Match | None:
		"""Execute compiled regexp to a given string"""

	def split(self, string: str, max_split: int = -1, /) -> list[str] | None:
		"""Execute compiled regexp to a given string"""
