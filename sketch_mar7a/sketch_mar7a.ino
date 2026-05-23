int led = 13;

void setup() {
  pinMode(led, OUTPUT);
  Serial.begin(9600);
}

void loop() {

  if (Serial.available()) {
    char comando = Serial.read();

    if (comando == '1') {
      digitalWrite(led, HIGH);
    }

    if (comando == '0') {
      digitalWrite(led, LOW);
    }
  }

}
