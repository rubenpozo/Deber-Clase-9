import time
import os
for x in range(0,120):
	t=time.localtime()
	hour=t[3]
	minute=t[4]
	second=t[5]
	print(hour,": ",minute,": ",second)
	time.sleep(1)
	os.system('cls')