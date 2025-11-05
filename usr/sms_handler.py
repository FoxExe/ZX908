import sim
import sms


class SMSHandler:
	"""Обработчик SMS команд"""

	def __init__(self, config, callback=None):
		self.config = config
		self.callback = callback
		self.init_sms()

	def init_sms(self):
		"""Инициализация SMS"""
		try:
			# Устанавливаем формат текстовых сообщений
			sms.setCallback(self._sms_callback)
			print('SMS handler initialized')
		except Exception as e:
			print('SMS init error:', e)

	def _sms_callback(self, args):
		"""Callback при получении SMS"""
		try:
			# Получаем индекс сообщения
			index = args[2]
			# Читаем сообщение
			msg = sms.getMessage(index)
			if msg:
				phone = msg[1]
				text = msg[4]
				print('SMS from:', phone, 'Text:', text)

				# Проверка разрешённых номеров
				if self._is_allowed_number(phone):
					self._process_command(phone, text)

				# Удаляем прочитанное сообщение
				sms.deleteMessage(index)
		except Exception as e:
			print('SMS callback error:', e)

	def _is_allowed_number(self, phone):
		"""Проверка, разрешён ли номер"""
		allowed = self.config.get('allowed_numbers', [])
		primary = self.config.get('primary_number', '')

		# Если список пуст, первый номер становится основным
		if not primary and not allowed:
			self.config.set('primary_number', phone)
			self.config.set('allowed_numbers', [phone])
			return True

		# Если список пуст, разрешены все
		if not allowed:
			return True

		# Проверяем наличие номера в списке
		return phone in allowed

	def _process_command(self, phone, text):
		"""Process SMS command"""
		text = text.strip().upper()

		try:
			# Parse command and parameters
			parts = [p.strip() for p in text.split(',')]
			command = parts[0]
			params = parts[1:] if len(parts) > 1 else []

			# Execute command
			if command == 'APN':
				self._cmd_apn(phone, params)
			elif command == 'SERVER':
				self._cmd_server(phone, params)
			elif command == 'WIFISERVER':  # New command for WiFi location server
				self._cmd_wifi_server(phone, params)
			elif command == 'ADDNUMBER':
				self._cmd_add_number(phone, params)
			elif command == 'DELNUMBER':
				self._cmd_del_number(phone, params)
			elif command == 'ADDCALL':
				self._cmd_add_call(phone, params)
			elif command == 'DELCALL':
				self._cmd_del_call(phone, params)
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

	def _cmd_wifi_server(self, phone, params):
		"""Set WiFi location server - WIFISERVER,host[:port][,path]"""
		if len(params) >= 1:
			host_port = params[0]
			path = params[1] if len(params) > 1 else '/api/locate'

			# Parse host and port
			if ':' in host_port:
				host, port = host_port.split(':', 1)
				port = int(port)
			else:
				host = host_port
				port = 80

			self.config.update(wifi_server={
				'host': host,
				'port': port,
				'path': path
			})

			if self.callback:
				self.callback('wifi_server_changed')

			self._send_sms(phone, 'WiFi server set: {}:{}'.format(host, port))
			print('WiFi location server updated:', host, port)
		else:
			self._send_sms(phone, 'Usage: WIFISERVER,host:port[,path]')

	def _cmd_apn(self, text):
		"""Установка APN настроек"""
		parts = text.split(',')
		if len(parts) >= 2:
			apn_name = parts[1] if len(parts) > 1 else ''
			apn_user = parts[2] if len(parts) > 2 else ''
			apn_pass = parts[3] if len(parts) > 3 else ''

			self.config.update(apn={
				'name': apn_name,
				'user': apn_user,
				'password': apn_pass
			})

			if self.callback:
				self.callback('apn_changed')
			print('APN updated:', apn_name)

	def _cmd_server(self, text):
		"""Установка сервера"""
		parts = text.split(',')
		if len(parts) >= 4:
			protocol = parts[1]  # GT06 или HTTP
			host = parts[2]
			port = int(parts[3])

			self.config.update(server={
				'protocol': protocol,
				'host': host,
				'port': port
			})

			if self.callback:
				self.callback('server_changed')
			print('Server updated:', host, port)

	def _cmd_add_number(self, text):
		"""Добавление разрешённого номера"""
		parts = text.split(',')
		if len(parts) >= 2:
			phone = parts[1]
			allowed = self.config.get('allowed_numbers', [])
			if phone not in allowed:
				allowed.append(phone)
				self.config.set('allowed_numbers', allowed)
			print('Number added:', phone)

	def _cmd_del_number(self, text):
		"""Удаление разрешённого номера"""
		parts = text.split(',')
		if len(parts) >= 2:
			phone = parts[1]
			allowed = self.config.get('allowed_numbers', [])
			if phone in allowed:
				allowed.remove(phone)
				self.config.set('allowed_numbers', allowed)
			print('Number removed:', phone)

	def _cmd_add_call(self, text):
		"""Добавление номера для приёма звонков"""
		parts = text.split(',')
		if len(parts) >= 2:
			phone = parts[1]
			call_numbers = self.config.get('call_numbers', [])
			if phone not in call_numbers:
				call_numbers.append(phone)
				self.config.set('call_numbers', call_numbers)
			print('Call number added:', phone)

	def _cmd_del_call(self, text):
		"""Удаление номера для приёма звонков"""
		parts = text.split(',')
		if len(parts) >= 2:
			phone = parts[1]
			call_numbers = self.config.get('call_numbers', [])
			if phone in call_numbers:
				call_numbers.remove(phone)
				self.config.set('call_numbers', call_numbers)
			print('Call number removed:', phone)

	def _cmd_interval(self, text):
		"""Установка интервала передачи"""
		parts = text.split(',')
		if len(parts) >= 2:
			interval = int(parts[1])
			if 1 <= interval <= 600:
				self.config.set('update_interval', interval)
				if self.callback:
					self.callback('interval_changed')
				print('Interval updated:', interval)

	def _cmd_sleep(self, text):
		"""Установка времени до сна"""
		parts = text.split(',')
		if len(parts) >= 2:
			minutes = int(parts[1])
			self.config.set('sleep_timeout', minutes * 60)
			print('Sleep timeout updated:', minutes, 'min')

	def _cmd_status(self, phone):
		"""Отправка статуса устройства"""
		if self.callback:
			status = self.callback('get_status')
			if status:
				self._send_sms(phone, status)

	def _send_sms(self, phone, text):
		"""Отправка SMS"""
		try:
			sms.sendTextMsg(phone, text, 'GSM')
			print('SMS sent to:', phone)
		except Exception as e:
			print('SMS send error:', e)
