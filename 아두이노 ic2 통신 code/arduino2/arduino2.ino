// 적외선 거리센서 B1 + led 파랑
// 감지 센서 B2 + led 파랑
// 불꽃센서 B + led 빨강
#include <Wire.h>
#define SLAVE 2

char Big = ' ';

int IR_SENSOR_B1 = 0; // Sensor is connected to the analog A0
int intSensorResult_B1 = 0; //Sensor result
float fltSensorCalc_B1 = 0; //Calculated value
int LED_B1 = 3;

int sensorPin_B2 = A1;    // select the input pin for the potentiometer
int LED_B2 = 4;      // select the pin for the LED
int sensorValue_B2 = 0;  // variable to store the value coming from the sensor

int flame_B = A2;     //센서 연결
int LED_B = 2;       //LED 연결

void setup()
{
  Wire.begin(2);
  Wire.onRequest(requestEvent);
  
  pinMode(flame_B, INPUT);
  pinMode(LED_B, OUTPUT);
  pinMode(LED_B1, OUTPUT);
  pinMode(LED_B2, OUTPUT);
  Serial.begin(9600); 
}

void loop()
{
// read the value from the ir sensor
  
  intSensorResult_B1 = analogRead(IR_SENSOR_B1); //Get sensor value
  fltSensorCalc_B1 = (6787.0 / (intSensorResult_B1 - 3.0)) - 4.0; //Calculate distance in cm
  
  Serial.print(fltSensorCalc_B1); //Send distance to computer
  Serial.println(" cm"); //Add cm to result
  if(fltSensorCalc_B1<10.5)
    {
      digitalWrite(LED_B1, HIGH);
    }
    else 
    {
      digitalWrite(LED_B1, LOW);
    }
      
 
  sensorValue_B2 = analogRead(sensorPin_B2);
  Serial.println(sensorValue_B2);
  delay(10);
  if(sensorValue_B2>800)
  {
    digitalWrite(LED_B2, HIGH);
  }
  else
  {
    digitalWrite(LED_B2, LOW);
  }

  int val = analogRead(flame_B);
  Serial.print("flame_sensor : ");
  Serial.println(val);
 
  if(val<1000) {     //값이 1022미만이면 LED 불이 켜집니다.
    digitalWrite(LED_B, HIGH);
  }
  else{
    digitalWrite(LED_B, LOW);
  }

  if(fltSensorCalc_B1<10.5) {
    if(sensorValue_B2>800){
      if(val<1000){
        Big = 'a';
      }
      else {
        Big = 'b';
      }
    }
    else {
      if(val<1000){
        Big = 'c';
      }
      else {
        Big = 'd';
      }
    }
  }
  else {
    if(sensorValue_B2>800) {
      if(val<1000){
        Big = 'e';
      }
      else {
        Big = 'f';
      }
    }
    else {
      if(val<1000) {
        Big = 'g';
      }
      else {
        Big = 'h';
      }
    }
  }

  Serial.println(Big);
  
  delay(200); //Wait
}

void requestEvent() {
  Wire.write(Big);
}
