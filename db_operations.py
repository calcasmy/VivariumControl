import mariadb
from propertyreader import DBCONFIG

class DBOperations:
    """Database operations common across all databases."""
    def dbConnection(_dbname):
        """Returns a db connection object based on the provided db name"""

        if(_dbname != ''):
            try:
                _connectObject = mariadb.connect(host=DBCONFIG.dbhost, user=DBCONFIG.dbuser, passwd=DBCONFIG.dbpassword, db=_dbname)
            except mariadb.Error as e:
                print(f"Error connecting to MariaDB Platform: {e}")
        else:
            _connectObject = None
        return _connectObject

    def dbConClose(_connectObject):
        """Closes the db connection for the provided db connection object"""
        try:
            _connectObject.close()
        except mariadb.Error as e:
            print(f"Error closing db connection: {e}")
        
DBOperations.dbConnection('atmosphere')