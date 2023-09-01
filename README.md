# Vivarium
Attempt to created a completely automated and environment controlled Vivarium using Raspberry PI

Introduction:

  Goal: To create a completely automated environment controlled Vivarium (Orchidarium) using Raspberry Pi, which can be used for both plants and/or animals if desired. But since I am only attempting to grow orchids, will only refer to plants in the future and not will not mention animals.
  
  **_Ideas:_**
  1. Humidity Control:
  _  Control air moisture using a cool mist humidifer that runs automatically based on the input acquired from humidity sensor. Ability to simulate daily and seasonal changes based on plant profile if available. If not, based on instructions.
        
  2. Grow lights:
  _  Mode 1: Automated lights based on the natural weather predecitions if placed near a bright window.
    Mode 2: If completely indoors, away from birght window, operate grow lights. If dimmable, using PWM, simulate sunrise and sunset including lighting                 duration bsed on seasons and plant profile.
        
  3. Temperature Control:
  _   Mode 1: If plant profile available, simulate day/night and seasonal temperature changes based on inputs from temperature sensor. Control fans and heater either to cool or to heat as needed.
        
  4. Irrigation:
  _   Drip Irrigation:
      _  Mode 1: Plant Profile
           If plant profile available, drip irrigate as per schedule provided and if planted in medium, data from plant medium moisture sensor if one available.
      _  Mode 2: Instruct.
           If Plant provile not available, ability to automate drip irrigation as instructed (Intervals, start time, end time. If plant medium moisture senor available, then end time will be replaced with mositure sensor data.
                
 _    Nutrient feed:
        Mode 1: Plant Profile
           If plant profile available, drip irrigate as per schedule provided and if planted in medium, data from plant medium moisture sensor if one available.
        Mode 2: Instruct.
           If Plant provile not available, ability to automate drip irrigation as instructed (Intervals, start time, end time. If plant medium moisture senor available, then end time will be replaced with mositure sensor data.
                
**_Construction:_**

  1. Raspberry PI and other instrument housing.
     Created the Inkspace SVG file for Raspberry Pi 3 B from the [Mechanical drawings](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#schematics-and-mechanical-drawings) available at raspberrypi.com.
