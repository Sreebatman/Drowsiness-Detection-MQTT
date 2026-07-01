# Driver Drowsiness Detection using OpenCV, MediaPipe, ESP32 & MQTT

A real-time Driver Drowsiness Detection System that detects prolonged eye closure using MediaPipe Face Mesh and Eye Aspect Ratio (EAR). When drowsiness is detected, the system stops the motor through ESP32 and sends an alert notification to a mobile phone using MQTT.

---

## Features

- Real-time eye tracking
- Eye Aspect Ratio (EAR) calculation
- Drowsiness detection
- ESP32 motor control
- MQTT mobile notification
- Computer Vision + IoT integration

---

## Technologies Used

- Python
- OpenCV
- MediaPipe
- SciPy
- PySerial
- Paho MQTT
- ESP32
- L298N Motor Driver
- MQTT Dashboard

---

## Project Workflow

```
Camera
   │
   ▼
OpenCV
   │
   ▼
MediaPipe Face Mesh
   │
   ▼
EAR Calculation
   │
   ▼
Eyes Closed > 2 Seconds
   │
   ├────────► ESP32
   │             │
   │             ▼
   │        Stop Motor
   │
   └────────► MQTT Broker
                 │
                 ▼
          MQTT Dashboard
```

---

## Project Structure

```
Drowsiness-Detection-MQTT
│
├── drowsiness.py
├── requirements.txt
├── README.md
│
└── arduino
      └── esp32_motor_control.ino
```

---

## Installation

Create Virtual Environment

```bash
python -3.10 -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

Run

```bash
python drowsiness.py
```

---

## MQTT Configuration

Broker

```
broker.hivemq.com
```

Port

```
1883
```

Topic

```
drowsiness/alert
```

---

## Hardware Used

- ESP32
- L298N Motor Driver
- DC Motor
- Webcam
- Laptop
- Android Phone

---

# Demonstration

### Eyes Open

![Eyes Open](screenshots/eyes_open.png)

---

### Drowsiness Detected

![Drowsiness](screenshots/drowsiness_detected.png)

---

### MQTT Alert Received

![MQTT](screenshots/mqtt_dashboard.jpg)

---

### Motor Running

![Motor ON](screenshots/motor_on.jpg)

---

### Motor Stopped

![Motor OFF](screenshots/motor_off.jpg)

---

## Future Improvements

- Buzzer Alarm
- Telegram Notification
- Firebase Cloud Logging
- Driver Monitoring Dashboard
- GPS Integration
- AI-based Fatigue Prediction

---
