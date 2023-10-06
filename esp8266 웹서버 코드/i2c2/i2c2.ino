#include <Wire.h>

// 슬레이브 주소
int SLAVE[3] = {1, 2, 3}; 

void setup() {
  Wire.begin(2,1);
  Serial.begin(9600); 
}

void loop() {  
  Wire.beginTransmission(2);                
  Wire.write("test ");       
  Wire.write(2);             
  Wire.endTransmission();  

  delay(500);

  Wire.requestFrom(2, 3);   
  while (Wire.available()) {
      char c = Wire.read(); 
      Serial.print(c);        
  }
}
