# Report device load stats to Watson IoT Platform
import os
import time
import json

from datetime import datetime


waitInterval=[1]

def get_system_load():
	load = json.loads(os.popen('./sys-stats.sh').read())
	load['timestamp'] = datetime.now().isoformat()
	return load

	

while True:
	data = get_system_load()
	print data
	time.sleep(waitInterval[0])

