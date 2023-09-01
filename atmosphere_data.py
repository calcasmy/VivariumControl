#!/usr/bin/python3
import mariadb
import json
import requests
from atmosphere_dao import AtmosphereDAO
from propertyreader import APPCONFIG

class AtmosphereData:

	def getRawData_api():
		"""Request climate data from weatherapi.com for specified location
		Key for the request was fetched by logging into weatherapi.com"""

		if not AtmosphereDAO.checkRawData_db():
			try:
				climateDataRequest = requests.get(APPCONFIG.weatherAPI)
				climateData = json.loads(climateDataRequest.content)
			except requests.exceptions.RequestException as e:
				print(f"Error requesting data from WeatherAPI.com: {e}")

			if(climateDataRequest.status_code == 200):
				AtmosphereDAO.putRawData_db(climateData)
			else:
				return
		else:
			print("Today's raw data already fetched and available in db")
			return

AtmosphereData.getRawData_api()