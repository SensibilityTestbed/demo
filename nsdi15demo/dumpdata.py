import os
import subprocess

outfilename = "./test.html"
f = open(outfilename, "w")

subprocess.call(['cat', './part1.txt'], stdout=f)

for location_file in os.listdir(os.getcwd()):
  if location_file.startswith('location_wifi'): 
    subprocess.call(['cat', location_file], stdout=f)

subprocess.call(['cat', './part2.txt'], stdout=f)
f.close()
