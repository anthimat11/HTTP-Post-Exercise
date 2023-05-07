# HTTP-Post-Exercise
This exercise is part of The Advanced Programming Techniques class. 
This is a simple Python application that allows you to publish MQTT messages via an HTTP POST request using the Flask web framework.

Before you can run this application, you'll need to install the following:
Python 3.x
Flask
paho-mqtt

You can install Flask and paho-mqtt using pip:

pip install Flask paho-mqtt

You'll also need to have a running MQTT broker to publish messages to. I recommend using the Mosquitto broker, which you can download and install from the official website.

To use this application, follow these steps:

Start the Mosquitto broker in a terminal window:
mosquitto

In a new terminal window, start the Flask app by running the following command from the directory containing the app.py file:
python app.py

In a third terminal window, use the curl command to send an HTTP POST request to the Flask app:
curl --data "message=Hello MQTT!" http://localhost:5000/publish


If everything is set up correctly, you should see the message you sent printed to the console in the terminal window where you started the Flask app.
