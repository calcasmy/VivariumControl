import Adafruit_DHT
import time
import board
import adafruit_bh1750

from dt_operations import DTOperations
from vivarium_dao import VivariumDAO

class VivariumData:
	def getVivariumData():
		while True:
			viva_t, viva_h = VivariumData.getTempHumidData()
			print("light: %.2f Lux"%VivariumData.getluminosdata())
			print("Humidity: {}, Temperature: {}".format(viva_h, viva_t))
			time.sleep(15)

	def getTempHumidData():
		"""Get Temperature and Humidity data from Vivarium sensor"""

		# Current date with timestamp to save to database.
		currentDtTm = DTOperations.todayDtTm() 

		# Humidity and Temperature data from the Vivarium Sensors
		viva_h, viva_t = Adafruit_DHT.read_retry(11, 4)
		viva_t = round((viva_t * 1.8) + 32, 2)

		lastVivariumData = VivariumDAO.getTempHumidData_db()

		# if(viva_t != lastVivariumData[0][1] or viva_h != lastVivariumData[0][2]):
		# 	VivariumDAO.putTempHumidData_db(currentDtTm, viva_t, viva_h)
		VivariumDAO.putTempHumidData_db(currentDtTm, viva_t, viva_h)
		print("Humidity: {}, Temperature: {}".format(viva_h, viva_t))
		return viva_t, viva_h

	def getluminosdata():
		"""Get Light data from Vivarium sensor"""

		i2c = board.I2C()
		sensor = adafruit_bh1750.BH1750(i2c)
		currentDtTm = DTOperations.todayDtTm()
		viva_l = round(sensor.lux, 2)
		VivariumDAO.putLuminosData_db(currentDtTm, viva_l)
		print("light: %.2f Lux"%viva_l)
		return viva_l

# VivariumData.getVivariumData()