/*
 * 
 *
 * Wiring: Ultrasonic Sensor -> Arduino:
 * - VCC  -> 5V
 * - TRIG -> Pin 9
 * - ECHO -> Pin 8
 * - GND  -> GND
 *
 * Tutorial is available here: https://arduinogetstarted.com/tutorials/arduino-ultrasonic-sensor
 */

const int TRIGPin = 3;    // TRIG pin
const int ECHOPin = 2;    // ECHO pin

float duration,distance;  // distance in cm and duration in us(micro seconds)

void setup() {
  // begin serial port
  Serial.begin(9600);

  // configure the trig pin to output mode ---> transmitting the signal
  pinMode(TRIGPin,OUTPUT);
  // configure the echo pin to input mode ---> receiveing the signal
  pinMode(ECHOPin,INPUT);
}

void loop() {
  // generating a  10-microsecond pulse to TRIG pin
  digitalWrite(TRIGPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIGPin, LOW);

  // Reads the echoPin, returns the sound wave travel time in microseconds
  // measure the duration of pulse from ECHO pin
  duration = pulseIn(ECHOPin, HIGH);

  // calculate the distance
  distance = 0.017 * duration;

  // print the value in  Serial Monitor
  Serial.print("distance: ");
  Serial.print(distance);
  Serial.println(" cm");

  delay(500);
}
