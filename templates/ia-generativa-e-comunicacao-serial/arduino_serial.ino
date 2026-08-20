const int LED = LED_BUILTIN;

void setup() {
  pinMode(LED, OUTPUT);

  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {

    char comando = Serial.read();

    if (comando == 'a') {
      digitalWrite(LED, HIGH);
    }

    else if (comando == 'b') {
      digitalWrite(LED, LOW);
    }
  }
}