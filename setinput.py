import os

with open("/root/input") as f:
   input = f.read()
if "SP/DIF" in input:
   os.system('bash /root/coaxial1')
if "streamer" in input:
   os.system('bash /root/streamer')
