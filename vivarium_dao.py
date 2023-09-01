import mariadb

from db_operations import DBOperations
from propertyreader import DBCONFIG

class VivariumDAO:
	"""Vivarium db related operations"""

	def putTempHumidData_db(currentDtTm, viva_t, viva_h):
		"""Insert current datetime, temperature and humidity data into db"""

		dbConnectObject = DBOperations.dbConnection(DBCONFIG.vdbname)

		try:
			insertCursor = dbConnectObject.cursor()
		except mariadb.Error as e:
			print(f"Error connecting to MariaDB platform: {e}")
		
		try:
			insertCursor.execute("INSERT INTO viva_climatedata (today_dttm, viva_temperature, viva_humidity) VALUES (?,?,?)", 
			(currentDtTm,
				float(viva_t),
				float(viva_h)))
			dbConnectObject.commit()
		except mariadb.Error as e:
			print(f"Error inserting into mariadb: {e}")
			dbConnectObject.rollback()

		insertCursor.close()
		dbConnectObject.close()

	def getTempHumidData_db():
		"""Fetch the last inserted Temperature and Humidity data from database"""
		
		dbConnectObject = DBOperations.dbConnection(DBCONFIG.vdbname)

		try:
			selectCursor = dbConnectObject.cursor()
		except mariadb.Error as e:
			print(f"Error connecting to MariaDB platform: {e}")

		try:
			selectCursor.execute("SELECT * FROM viva_climatedata order by today_dttm desc limit 1")
		except mariadb.Error as e:
			print(f"Error retrieving from MariaDB Platform: {e}")
		
		_vivaData = selectCursor.fetchall()

		selectCursor.close()
		dbConnectObject.close()

		if (_vivaData != []):
			return(_vivaData)
		else:
			return
	
	def putLuminosData_db(currentDtTm, viva_l):
		"""Insert current datetime, light data into db"""

		dbConnectObject = DBOperations.dbConnection(DBCONFIG.vdbname)

		try:
			insertCursor = dbConnectObject.cursor()
		except mariadb.Error as e:
			print(f"Error connecting to MariaDB platform: {e}")
		
		try:
			insertCursor.execute("INSERT INTO viva_luminosdata (today_dttm, viva_luminos) VALUES (?,?)", 
			(currentDtTm,
				viva_l))
			dbConnectObject.commit()
		except mariadb.Error as e:
			print(f"Error inserting into mariadb: {e}")
			dbConnectObject.rollback()

		insertCursor.close()
		dbConnectObject.close()

	def getLumosData_db():
		"""Fetch the last inserted Light data from db"""
		
		dbConnectObject = DBOperations.dbConnection(DBCONFIG.vdbname)

		try:
			selectCursor = dbConnectObject.cursor()
		except mariadb.Error as e:
			print(f"Error connecting to MariaDB platform: {e}")

		try:
			selectCursor.execute("SELECT * FROM viva_luminosdata order by today_dttm desc limit 1")
		except mariadb.Error as e:
			print(f"Error retrieving from MariaDB Platform: {e}")
		
		_vivaData = selectCursor.fetchall()

		selectCursor.close()
		dbConnectObject.close()
		
		return(_vivaData)

		# if (_vivaData != []):
		# 	return(_vivaData)
		# else:
		# 	return

# VivariumDAO.getLumosData_db()