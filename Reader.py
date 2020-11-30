import RPi.GPIO as GPIO
import string
import csv
import os.path
import sys
from mfrc522 import SimpleMFRC522

class Reader:
	reader = None

	def __init__(self):
		self.reader = SimpleMFRC522()

	def readCard(self):
		try:
			print("Trying to read card...")
			id = self.reader.read_id()
			print("ID: %s" % (id))
			return "%s" % id
		finally:
			GPIO.cleanup()

