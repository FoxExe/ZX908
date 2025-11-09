import sms
import utime
import modem
from usr.config import Config


class SMSHandler:
	"""SMS command handler"""

	def __init__(self, config, callback=None):
		self.config = config
		self.callback = callback
		self.imei = modem.getDevImei()
		self.init_sms()

	def init_sms(self):
		"""Initialize SMS handler"""
		try:
			sms.setCallback(self._sms_callback)
			print('SMS handler initialized, IMEI:', self.imei)
		except Exception as e:
			print('SMS init error:', e)

	def _sms_callback(self, args):
		"""Callback on SMS received"""
		try:
			if args[0] == 1:
				print('SMS received, index:', args[2])
				msg = sms.searchTextMsg(args[2])
				if msg != -1:
					phone, text, timestamp = msg
					print('From:', phone, 'Text:', text)
					sms.deleteMsg(args[2])
					self._process_command(phone, text)
		except Exception as e:
			print('SMS callback error:', e)

	def _process_command(self, phone, text):
		"""Process SMS command"""
		text = text.strip().upper()
		try:
			parts = [p.strip() for p in text.split(',')]
			command = parts[0]
			params = parts[1:] if len(parts) > 1 else []
			if command == 'RESET' and len(params) >= 1:
				self._cmd_reset(phone, params)
			elif not self._is_authorized(phone):
				print('Unauthorized command from:', phone)
				return
			if command == 'APN':
				self._cmd_apn(phone, params)
			elif command == 'SERVER':
				self._cmd_server(phone, params)
			elif command == 'WIFISERVER':
				self._cmd_wifi_server(phone, params)
			elif command == 'WIFIENABLE':
				self._cmd_wifi_enable(phone, params)
			elif command == 'ADDNUMBER':
				self._cmd_add_number(phone, params)
			elif command == 'DELNUMBER':
				self._cmd_del_number(phone, params)
			elif command == 'INTERVAL':
				self._cmd_interval(phone, params)
			elif command == 'SLEEP':
				self._cmd_sleep(phone, params)
			elif command == 'STATUS':
				self._cmd_status(phone, params)
			elif command == 'POWEROFF':
				self._cmd_poweroff(phone, params)
			else:
				self._send_sms(phone, 'Unknown command: ' + command)
		except Exception as e:
			print('Command processing error:', e)
			self._send_sms(phone, 'Error: ' + str(e))

	def _is_authorized(self, phone):
		"""Check if phone number is authorized"""
		sms_numbers = self.config.get('sms_numbers', [])
		if not sms_numbers:
			sms_numbers.append(phone)
			self.config.update(sms_numbers=sms_numbers)
			print('First number added:', phone)
			return True
		for allowed_number in sms_numbers:
			if phone in allowed_number or allowed_number in phone:
				return True
		return False

	def _send_sms(self, phone, text):
		"""Send SMS response"""
		try:
			ret = sms.sendTextMsg(phone, text, 'GSM')
			if ret >= 0:
				print('SMS sent to', phone)
			else:
				print('SMS send failed')
		except Exception as e:
			print('SMS send error:', e)

	def _cmd_reset(self, phone, params):
		"""Reset device - RESET,IMEI"""
		if len(params) >= 1:
			provided_imei = params[0].strip()
			if provided_imei == self.imei:
				self._send_sms(phone, 'Device reset OK')
				utime.sleep(2)
				if self.callback:
					self.callback('reset')
			else:
				print('Invalid IMEI for reset from:', phone)
		else:
			self._send_sms(phone, 'Usage: RESET,IMEI')

	def _cmd_apn(self, phone, params):
		"""Configure APN - APN,name[,user,password]"""
		if len(params) >= 1:
			apn_name = params[0]
			apn_user = params[1] if len(params) > 1 else ''
			apn_password = params[2] if len(params) > 2 else ''
			self.config.update(apn={'name': apn_name, 'user': apn_user, 'password': apn_password})
			if self.callback:
				self.callback('apn_changed')
			self._send_sms(phone, 'APN set: ' + apn_name)
			print('APN updated:', apn_name)
		else:
			self._send_sms(phone, 'Usage: APN,name[,user,password]')

	def _cmd_server(self, phone, params):
		"""Configure server - SERVER,protocol,host:port[,path]"""
		if len(params) >= 2:
			protocol = params[0].upper()
			host_port = params[1]
			if '://' in host_port:
				parts = host_port.split('://', 1)
				protocol = parts[0].upper()
				host_port = parts[1]
				if '/' in host_port:
					host_port, path = host_port.split('/', 1)
					path = '/' + path
				else:
					path = '/api/location'
			else:
				path = params[2] if len(params) > 2 else '/api/location'
			if ':' in host_port:
				host, port = host_port.split(':', 1)
				port = int(port)
			else:
				host = host_port
				port = 5023 if protocol == 'GT06' else 80
			self.config.update(server={'protocol': protocol, 'host': host, 'port': port, 'path': path})
			if self.callback:
				self.callback('server_changed')
			self._send_sms(phone, 'Server: {}://{}:{}'.format(protocol, host, port))
			print('Server updated:', protocol, host, port)
		else:
			self._send_sms(phone, 'Usage: SERVER,protocol,host:port[,path]')

	def _cmd_wifi_server(self, phone, params):
		"""Set WiFi location server - WIFISERVER,host:port[,path]"""
		if len(params) >= 1:
			host_port = params[0]
			path = params[1] if len(params) > 1 else '/api/locate'
			if ':' in host_port:
				host, port = host_port.split(':', 1)
				port = int(port)
			else:
				host = host_port
				port = 80
			self.config.update(wifi_server={'host': host, 'port': port, 'path': path})
			if self.callback:
				self.callback('wifi_server_changed')
			self._send_sms(phone, 'WiFi server: {}:{}'.format(host, port))
			print('WiFi location server updated:', host, port)
		else:
			self._send_sms(phone, 'Usage: WIFISERVER,host:port[,path]')

	def _cmd_wifi_enable(self, phone, params):
		"""Enable/disable WiFi location - WIFIENABLE,1/0"""
		if len(params) >= 1:
			try:
				enable = int(params[0])
				self.config.update(wifi_location_enabled=(enable == 1))
				status = 'enabled' if enable == 1 else 'disabled'
				self._send_sms(phone, 'WiFi location ' + status)
				print('WiFi location:', status)
			except ValueError:
				self._send_sms(phone, 'Invalid value (0 or 1)')
		else:
			enabled = self.config.get('wifi_location_enabled', False)
			status = 'enabled' if enabled else 'disabled'
			self._send_sms(phone, 'WiFi location: ' + status)

	def _cmd_add_number(self, phone, params):
		"""Add allowed number - ADDNUMBER,phone"""
		if len(params) >= 1:
			new_number = params[0]
			sms_numbers = self.config.get('sms_numbers', [])
			if new_number not in sms_numbers:
				sms_numbers.append(new_number)
				self.config.update(sms_numbers=sms_numbers)
				self._send_sms(phone, 'Number added: ' + new_number)
				print('SMS number added:', new_number)
			else:
				self._send_sms(phone, 'Number already exists')
		else:
			self._send_sms(phone, 'Usage: ADDNUMBER,phone')

	def _cmd_del_number(self, phone, params):
		"""Remove allowed number - DELNUMBER,phone"""
		if len(params) >= 1:
			del_number = params[0]
			sms_numbers = self.config.get('sms_numbers', [])
			if del_number in sms_numbers:
				sms_numbers.remove(del_number)
				self.config.update(sms_numbers=sms_numbers)
				self._send_sms(phone, 'Number removed: ' + del_number)
				print('SMS number removed:', del_number)
			else:
				self._send_sms(phone, 'Number not found')
		else:
			self._send_sms(phone, 'Usage: DELNUMBER,phone')

	def _cmd_interval(self, phone, params):
		"""Set update interval - INTERVAL,seconds"""
		if len(params) >= 1:
			try:
				interval = int(params[0])
				if 1 <= interval <= 600:
					self.config.update(update_interval=interval)
					if self.callback:
						self.callback('interval_changed')
					self._send_sms(phone, 'Interval: {}s'.format(interval))
					print('Update interval changed:', interval)
				else:
					self._send_sms(phone, 'Invalid interval (1-600)')
			except ValueError:
				self._send_sms(phone, 'Invalid interval value')
		else:
			interval = self.config.get('update_interval', 10)
			self._send_sms(phone, 'Current interval: {}s'.format(interval))

	def _cmd_sleep(self, phone, params):
		"""Set sleep timeout - SLEEP,minutes"""
		if len(params) >= 1:
			try:
				minutes = int(params[0])
				timeout = minutes * 60
				self.config.update(sleep_timeout=timeout)
				self._send_sms(phone, 'Sleep timeout: {}min'.format(minutes))
				print('Sleep timeout changed:', minutes, 'minutes')
			except ValueError:
				self._send_sms(phone, 'Invalid timeout value')
		else:
			timeout = self.config.get('sleep_timeout', 1800)
			minutes = timeout // 60
			self._send_sms(phone, 'Sleep timeout: {}min'.format(minutes))

	def _cmd_status(self, phone, params):
		"""Get device status - STATUS"""
		if self.callback:
			status = self.callback('get_status')
			if status:
				self._send_sms(phone, status)

	def _cmd_poweroff(self, phone, params):
		"""Power off device - POWEROFF"""
		self._send_sms(phone, 'Powering off...')
		utime.sleep(2)
		if self.callback:
			self.callback('poweroff')
