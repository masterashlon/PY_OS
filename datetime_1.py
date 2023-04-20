#show info on the date or time
import time

def today():
	print(f"\tToday: {time.localtime().tm_mday} / {time.localtime().tm_mon} / {time.localtime().tm_year}")

def time_now():
	print(f"\tNow:  {time.localtime().tm_hour} : {time.localtime().tm_min} : {time.localtime().tm_sec}")