
from ast import While
import datetime
# from influxdb import InfluxDBClient
import time
import random   
import time
import sched, time
# from apscheduler.schedulers.blocking import BlockingScheduler
import json
import requests
import csv
import numpy as np
import pandas as pd
# from requests.api import head
# import tzlocal

# def data_generator():
print("Data Sent: ")
# input nessary function for port 8086 which is connected to InfludxDB . 

url = "https://vmu8dcjc8j.execute-api.eu-central-1.amazonaws.com/default/Data_Moving"
# url = "https://svmogk42gh.execute-api.eu-central-1.amazonaws.com/default/Data_InfluxDB_Parsing"
measurement_name_Fall_dectections = "fall_detections"

# take a timestamp for this measurement

sensors = ['Sensor_kitchen','Sensor_living','Sensor_sleeping']
# build random in 3 main room. 
header = ['measurement', 'time','sensor_id','Sensor','Velocity','fall_detection','elevation','x_coordinate','y_coordinate','motions']

dbline_Fall_detections = {"Data": []}  
# Add random data_dummies from random number
while True: 
    timeinflux = time.time_ns() 
    Sensor = random.choice(sensors)
    Velocity = random.randint(0,5)
    fall_detection = random.randint(0,1)
    elevation = random.uniform(0,6) # 6 meter ....
    x_coordinate = random.uniform(0,5) # 5 meter ....
    y_coordinate = random.uniform(0,3) 
    motions = random.uniform(0,100) 
    sensor_id = 'sensor_' + str(random.randint(0,3))
# format the data as a single measurement for influx , db line protocal json. 
            
    # dbline_Fall_detections["Data"].append(
    #     {
    #     "measurement": measurement_name_Fall_dectections, 
    #     "time":timeinflux,    
    #     "sensor_id": sensor_id,
    #     "Sensor": Sensor,
    #     "Velocity": Velocity,
    #     "fall_detection":fall_detection,    
    #     "elevation":elevation, 
    #     "x_coordinate":x_coordinate, 
    #     "y_coordinate":y_coordinate, 
    #     "motions":motions
    #     }
    # )
    
    data = {
        "measurement": measurement_name_Fall_dectections, 
        "time":timeinflux,    
        "sensor_id": sensor_id,
        "Sensor": Sensor,
        "Velocity": Velocity,
        "fall_detection":fall_detection,    
        "elevation":elevation, 
        "x_coordinate":x_coordinate, 
        "y_coordinate":y_coordinate, 
        "motions":motions
        }

    headers =  {"x-api-key":"gcMq0YtuSm47UP62GiriW1SUFILWOoq38BUIWntO"}

    # send_data_post_json = requests.post(url, json = data,headers=headers)
    # response = requests.get(url)
    # response.text
    print(data)
    time.sleep(1)


