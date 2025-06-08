// Teensyduino sketch
// Receives '1' via UART and clicks left mouse button

void setup() {
  Serial.begin(9600);      // Start UART communication
  Mouse.begin();           // Start mouse emulation
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();

    if (command == '1') {
      Mouse.click(MOUSE_LEFT);     // Simulate left mouse click
      delay(50);                   // Short debounce delay
    }
  }
}
