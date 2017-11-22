#-*- coding: utf-8 -*-
import time
while True:
    print( "########################################################################")
    print time.gmtime().tm_year, time.gmtime().tm_mon, time.gmtime().tm_mday
    print time.gmtime().tm_hour, time.gmtime().tm_min, time.gmtime().tm_sec
    time.sleep(1)
