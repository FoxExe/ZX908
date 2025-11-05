import call
import audio


class CallHandler:
	"""Обработчик входящих звонков"""

	def __init__(self, config):
		self.config = config
		self.init_call()

	def init_call(self):
		"""Инициализация обработчика звонков"""
		try:
			call.setAutoAnswer(0)  # Отключаем автоответ
			call.setCallback(self._call_callback)
			print('Call handler initialized')
		except Exception as e:
			print('Call init error:', e)

	def _call_callback(self, args):
		"""Callback при входящем звонке"""
		try:
			event = args[0]

			if event == 1:  # Incoming call
				phone = args[1]
				print('Incoming call from:', phone)

				# Проверка разрешённых номеров
				if self._is_allowed_call(phone):
					print('Answering call from:', phone)
					call.answer()
					# Включаем микрофон
					audio.setChannel(1)  # Наушники
					audio.play(1, 0, '')  # Включаем аудио канал
				else:
					print('Call rejected from:', phone)
					call.callEnd()

			elif event == 6:  # Call ended
				print('Call ended')
				audio.stop()

		except Exception as e:
			print('Call callback error:', e)

	def _is_allowed_call(self, phone):
		"""Проверка, разрешён ли номер для звонков"""
		call_numbers = self.config.get('call_numbers', [])

		# Если список пуст, звонки не принимаются
		if not call_numbers:
			return False

		# Проверяем наличие номера в списке
		return phone in call_numbers
