
int state = 0;
int RbuttonState = 0;
int GbuttonState = 0;
int BbuttonState = 0;
int YbuttonState = 0;
int prevButtonState = 0;
void setup() {
  // put your setup code here, to run once:
  //LIGHTS
pinMode(2, OUTPUT); //RED
pinMode(3, OUTPUT); //GRN
pinMode(4, OUTPUT); //BLU
pinMode(5, OUTPUT); //YEL
  //BUTTONS
pinMode(8,INPUT_PULLUP); //RED
pinMode(9,INPUT_PULLUP); //GRN
pinMode(10,INPUT_PULLUP); //BLU
pinMode(11,INPUT_PULLUP); //YEL
  //BUZZER
pinMode(6,OUTPUT);
}

void loop() {
  RbuttonState = digitalRead(8);
  GbuttonState = digitalRead(9);
  BbuttonState = digitalRead(10);
  YbuttonState = digitalRead(11);
  if (RbuttonState == LOW){
    digitalWrite(2,HIGH);
    tone(6,262,250);
    }
  else {
    digitalWrite(2,LOW);
  }
  if (GbuttonState == LOW){
    digitalWrite(3,HIGH);
    tone(6,700,250);
    }
  else {
    digitalWrite(3,LOW);
  }
  if (BbuttonState == LOW){
    digitalWrite(4,HIGH);
    tone(6,1047,250);
    }
  else {
    digitalWrite(4,LOW);
  }
  if (YbuttonState == LOW){
    digitalWrite(5,HIGH);
    tone(6,1397,250);
    }
  else {
    digitalWrite(5,LOW);
  }
  
  delay(50);
}
