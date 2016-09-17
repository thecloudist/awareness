from gopigo import *
import time
enable_servo()
for i in range(180):
   servo(i)
   time.sleep(100)
