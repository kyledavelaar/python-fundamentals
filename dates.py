from datetime import datetime, timedelta
import time

#######################################################
start = datetime.now()
print(f'start {start}')
time.sleep(1);

finish = datetime.now()
print(f'finish {finish}')

print(f'difference {finish - start}')

#######################################################

one_hour_ago = finish - timedelta(hours=1)
print(f'1 hour ago {one_hour_ago}')

