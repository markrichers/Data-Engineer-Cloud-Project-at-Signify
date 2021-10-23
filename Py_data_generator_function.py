
import datetime
from influxdb import InfluxDBClient
import time
import random
import time
import sched, time
from apscheduler.schedulers.blocking import BlockingScheduler

def data_generator():
    print("Data: ")
    # input nessary function for port 8086 which is connected to InfludxDB . 
    ifuser = "grafana2"
    ifpass = "thienphuc"
    ifdb   = "home1"
    ifhost = "127.0.0.1"
    ifport = 8086
    # Set up measure name fall_detections. 
    measurement_name_Fall_dectections = "fall_detections"

    # take a timestamp for this measurement
    time = datetime.datetime.utcnow() 
    # -> etc timezone amsterdam. It mean utc() + 2 already settup in the computer time. 

    # build random in 3 main room. 
    sensors = ['Sensor_kitchen','Sensor_living','Sensor_sleeping']

    # Add random data_dummies from random number
    for i in range(1):
        Sensor = random.choice(sensors)
        Velocity = random.randint(0,5)
        fall_detection = random.randint(0,1)
        elevation = random.uniform(0,6) # 6 meter ....
        x_coordinate = random.uniform(0,5) # 5 meter ....
        y_coordinate = random.uniform(0,3) 
        motions = random.uniform(0,100) 
        sensor_id = 'sensor_' + str(random.randint(0,3)) 
    # format the data as a single measurement for influx , db line protocal json. 
    dbline_Fall_detections = [
    {
        "measurement": measurement_name_Fall_dectections,
        "time": time,
        "tags":{
            "sensor_id":sensor_id # 1 2 3. 
        },
        "fields": {
            "Sensor": Sensor,
            "Velocity": Velocity,
            "fall_detection": fall_detection,
            "elevation": elevation,
            "x_coordinate": x_coordinate,
            "y_coordinate": y_coordinate,
            "motions": motions
        }
    }
    ]
    print(dbline_Fall_detections)

    # connect to influx 
    if_client_data_input = InfluxDBClient(ifhost,ifport,ifuser,ifpass,ifdb)
    # write the measurement
    if_client_data_input.write_points(dbline_Fall_detections)

#     s.enter(2, 1, data_generator, (sc,))

# s.enter(2, 1, data_generator, (s,))
# s.run()
time_on = BlockingScheduler()
time_on.add_job(data_generator, 'interval', seconds=1)
# intervew of second: possible to adjust. 
time_on.start()

# line plot - 2 dashboard. 
# Add the description in Jira - add screen shot. ( show outpu trsult in jira  )
# commit the git repos.

