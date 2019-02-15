import paho.mqtt.client as maqtt
import paho.mqtt.publish as publish
import json
import random
import time


while True:

    iot_data = {
        'temperature' : random.uniform(1,40),
        'humidity' :  random.uniform(20,80)
    }


    publish.single("iot",
        payload= json.dumps(iot_data),
        hostname='127.0.0.1',
        client_id="pi",
        # qos=0
        port=1883,
        protocol=maqtt.MQTTv311 
        )
    print("发送成功")

    time.sleep(1)

