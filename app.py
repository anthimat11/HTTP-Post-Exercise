import paho.mqtt.client as mqtt
from flask import Flask, request

app = Flask(__name__)
mqtt_client = mqtt.Client()

def on_message(client, userdata, message):
    print(f"Received message: {message.payload.decode()}")
    
mqtt_client.on_message = on_message
mqtt_client.connect("localhost", 1883)
mqtt_client.subscribe("test")
mqtt_client.loop_start()

@app.route('/publish', methods=['POST'])
def publish():
    message = request.form['message']
    mqtt_client.publish("test", message)
    return "Message published to MQTT"

if __name__ == '__main__':
    app.run(debug=True)
