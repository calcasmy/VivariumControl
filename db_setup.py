import mariadb

from propertyreader import DBCONFIG
from db_operations import DBOperations

class DBSetup:
    def setupDatabase():
        try:
            _dbconnectObj = mariadb.connect(
                host = DBCONFIG.dbhost,
                user = DBCONFIG.dbuser,
                passwd = DBCONFIG.dbpassword
            )
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")

        _dbCursorObj = _dbconnectObj.cursor()

        try:
            _dbCursorObj.execute(
                "CREATE DATABASE IF NOT EXISTS ?",
                (DBCONFIG.adbname)
            )
            _dbCursorObj.execute(
                "CREATE DATABASE IF NOT EXISTS ?",
                (DBCONFIG.vdbname)
            )
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
        finally:
            _dbCursorObj.close()
            _dbconnectObj.close()

    def setupDBTables():
            
        _adbConnectionObj = DBOperations.dbConnection(DBCONFIG.adbname)
        _vdbConnectionObj = DBOperations.dbConnection(DBCONFIG.vdbname)

        _adbCursorObj = _adbConnectionObj.cursor()
        _vdbCursorObj = _vdbConnectionObj.cursor()

        # print("CREATE TABLE IF NOT EXISTS ? (today_date date NOT NULL, rawdata  JSON DEFAULT NULL,PRIMARY KEY (today_date))",
        #                           (DBCONFIG.atrawdata,))

        try:
            _adbCursorObj.execute("CREATE TABLE IF NOT EXISTS {} (today_date date NOT NULL, rawdata  JSON DEFAULT NULL, PRIMARY KEY (today_date))".format(DBCONFIG.atrawdata))
            _adbCursorObj.execute("CREATE TABLE IF NOT EXISTS {} (today_date date NOT NULL, sunrise char(10) DEFAULT NULL, sunset char(10) DEFAULT NULL, moonrise char(10) DEFAULT NULL, moonset char(10) DEFAULT NULL, moonphase char(50) DEFAULT NULL, PRIMARY KEY (today_date))".format(DBCONFIG.atastrodata))
            _adbCursorObj.execute("CREATE TABLE IF NOT EXISTS {} (today_date date NOT NULL, maxtemp_c char(10) DEFAULT NULL, maxtemp_f char(10) DEFAULT NULL, mintemp_c char(10) DEFAULT NULL, mintemp_f char(10) DEFAULT NULL, avgtemp_c char(10) DEFAULT NULL, avgtemp_f char(10) DEFAULT NULL, PRIMARY KEY (today_date))".format(DBCONFIG.atclimatedata))
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
        finally:
            _adbCursorObj.close()
            _adbConnectionObj.close()
        
        try:
            _vdbCursorObj.execute("CREATE TABLE viva_climatedata (today_dttm datetime NOT NULL, viva_temperature double DEFAULT NULL, viva_humidity double DEFAULT NULL, PRIMARY KEY (today_dttm))".format(DBCONFIG.vtclimatedata))
            _vdbCursorObj.execute("CREATE TABLE viva_luminosdata (today_dttm datetime NOT NULL, viva_luminos double DEFAULT NULL, PRIMARY KEY (today_dttm))".format(DBCONFIG.vtluminosdata))
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
        finally:
            _vdbCursorObj.close()
            _vdbConnectionObj.close()

DBSetup.setupDBTables()