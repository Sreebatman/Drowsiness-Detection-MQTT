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

<img width="1582" height="797" alt="eyes_opened" src="https://github.com/user-attachments/assets/c9051b6d-4603-4893-9713-339ad9d63e66" />
---

### Drowsiness Detected

<img width="1423" height="827" alt="drowsiness_detected" src="https://github.com/user-attachments/assets/fcbe9c21-1de4-4bf9-9af2-2cbe38121fd0" />

---

### MQTT Alert Received

<img width="738" height="1600" alt="mqtt_dashboard" src="https://github.com/user-attachments/assets/81fbb99f-c77e-424a-8d3a-e5af90eea9df" />

---

### Motor Running

<img width="899" height="1599" alt="motor_on" src="https://github.com/user-attachments/assets/4aba35e2-6a2b-4b9f-8454-74c69d24967f" />

---

### Motor Stopped

<img width="1200" height="1600" alt="motor_off" src="https://github.com/user-attachments/assets/5bb51b7b-564a-4615-865e-f77526668b5a" />

---

## Future Improvements

- Buzzer Alarm
- Telegram Notification
- Firebase Cloud Logging
- Driver Monitoring Dashboard
- GPS Integration
- AI-based Fatigue Prediction

---
