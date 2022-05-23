
import datetime
from influxdb import InfluxDBClient
import time
import random   
import time
import sched, time
from apscheduler.schedulers.blocking import BlockingScheduler
import apscheduler.schedulers.background
import json
import requests
import csv
import numpy as np
import pandas as pd
from requests.api import head


INTERVAL = 1 # Seconds

# def data_generator():
print("Data Sent: ")

ifhost = "ec2-3-125-120-129.eu-central-1.compute.amazonaws.com"
url = "https://vbsx0pji89.execute-api.eu-central-1.amazonaws.com/default/Data_Timestream"
measurement_name_Fall_dectections = "fall_detections"

# build random in 3 main room. 
sensors = ['Sensor_kitchen','Sensor_living','Sensor_sleeping']

header = ['measurement', 'time','sensor_id','Sensor','Velocity','fall_detection','elevation','x_coordinate','y_coordinate','motions']

dbline_Fall_detections = {"Data": []} 
# Add random data_dummies from random number
while True: 
# for _ in range(10): 
    current_time = int(time.time() * 1000)
    Sensor = random.choice(sensors)
    Velocity = random.randint(0,5)
    fall_detection = random.randint(0,1)
    elevation = random.uniform(0,6) # 6 meter ....
    x_coordinate = random.uniform(0,5) # 5 meter ....
    y_coordinate = random.uniform(0,3) 
    motions = random.uniform(0,100) 
    sensor_id = 'sensor_' + str(random.randint(0,3)) 
# format the data as a single measurement for influx , db line protocal json. 
            
    dbline_Fall_detections["Data"].append(
        {
        "measurement": measurement_name_Fall_dectections, 
        "time":current_time,    
        "sensor_id": sensor_id,
        "Sensor": Sensor,
        "Velocity": Velocity,
        "fall_detection":fall_detection,    
        "elevation":elevation, 
        "x_coordinate":x_coordinate, 
        "y_coordinate":y_coordinate, 
        "motions":motions
        }
    )
    
    data = {
        "measurement": measurement_name_Fall_dectections, 
        "time":current_time,    
        "sensor_id": sensor_id,
        "Sensor": Sensor,
        "Velocity": Velocity,
        "fall_detection":fall_detection,    
        "elevation":elevation, 
        "x_coordinate":x_coordinate, 
        "y_coordinate":y_coordinate, 
        "motions":motions
        }

    
    headers =  {"x-api-key":"GEMJ8R3HbE7iHLhCvANuS8c0enMHeudclsEaEIn2p36"}

    send_data_post_json = requests.post(url, json = data)
    response = requests.get('https://vbsx0pji89.execute-api.eu-central-1.amazonaws.com/default/Data_Timestream')
    response.text
    # send data into the lambda function at AWS. 
    print(data)
    time.sleep(INTERVAL)
 



