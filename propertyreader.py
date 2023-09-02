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
    DHTSI2C = config.get ('AppSection', 'app.DHTSI2C')
    DHTS11 = config.get ('AppSection', 'app.DHTS11')