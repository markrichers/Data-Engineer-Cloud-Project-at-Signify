import boto3
import json
from influxdb import InfluxDBClient

def respond(res):
    return {
        'statusCode': '200', 
        'body': json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
        },
    }

def lambda_handler(event, context):
    decodedBody = json.loads(event['body'])
    measurement = decodedBody['measurement']
    time = decodedBody['time']
    sensor_id = decodedBody['sensor_id']
    Sensor = decodedBody['Sensor']
    Velocity = decodedBody['Velocity']
    fall_detection = decodedBody['fall_detection']
    elevation = decodedBody['elevation']
    x_coordinate = decodedBody['x_coordinate']
    y_coordinate = decodedBody['y_coordinate']
    motions = decodedBody['motions']
    
    dbline_Fall_detections = [{
        "measurement": measurement,
        "time": time,
        "tags":{
            "sensor_id":sensor_id, # 1 2 3. 
            "Sensor": Sensor
        },
        "fields": {
            "Velocity": Velocity,
            "fall_detection": fall_detection,
            "elevation": elevation,
            "x_coordinate": x_coordinate,
            "y_coordinate": y_coordinate,
            "motions": motions
        }
    }]
  
    ifuser = "grafana"
    ifpass = "thienphuc"
    ifdb   = "home"
    ifhost = "ec2-3-65-21-217.eu-central-1.compute.amazonaws.com"
    ifport = 8086
    if_client_data_input = InfluxDBClient(ifhost,ifport,ifuser,ifpass,ifdb)
    if_client_data_input.write_points(dbline_Fall_detections)
    writingSuccess = if_client_data_input.write_points(dbline_Fall_detections)
    
    # return respond({measurement})

    return respond({"Data: ": dbline_Fall_detections, "Result": writingSuccess})