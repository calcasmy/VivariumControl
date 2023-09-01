from vivarium_data import VivariumData
from atmosphere_dao import AtmosphereDAO
from dt_operations import DTOperations
import time

class VivariumController:
    def controller():
        _astroData = AtmosphereDAO.getAstroData_db(DTOperations.todayDate())[0]

        _time = time.strftime("%I:%M %p", time.localtime())

        if(len(_astroData)> 0):
            if (_astroData[1] <= _time <= _astroData[2]):
                VivariumData.getluminosdata()
        
        VivariumData.getTempHumidData()

VivariumController.controller() 