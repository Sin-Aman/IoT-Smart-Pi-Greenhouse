# IoT-Smart-Pi-Greenhouse

## Introduction
Welcome to the Smart Pi Greenhouse project repository! This project addresses the challenges in modern agriculture by leveraging IoT technology to create a smart mini greenhouse. Our solution, powered by Raspberry Pi, integrates advanced sensors and actuators to monitor and regulate environmental conditions for optimal plant growth. This collaborative endeavor was undertaken by myself and Naif for the coursework on the Internet of Things.

## Problem
Traditional agriculture struggles to maintain precise environmental conditions, leading to resource inefficiencies and suboptimal plant growth. The Smart Pi Greenhouse aims to overcome these challenges through accurate monitoring and control, enhancing agricultural efficiency and sustainability.

## Solution
Our IoT-based mini greenhouse utilizes a Raspberry Pi as the central control unit. It incorporates a DHT22 sensor for humidity and temperature, a soil moisture sensor, a servo motor for window automation, and a fan motor for temperature regulation.

## Architecture
![image](https://github.com/Sin-Aman/IoT-Smart-Pi-Greenhouse/assets/108439592/1c501d11-68ad-4a6d-9073-5dcf61b24502)

## Hardware Components:
-	Raspberry Pi 3b+: At the heart of our mini greenhouse project, the Raspberry Pi 3b+ serves as the brain, orchestrating communication and control among all components. This credit-card-sized computer allows us to program and automate the greenhouse's responses based on data from the sensors.
-	DHT22 Sensor (Humidity and Temperature): The DHT22 sensor is the eyes and ears of our project, diligently monitoring the greenhouse's atmospheric conditions. It provides real-time data on humidity and temperature, offering crucial insights into the environmental well-being of the plants.
-	Soil Moisture Sensor LM393 3.3V-5V: The soil moisture sensor delves beneath the surface, gauging the moisture content in the soil. This information guides our irrigation system, ensuring plants receive the right amount of water for optimal growth and health.
-	5V DC Motor (Fan): The 5V DC motor operates our fan, a guardian against overheating. Triggered by temperature and humidity settings, the fan activates to expel excess heat, maintaining a conducive climate within the greenhouse for plant growth.
-	 Mini Servo (Window Control): Functioning as the caretaker of ventilation, the mini servo opens and closes the greenhouse window based on temperature settings. This dynamic control mechanism ensures a balanced and controlled airflow for the well-being of the plants.
-	Connecting Wires and Breadboard: These unsung heroes form the connective tissue of our project, linking the various components to the Raspberry Pi. The breadboard provides a structured platform for secure connections, enabling seamless communication among the ensemble.
-	Red and Green LED Lights: The red and green LED lights act as visual indicators, communicating the status of the greenhouse. Red signifies dry conditions, while green indicates optimal moisture conditions. This human-friendly interface allows for quick assessment without delving into technical details.
-	10 Kilo-Ohm Resistors: The 10  K-Ohm resistors play a crucial role in protecting components like LEDs from excessive current flow. Placed in series with the LEDs, they ensure that the lights operate within their safe operating range, contributing to the longevity and reliability of the visual indicators.
-	Piezo Electric Buzzer: The piezoelectric buzzer adds an audible dimension to our project. It sounds an alert when the soil moisture falls below the desired level, prompting timely intervention to prevent dehydration stress in the plants.-	16x2 Display: Our 16x2 display serves as the project's communicator, providing a user-friendly interface for real-time data. It showcases temperature and humidity levels in the greenhouse, as well as the moisture content in the soil, allowing users to stay informed at a glance.
-	Raspberry Pi Peripherals: keyboard, mouse, and monitor. 

## Software Components:
- Raspberry Pi OS: The operating system running on the Raspberry Pi, provides the necessary software infrastructure to operate your hardware and run the code for monitoring and automation.
-	Integrated Development Environment (IDE): The software application used for writing the Python code that controls the greenhouse system. The specific IDE isn't mentioned, but it could be something like Thonny, which is commonly used with Raspberry Pi.
-	PuTTY: This terminal emulator application is used for remote access to Raspberry Pi's command line interface over SSH, enabling code management and system operation from a different computer.
-	VNC Viewer: Allows for remote graphical desktop sharing, enabling you to access and interact with the Raspberry Pi's desktop environment from another device.

## Deliverables
The project delivers a fully operational smart greenhouse model, showcasing real-time environmental monitoring, automated control systems, and the integration of IoT technology for enhanced agricultural efficiency.
![IMG_6747](https://github.com/Sin-Aman/IoT-Smart-Pi-Greenhouse/assets/108439592/74e0176f-dce1-4940-82e3-c94d794253be)


