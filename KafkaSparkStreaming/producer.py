from time import sleep
from json import dumps
from kafka import KafkaProducer
import pandas as pd
import json
import csv

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
value_serializer=lambda x:
dumps(x).encode('utf-8'))
with open('./boston.csv') as file:
    reader = csv.DictReader(file, delimiter=';')    
    producer.send('topic-name',value='test')  
    for row in reader:
        data = json.dumps(row)
        
        producer.send('topic-name',value=data)
        sleep(1)
        print("Successfully sent data to kafka topic")