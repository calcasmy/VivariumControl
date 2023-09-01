#!/usr/bin/python3
import mariadb
import json

from dt_operations import DTOperations
from db_operations import DBOperations
from propertyreader import DBCONFIG


class AtmosphereDAO:

	def putRawData_db(rawRequestData):
		"""Insert todays raw climate data into Database"""
		
		#Today's Date formatted to be inserted into DB
		today = DTOperations.todayDate()

		dbConnectObject = DBOperations.dbConnection(DBCONFIG.adbname)

		try:
			selectCursor = dbConnectObject.cursor()
			insertCursor = dbConnectObject.cursor()
		except mariadb.Error as e:
			print(f"Error connecting to MariaDB Platform: {e}")

		try:
			selectCursor.execute("SELECT today_date FROM atmos_rawdata WHERE today_date=?", (today,))
		except mariadb.Error as e:
			print(f"Error connecting to MariaDB Platform: {e}")
		
		if(selectCursor.fetchall() == []):

			# JSON data from AtmosphereData.getRawData_api
			atmosphereData = json.dumps(rawRequestData)

			try:
				insertCursor.execute("INSERT INTO atmos_rawdata (today_date, rawdata) VALUES (?,?)", (today, atmosphereData,))
				dbConnectObject.commit()
			except mariadb.Error as e:
				print(f"Error inserting into mariadb: {e}")
				dbConnectObject.rollback

			selectCursor.close()
			insertCursor.close()
			dbConnectObject.close()

			AtmosphereDAO.formatAtmosphereData()
		else:
			print("Today rawdata is already in database")

	def getRawData_db(_date: str):
		"""Fetches raw climate data from database for a specified date"""

		#Today's Date formatted to be inserted into DB
		today = DTOperations.todayDate()

		if(_date <= today):
			dbConnectObject = DBOperations.dbConnection(DBCONFIG.adbname)

			try:
				selectCursor = dbConnectObject.cursor()
			except mariadb.Error as e:
				print(f"Error connecting to MariaDB Platform: {e}")

			try:
				selectCursor.execute("SELECT JSON_QUERY(rawdata, '$.forecast.forecastday') FROM atmos_rawdata WHERE today_date=?", (_date,))
			except mariadb.Error as e:
				print(f"Error retrieving from MariaDB Platform: {e}")

			_rawdata = selectCursor.fetchall()

			dbConnectObject.close()
			selectCursor.close()
			
			if(_rawdata == []):
				# JSON data from AtmosphereData.getRawData_api
				print('Raw data unavailable')
			else:
					return _rawdata
		else:
			print("Invalid date provided, date must be less than or equeal to today date")

	def formatAtmosphereData():
		"""Prepare the raw climate data to only include Astro and Day forecast data"""
	
		#Today's Date formatted to be inserted into DB
		today = DTOperations.todayDate()
		
		rawAtmosphereData = AtmosphereDAO.getRawData_db(today)[0]
		rawAtmosphereData = rawAtmosphereData[0]
		rawAtmosphereData = rawAtmosphereData[1:]
		rawAtmosphereData = rawAtmosphereData[:-1]
		rawAtmosphereData = json.loads(rawAtmosphereData)

		AtmosphereDAO.putAstroData_db(today, rawAtmosphereData['astro'])
		AtmosphereDAO.putClimateData_db(today, rawAtmosphereData['day'])

	def putAstroData_db(today, astroData):
		"""Insert today's astro data along with today's date into db"""
		
        #Loading astro data into DB from Rawdata
		if(astroData != None):
			dbConnectObject = DBOperations.dbConnection(DBCONFIG.adbname)
			try:
				insertCursor = dbConnectObject.cursor()
			except mariadb.Error as e:
				print(f"Error connecting to MariaDB Platform: {e}")

			try:
				insertCursor.execute("INSERT INTO atmos_astrodata (today_date, sunrise, sunset, moonrise, moonset, moonphase) VALUES (?,?,?,?,?,?)", 
					(today, 
						astroData['sunrise'], 
						astroData['sunset'], 
						astroData['moonrise'], 
						astroData['moonset'], 
						astroData['moon_phase'],))
				dbConnectObject.commit()
			except mariadb.Error as e:
				print(f"Error inserting into mariadb: {e}")
				dbConnectObject.rollback

			insertCursor.close()
			dbConnectObject.close()

	def putClimateData_db(today, climateData):
		"""Insert today's climate data along with today's date into DB"""

		#Loading astro data into DB from Rawdata
		if(climateData != None):
			dbConnectObject = DBOperations.dbConnection(DBCONFIG.adbname)
			try:
				insertCursor = dbConnectObject.cursor()
			except mariadb.Error as e:
				print(f"Error connecting to MariaDB Platform: {e}")

			try:
				insertCursor.execute("INSERT INTO atmos_climatedata (today_date, maxtemp_c, maxtemp_f, mintemp_c, mintemp_f, avgtemp_c, avgtemp_f) VALUES (?,?,?,?,?,?,?)", 
					(today, 
						climateData['maxtemp_c'], 
						climateData['maxtemp_f'], 
						climateData['mintemp_c'], 
						climateData['mintemp_f'], 
						climateData['avgtemp_c'], 
						climateData['avgtemp_f'],))
				dbConnectObject.commit()
			except mariadb.Error as e:
				print(f"Error inserting into mariadb: {e}")
				dbConnectObject.rollback

			insertCursor.close()
			dbConnectObject.close()

	def getAstroData_db(fetchDate: str) -> list:
		"""Fetches astro data from db  for the specified date
	    Return list contains the following values
	    today_date, sunrise, sunset, moonrise, moonset, moonphase"""
		
		if fetchDate:
			dbConnectObject = DBOperations.dbConnection(DBCONFIG.adbname)
			selectCursor = dbConnectObject.cursor()
		else:
			print('Provide date to fetch the correct information')

		try:
			selectCursor.execute("SELECT * FROM atmos_astrodata WHERE today_date=?", (DTOperations.convertStrToDt(fetchDate),))
		except mariadb.Error as e:
			print(f"Unable to fetch data from DB: {e}")

		_astroData = selectCursor.fetchall()

		selectCursor.close()
		dbConnectObject.close()

		return _astroData

	def getClimateData_db(fetchDate) -> list:
		"""Fetch climate data from db for the specified date
	    Return list contains the following values
	    today_date, maxtemp_c, maxtemp_f, mintemp_c, mintemp_f, avgtemp_c, avgtemp_f"""
		if fetchDate:
			dbConnectObject	= DBOperations.dbConnection(DBCONFIG.adbname)
			selectCursor = dbConnectObject.cursor()
		else:
			print('Provide date to fetch the correct information')

		try:
			selectCursor.execute("SELECT * FROM atmos_climatedata WHERE today_date=?", (DTOperations.convertStrToDt(fetchDate),))
		except mariadb.Error as e:
			print(f"Unable to fetch data from DB: {e}")
		
		_climateData = selectCursor.fetchall()
		
		selectCursor.close()
		dbConnectObject.close()

		return _climateData
	
	def checkRawData_db() -> bool:
		"""Check if today's raw data has already inserted into db
	    Returns True if today's data already exists and False if it doesn't"""

		#Today's Date formatted to be inserted into DB
		today = DTOperations.todayDate()

		dbConnectObject = DBOperations.dbConnection(DBCONFIG.adbname)

		try:
			selectCursor = dbConnectObject.cursor()
		except mariadb.Error as e:
			print(f"Error connecting to MariaDB Platform: {e}")

		try:
			selectCursor.execute("SELECT today_date FROM atmos_rawdata WHERE today_date=?", (today,))
		except mariadb.Error as e:
			print(f"Error connecting to MariaDB Platform: {e}")
		selectResult = selectCursor.fetchall()
		selectCursor.close()
		dbConnectObject.close()

		if(selectResult != []):
			return True
		else:
			return False

# AtmosphereDAO.checkRawData_db()