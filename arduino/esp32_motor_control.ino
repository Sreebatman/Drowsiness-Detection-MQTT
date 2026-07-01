#define IN1 25
#define IN2 26

char data = 0;
char lastCommand = 0;

void stopMotor() {
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, LOW);
}

void startMotor() {
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
}

void setup() {

  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);

  stopMotor();

  Serial.begin(115200);

  Serial.println("--------------------------------");
  Serial.println("ESP32 Motor Controller Ready");
  Serial.println("A = Motor ON");
  Serial.println("a = Motor OFF");
  Serial.println("--------------------------------");
}

void loop() {

  if (Serial.available()) {

    data = Serial.read();

    // Ignore repeated commands
    if (data == lastCommand)
      return;

    switch (data) {

      case 'A':

        startMotor();

        Serial.println("Motor ON");

        lastCommand = 'A';

        break;

      case 'a':

        stopMotor();

        Serial.println("Motor OFF");

        lastCommand = 'a';

        break;

      default:

        Serial.print("Unknown Command : ");
        Serial.println(data);

        break;
    }
  }
}
