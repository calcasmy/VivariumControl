import Adafruit_DHT
import time
import board
import adafruit_blinka
from adafruit_htu21d import HTU21D
import busio


from propertyreader import APPCONFIG
from dt_operations import DTOperations
from vivarium_dao import VivariumDAO

class VivariumData:
	def getVivariumData(dhtSensor: str):
		while True:
			if(dhtSensor == APPCONFIG.DHTS11):
				viva_t, viva_h = VivariumData.getTempHumidDataDHTS11()
			elif(dhtSensor == APPCONFIG.DHTSI2C):
				viva_t, viva_h = VivariumData.getTempHumidDataDHTSI2C()

			# print("light: %.2f Lux"%VivariumData.getluminosdata())
			print("Humidity: {}, Temperature: {}".format(viva_h, viva_t))
			time.sleep(15)

	def getTempHumidDataDHTS11():
		"""Get Temperature and Humidity data from Vivarium sensor"""

		currentDtTm = DTOperations.todayDtTm() 

		viva_h, viva_t = Adafruit_DHT.read_retry(11, 4)
		viva_t = round((viva_t * 1.8) + 32, 2)

		# lastVivariumData = VivariumDAO.getTempHumidData_db()

		# if(viva_t != lastVivariumData[0][1] or viva_h != lastVivariumData[0][2]):
		# 	VivariumDAO.putTempHumidData_db(currentDtTm, viva_t, viva_h)

		VivariumDAO.putTempHumidData_db(currentDtTm, viva_t, viva_h)
		print("Humidity: {}, Temperature: {}".format(viva_h, viva_t))
		return viva_t, viva_h

	def getTempHumidDataDHTSI2C():
		i2c = busio.I2C(board.SCL, board.SDA)
		sensor = HTU21D(i2c)
		return sensor.temperature, sensor.relative_humidity

	# def getluminosdata():
	# 	"""Get Light data from Vivarium sensor"""

	# 	i2c = board.I2C()
	# 	sensor = adafruit_bh1750.BH1750(i2c)
	# 	currentDtTm = DTOperations.todayDtTm()
	# 	viva_l = round(sensor.lux, 2)
	# 	VivariumDAO.putLuminosData_db(currentDtTm, viva_l)
	# 	print("light: %.2f Lux"%viva_l)
	# 	return viva_l

VivariumData.getTempHumidDataDHTSI2C()