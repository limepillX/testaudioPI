import time

import RPi.GPIO as GPIO
import os

path_to_file = os.path.abspath('sound.m4a')

# Установка номера GPIO-пина для управления реле
relay_pin = 23

# Инициализация библиотеки RPi.GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(relay_pin, GPIO.OUT)

# Включение реле
GPIO.output(relay_pin, GPIO.HIGH)

# Воспроизведение аудиофайла с помощью mpg321
os.system(f'mpg321 {path_to_file}')

time.sleep(3)

# Отключение реле
GPIO.output(relay_pin, GPIO.LOW)

# Выключение библиотеки RPi.GPIO
GPIO.cleanup()
