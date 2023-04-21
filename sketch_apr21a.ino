
const int buttonPin = 2;
int buttonState = 0;
int status = 0;

void setup() {
  pinMode(buttonPin, INPUT);
  status = 0;
}

void loop() {
  // read the state of the pushbutton value:
  buttonState = digitalRead(buttonPin);

  // check if the pushbutton is pressed. If it is, the buttonState is HIGH:
  if (buttonState == HIGH) {
    if (status == 0){
      serial.writeln("start");
    }
    else{

    }
  }
  else {
    if (status == 1){}
      serial.writeln("stop");
  }
}
