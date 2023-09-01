import configparser


config = configparser.RawConfigParser()
config.read('ConfigFile.properties')


class DBCONFIG:
    dbhost = config.get('DBSection', 'database.host')
    dbuser = config.get('DBSection', 'database.user')
    dbpassword = config.get('DBSection', 'database.password')

    adbname = config.get('DBSection', 'database.adbname')
    atrawdata = config.get('DBSection', 'database.atrawdata')
    atastrodata = config.get('DBSection', 'database.atastrodata')
    atclimatedata = config.get('DBSection', 'database.atclimatedata')

    vdbname = config.get('DBSection', 'database.vdbname')
    vtclimatedata = config.get('DBSection', 'database.vtclimatedata')
    vtluminosdata = config.get('DBSection', 'database.vtluminosdata') 

class APPCONFIG:
    weatherAPI = config.get('AppSection', 'app.weatherapi')
    I2CDHT = config.get ('AppSection', 'app.I2CDHT')
    DHT11 = config.get ('AppSection', 'app.DHT11')