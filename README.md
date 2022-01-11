# Signify_Cloud

The goal of the project is to build a system that will monitor older adults in their homes. The system mentioned should raise an alarm when some disturbing event like a fall happens. Monitoring is done by radar sensors that can be placed in older adult homes. Based on algorithms processing sensorics data, system will be able to determine if a fall occurred. In order to check how accurately fall events can be detected, a series of fall and non-fall scenarios will be executed. Sensor and reference data (later called ground truth) will be gathered during those experiments. During the project team needs to build a infrastructure for data visualization in the cloud using chose AWS services. Building data infrastructure in the cloud enables better storage option and visualization tooling. Visualization dashboard will help the team to estimate sensors performance.

## Use AMZ Webservice: EC2, Lambda. 
![image](https://user-images.githubusercontent.com/50198601/138552823-218abff1-5362-4fce-b68f-051149a52557.png)

## Connect to influxDb to build Grafana-Dashboard
![ABC](https://github.com/MarkRichers/Signify_Cloud/blob/new_path/Capture.PNG)

![ABCD](https://user-images.githubusercontent.com/50198601/142849287-748017ff-2466-43af-b77b-a18fd30e8c62.png)

## InfluxDB-Terminal
![image](https://user-images.githubusercontent.com/50198601/138552983-59cbf4b8-5818-416d-8ee6-304a2efc6a79.png)


## The code for InfluxDB
- Use Python to upload to Lambda Rest API. 
- Lambda merge the data to EC2 instance where InfluxDB is Hosted. 
- Grafana load the database from InfluxDB.
- Apply Private API and VPC + Cloud Formation. 
### Using Port For Grafana
Created an EC2 instance to install Grafana. 
### Creating a decoration

Access Terminal-Linux-Ubuntu to see databases. 

```coffee
influx

show databases

SHOW MEASUREMENTS

select * from fall_detections

```

Following by the JSON file:

```coffee
{ "sensor_id": "id", "sensor_name": "fall_detection_menaingful_name_string", "fall_detection": "1/0", "elevation": "Z", "x_coordinate": "X", "y_coordinate": "Y", "velocity": "V", "motion": "motion_level", "time": "timestamp" }
```
### Settup Cloud-Service with Lambda, EC2 instance, and VPC, IAM role. 
### Time Stream
![Capture](https://user-images.githubusercontent.com/50198601/148988881-f582c340-c9f3-489e-bb6f-076c8803d878.PNG)

