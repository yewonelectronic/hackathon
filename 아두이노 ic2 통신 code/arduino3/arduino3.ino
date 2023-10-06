// 적외선 거리센서 C1 + led 파랑
// 감지 센서 C2 + led 파랑
// 불꽃센서 C + led 빨강
#include <Wire.h>
#define SLAVE 3

char Cig = ' ';

int IR_SENSOR_C1 = 0; // Sensor is connected to the analog A0
int intSensorResult_C1 = 0; //Sensor result
float fltSensorCalc_C1 = 0; //Calculated value
int LED_C1 = 3;

int sensorPin_C2 = A1;    // select the input pin for the potentiometer
int LED_C2 = 4;      // select the pin for the LED
int sensorValue_C2 = 0;  // variable to store the value coming from the sensor

void setup()
{
  Wire.begin(3);
  Wire.onRequest(requestEvent);
  
  pinMode(LED_C1, OUTPUT);
  pinMode(LED_C2, OUTPUT);
  Serial.begin(9600); 
}

void loop()
{
// read the value from the ir sensor
  
  intSensorResult_C1 = analogRead(IR_SENSOR_C1); //Get sensor value
  fltSensorCalc_C1 = (6787.0 / (intSensorResult_C1 - 3.0)) - 4.0; //Calculate distance in cm
  
  Serial.print(fltSensorCalc_C1); //Send distance to computer
  Serial.println(" cm"); //Add cm to result
  if(fltSensorCalc_C1<10.5)
    {
      digitalWrite(LED_C1, HIGH);
    }
    else
    {
      digitalWrite(LED_C1, LOW);
    }

      
  sensorValue_C2 = analogRead(sensorPin_C2);
    Serial.println(sensorValue_C2);
    delay(10);
    if(sensorValue_C2>800)
    {
      digitalWrite(LED_C2, HIGH);
    }
    else
      digitalWrite(LED_C2, LOW);

  if(fltSensorCalc_C1<10.5) {
    if(sensorValue_C2>800){
      Cig = 'A';
    }
    else{
      Cig = 'B';
    }
  }
  else {
    if(sensorValue_C2>800) {
      Cig = 'C';
    }
    else {
      Cig = 'D';
    }
  }

  Serial.println(Cig);
  delay(200); //Wait
}

void requestEvent() {
  Wire.write(Cig);
}
