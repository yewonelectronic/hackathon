// 적외선 거리센서 A1 + led 파랑
// 감지 센서 A2 + led 파랑
// 불꽃센서 A + led 빨강
#include <Wire.h>
#define SLAVE 1

char Aig = ' ';

int IR_SENSOR_A1 = 0; // Sensor is connected to the analog A0
int intSensorResult_A1 = 0; //Sensor result
float fltSensorCalc_A1 = 0; //Calculated value
int LED_A1 = 3;

int sensorPin_A2 = A1;    // select the input pin for the potentiometer
int LED_A2 = 4;      // select the pin for the LED
int sensorValue_A2 = 0;  // variable to store the value coming from the sensor

void setup()
{
  Wire.begin(1);
  Wire.onRequest(requestEvent);
  
  pinMode(LED_A1, OUTPUT);
  pinMode(LED_A2, OUTPUT);
  Serial.begin(9600); 
}

void loop()
{
// read the value from the ir sensor
  
  intSensorResult_A1 = analogRead(IR_SENSOR_A1); //Get sensor value
  fltSensorCalc_A1 = (6787.0 / (intSensorResult_A1 - 3.0)) - 4.0; //Calculate distance in cm
  
  Serial.print(fltSensorCalc_A1); //Send distance to computer
  Serial.println(" cm"); //Add cm to result
  if(fltSensorCalc_A1<10.5)
    {
      digitalWrite(LED_A1, HIGH);
    }
    else
    {
      digitalWrite(LED_A1, LOW);
    }

      
  sensorValue_A2 = analogRead(sensorPin_A2);
    Serial.println(sensorValue_A2);
    delay(10);
    if(sensorValue_A2>800)
    {
      digitalWrite(LED_A2, HIGH);
    }
    else
      digitalWrite(LED_A2, LOW);

  if(fltSensorCalc_A1<10.5) {
    if(sensorValue_A2>800){
      Aig = 'E';
    }
    else{
      Aig = 'F';
    }
  }
  else {
    if(sensorValue_A2>800) {
      Aig = 'G';
    }
    else {
      Aig = 'H';
    }
  }
  
  delay(200); //Wait
}

void requestEvent() {
  Wire.write(Aig);
}
