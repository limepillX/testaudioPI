import time
from loguru import logger

import RPi.GPIO as GPIO
import os

path_to_file = os.path.abspath('sound.mp3')
logger.debug(path_to_file)
# Установка номера GPIO-пина для управления реле
relay_pin = 23
logger.info(f'Используем пин под номером {relay_pin}')
# Инициализация библиотеки RPi.GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(relay_pin, GPIO.OUT)
logger.info('GPIO initialized')

# Включение реле
GPIO.output(relay_pin, GPIO.HIGH)
logger.info('rele turned ON')

# Воспроизведение аудиофайла с помощью mpg321
os.system(f'mpg321 {path_to_file}')
logger.info('audio file started')

time.sleep(3)
logger.info('file finished')

# Отключение реле
GPIO.output(relay_pin, GPIO.LOW)
logger.info('rele turned OFF')

# Выключение библиотеки RPi.GPIO
GPIO.cleanup()
logger.info('cleaning up')
