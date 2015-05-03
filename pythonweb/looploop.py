"""
This unit test is to test error messages at these situations. One is using 
savestate before having loaded at least a pubkey, and work as that identity.
Another is using savestate to a write-protected file.   
"""

import seash
import sys
import os
import seash_exceptions
import time
import subprocess

#pragma out Please load at least a pubkey, and work as that identity.
#pragma out Don't use savestate to a write-protected file.

# local webpage
outfilename = "./index.html"

# initialize credentials, load all devices
command_list = [ 
  'loadkeys hackathon', 
  'as hackathon', 
  'browse',
]

try:
  seash.command_loop(command_list)
except seash_exceptions.UserError, e:
  print "first group of commands fail\n", str(e)

# running commands, download collected data
while True:
  command_list = [ 
  'on browsegood',
  'stop',
  'start dylink.r2py encasementlib.r2py sensor_layer.r2py blur_wifi.r2py map.r2py',
  ]
  try:
    seash.command_loop(command_list)
  except seash_exceptions.UserError, e:
    print "start dylink.r2py encasementlib.r2py ... fail\n", str(e)

    time.sleep(10)   # wait for code to finish running on the devices

  command_list = [ 
  'on browsegood',
  'download location_wifi',
  ]
  try:
    seash.command_loop(command_list)
  except seash_exceptions.UserError, e:
    print "download fail\n", str(e)

  proc = subprocess.Popen('ls -l location_wifi.*', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  print proc.communicate()[0]

  f = open(outfilename, "w")
  # dump first part of the html
  subprocess.call(['cat', './part1.txt'], stdout=f)

  # populate with all the data points
  for location_file in os.listdir(os.getcwd()):
    if location_file.startswith('location_wifi'): 
      subprocess.call(['cat', location_file], stdout=f)

  # dump second part of the html    
  subprocess.call(['cat', './part2.txt'], stdout=f)
  f.close()  
  time.sleep(10)  # sleep between runs
