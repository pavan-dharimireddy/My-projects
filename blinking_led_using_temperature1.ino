int temp = 60;

int green = 6;
int red = 7;
int blue = 8;

void setup(){
  
  pinMode(green,OUTPUT);
  pinMode(red,OUTPUT);
  pinMode(blue,OUTPUT);
  
}

void loop(){
  
  if (temp > 10 && temp <50){
    
    digitalWrite(green,HIGH);
    delay(1000);
    digitalWrite(green,LOW);
    delay(1000);
    
  }
  
  else if (temp >= 50 && temp <70){
    
    digitalWrite(blue,HIGH);
    delay(1000);
    digitalWrite(blue,LOW);
    delay(1000);
    
  }
  
  else {
    
    digitalWrite(red,HIGH);
    delay(1000);
    digitalWrite(red,LOW);
    delay(1000);
    
  }
}
