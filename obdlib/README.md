## obdlib

An On-Board Diagnostics (OBD) library for collecting vehicular sensor data in repy.
This script also manages the vehicular sensor data formatting and calculating,
as well as saving that data to a file so that one may back haul it
to a server or database.


### obd_example.r2py

```python
dy_import_module_symbols("obdlib.r2py") 
dy_import_module_symbols("sensorlib.r2py")
storesense = dy_import_module('storesense.r2py')

# Set sensor socket for sensorlib.r2py.
port = get_connectionport()
sensorsocket = getconnection(port)
setSensorPort(port)

local_port = 63100 # any local port you wish

# Use the customSetup() function in obdlib.r2py to set obd 
# sensor's ip, port, and localport.
customSetup("192.168.0.10", 35000, local_port)

storesense.init()
data = []
device_id = request_data(sensorsocket, 'getSimSerialNumber', [])

# Collect 60 data entries every 5 seconds.
counter = 0
while counter<60:
  counter = counter+1
  write_obd_data_to_file(filename)
  # Turn off the wifi, and connect to cellular network for POSTing.
  log("\nStatus: ",request_data(sensorsocket,'toggleWifiState',[]))
  sleep(5) # Give phone time to accomplish this.

# Read filename (my_trip.txt) and save into string r.
file = openfile("my_trip.txt", True)
car_data = file.readat(None, 0)
file.close()

# Backhaul to sensevis
storesense_post(car_data, device_id, 'sensevis_username', 'sensevis_password', 0)
```

