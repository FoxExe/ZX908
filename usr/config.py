import ujson
import uos
from misc import Power
import modem


CONFIG_FILE = '/usr/tracker_config.json'
DEFAULT_CONFIG = {
	'apn': {'name': 'internet', 'user': '', 'password': ''},
	'server': {'protocol': 'GT06', 'host': '', 'port': 0, 'path': '/api/location'},
	'wifi_server': None,
	'wifi_location_enabled': False,
	'update_interval': 10,
	'sleep_timeout': 1800,
	'buffer_enabled': True,
	'sms_numbers': [],
	'imei': ''
}


class Config:
	"""Configuration manager for GPS Tracker"""


	def __init__(self):
		self.config = self._load()
		if not self.config.get('imei'):
			self.config['imei'] = modem.getDevImei()
			self.save()
		print('Configuration loaded')

	def _load(self):
		"""Load configuration from file"""
		try:
			if CONFIG_FILE in uos.listdir('/usr'):
				with open(CONFIG_FILE, 'r') as f:
					config = ujson.load(f)
					for key, value in DEFAULT_CONFIG.items():
						if key not in config:
							config[key] = value
					return config
		except Exception as e:
			print('Config load error:', e)
		return DEFAULT_CONFIG.copy()

	def save(self):
		"""Save configuration to file"""
		try:
			with open(CONFIG_FILE, 'w') as f:
				ujson.dump(self.config, f)
			print('Configuration saved')
			return True
		except Exception as e:
			print('Config save error:', e)
			return False

	def get(self, key, default=None):
		"""Get configuration value"""
		return self.config.get(key, default)

	def update(self, **kwargs):
		"""Update configuration"""
		for key, value in kwargs.items():
			self.config[key] = value
		return self.save()

	def reset(self):
		"""Reset to default configuration"""
		self.config = DEFAULT_CONFIG.copy()
		self.config['imei'] = modem.getDevImei()
		return self.save()
