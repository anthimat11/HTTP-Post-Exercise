# HTTP-Post-Exercise
WITH DOCKER CONTAINER

This is a simple Python application that allows you to publish messages to an MQTT broker using an HTTP POST request. The application runs in a Docker container.

Before you can run this application, you'll need to have the Docker installed on your system.

To install the application, follow these steps:

Clone this repository to your local machine using the command:
git clone https://github.com/anthimat11/HTTP-Post-Exercise

Change into the project directory.

Build the Docker image using the following command:
docker build -t mqtt-message-publisher .

Once the image is built, start the Docker container using the following command:
docker run -p 5000:5000 mqtt-message-publisher

You should now be able to access the application by navigating to http://localhost:5000 in your web browser.
