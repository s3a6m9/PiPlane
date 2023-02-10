// Sliding Potentiometer
int potmeterPin = A0;
int potmeterVal = 0;

// joystick
int swPin = 12;  // button
int switchState = 1;

int VrxPin = A5;
int VryPin = A1;
int x = 0;
int y = 0;


String combined;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(swPin, INPUT);  // button
  digitalWrite(swPin, HIGH);  // button
}

void loop() {
  // put your main code here, to run repeatedly:
  potmeterVal = analogRead(potmeterPin);
  
  x = analogRead(VryPin);
  y = analogRead(VrxPin);
  switchState = digitalRead(swPin);

  combined = "s" + String(x) + " " + String(y) + " " + String(potmeterVal) + " " + String(switchState) + "e";
  Serial.println(combined);

  delay(20);
}
