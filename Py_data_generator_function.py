
import datetime
from influxdb import InfluxDBClient
import time
import random   
import time
import sched, time
from apscheduler.schedulers.blocking import BlockingScheduler
import json
import requests

def data_generator():
    print("Data: ")
    # input nessary function for port 8086 which is connected to InfludxDB . 
    url = "https://vmu8dcjc8j.execute-api.eu-central-1.amazonaws.com/default/Data_Moving"
    ifuser = "grafana"
    ifpass = "thienphuc"
    ifdb   = "home"
    # ifhost = "ec2-3-125-120-129.eu-central-1.compute.amazonaws.com"
    # ifhost = "localhost"
    ifport = 8086
    # Set up measure name fall_detections. 
    measurement_name_Fall_dectections = "fall_detections"

    # take a timestamp for this measurement
    timeinflux = time.time_ns() 
    # -> etc timezone amsterdam. It mean utc() + 2 already settup in the computer time. 

    # build random in 3 main room. 
    sensors = ['Sensor_kitchen','Sensor_living','Sensor_sleeping']

    dbline_Fall_detections = {"Data": []}  
    # Add random data_dummies from random number
    for _ in range(10):
        Sensor = random.choice(sensors)
        Velocity = str(random.randint(0,5))
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
        )

    with open('file.json', 'a') as outfile:
        outfile.write(json.dumps(dbline_Fall_detections))
        # outfile.write("")
        outfile.close()

    db_fall_0 = dbline_Fall_detections["Data"][0]
    db_fall_2 = dbline_Fall_detections["Data"][1]
    db_fall_3 = dbline_Fall_detections["Data"][2]
    db_fall_4 = dbline_Fall_detections["Data"][3]
    db_fall_5 = dbline_Fall_detections["Data"][4]
    db_fall_6 = dbline_Fall_detections["Data"][5]
    db_fall_7 = dbline_Fall_detections["Data"][6]
    db_fall_8 = dbline_Fall_detections["Data"][7]
    db_fall_9 = dbline_Fall_detections["Data"][8]
    db_fall_10 = dbline_Fall_detections["Data"][9]

    headers =  {"x-api-key":"GEMJ8R3HbE7iHLhCvANuS8c0enMHeudEaEIn2p36"}

    send_data_post_json = requests.post(url, json = db_fall_0,headers=headers)
    # time.sleep(1)
    send_data_post_json1 = requests.post(url, json = db_fall_2,headers=headers)
    # time.sleep(1)
    send_data_post_json2 = requests.post(url, json = db_fall_3,headers=headers)
    # time.sleep(1)
    send_data_post_json3 = requests.post(url, json = db_fall_4,headers=headers)
    # time.sleep(1)
    send_data_post_json4 = requests.post(url, json = db_fall_5,headers=headers)
    # time.sleep(1)
    send_data_post_json5 = requests.post(url, json = db_fall_6,headers=headers)
    # time.sleep(1)
    send_data_post_json6 = requests.post(url, json = db_fall_7,headers=headers)
    # time.sleep(1)
    send_data_post_json7 = requests.post(url, json = db_fall_8,headers=headers)
    # time.sleep(1)
    send_data_post_json8 = requests.post(url, json = db_fall_9,headers=headers)
    # time.sleep(1)
    send_data_post_json11 = requests.post(url, json = db_fall_10,headers=headers)
    # time.sleep(1)

    print(send_data_post_json11.text)

    # # connect to influx 
    # if_client_data_input = InfluxDBClient(ifhost,ifport,ifuser,ifpass,ifdb)
    # if_client_data_input.write_points(db_fall_0)
    # if_client_data_input.write_points(db_fall_2)

if __name__ == "__main__":
    data_generator()

time_on = BlockingScheduler()
time_on.add_job(data_generator, 'interval', seconds=10)
time_on.start()

