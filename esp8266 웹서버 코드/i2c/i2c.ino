#include <Wire.h>

// 슬레이브 주소
int SLAVE[3] = {1, 2, 3}; 

void setup() {
  Wire.begin(2,1); //SDA = D2(i2c -> data), SCL = D1(i2c -> clock)
  Serial.begin(9600); 
}

void loop() {  
  for(int i=1;i<4;i++){
    Wire.beginTransmission(i);                
    Wire.write("test ");       
    Wire.write(i);             
    Wire.endTransmission();    
     
    delay(500);
    
    Wire.requestFrom(i, 4);   
    while (Wire.available()) {
        char c = Wire.read(); 
        Serial.print(c);        
    }
  }    
}
