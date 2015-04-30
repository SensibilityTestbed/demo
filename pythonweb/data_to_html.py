""" Modifies a .html file

Function to populate index.html with location/wifi data from generated .txt files

"""

import os 
loc_wifi = []  # string to store all needed data 

# find the data files in the current directory
for location_file in os.listdir(os.getcwd()):
  if location_file.startswith('location_wifi'): 
    f = open(location_file, "r")
    # store location/wifi data
    for line in f:
      line = line.split()
      loc_wifi.append(line)
    f.close()  

# organize data
location = loc_wifi[0::2]
wifi = loc_wifi[1::2]

# build location strings
locations = []
for i in range(0, len(location)):
  locations.append("['SSID: " + wifi[i][0] + "<br>Link speed: " + wifi[i][1] +
                   " Mbps<br>RSSI: " + wifi[i][2] + " dBM'" + ", " + 
                   location[i][1] + ", " + location[i][2] + "]")

# make a buffer copy of index.html
with open("index.html", "r") as f:
  lines = f.readlines()
f.close()

start = 14 # line after "var locations = ["
end = 0
for i in range(0, len(lines)):
  if "var map;" in lines[i]: # line after list of points
    end = i
    break
  
# clear lines with whitespace and make a copy of lines after lines[end]
lines_copy = lines[end:]
for i in range(start, end): 
  lines[i] = ""
  
# populate index.html
for i in range(0, len(locations)):
  if i == len(locations) - 1:
    lines[start+i] = "  " + locations[i] + "\n"
  else:
    lines[start+i] = "  " + locations[i] + ",\n"
 
lines[start+len(locations)] = "];\n"
lines[start+len(locations)+1:] = lines_copy
with open("index.html", "w") as f:
  f.writelines(lines)  
f.close()
