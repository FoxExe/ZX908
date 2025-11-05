import ujson
import uos


class Config:
	"""Configuration management class"""

	CONFIG_FILE = '/usr/tracker_config.json'

	DEFAULT_CONFIG = {
		'apn': {'name': 'internet', 'user': '', 'password': ''},
		'server': {'protocol': 'GT06', 'host': '', 'port': 0, 'path': '/api/location'},
		'allowed_numbers': [],  # Empty list = all numbers allowed
		'call_numbers': [],  # Empty list = no calls accepted
		'primary_number': '',  # First number that sent SMS
		'update_interval': 10,  # Seconds
		'sleep_timeout': 1800,  # 30 minutes in seconds
		'buffer_enabled': True
	}

	def __init__(self):
		self.config = self.load()

	def load(self):
		"""Load configuration from file"""
		try:
			with open(self.CONFIG_FILE, 'r') as f:
				config = ujson.load(f)
				# Fill missing keys with defaults
				for key, value in self.DEFAULT_CONFIG.items():
					if key not in config:
						config[key] = value
				return config
		except:
			return self.DEFAULT_CONFIG.copy()

	def save(self):
		"""Save configuration to file"""
		try:
			with open(self.CONFIG_FILE, 'w') as f:
				ujson.dump(self.config, f)
			return True
		except Exception as e:
			print('Config save error:', e)
			return False

	def get(self, key, default=None):
		"""Get parameter value"""
		return self.config.get(key, default)

	def set(self, key, value):
		"""Set parameter value"""
		self.config[key] = value
		return self.save()

	def update(self, **kwargs):
		"""Update multiple parameters"""
		self.config.update(kwargs)
		return self.save()
