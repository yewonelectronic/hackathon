#include <Wire.h>
#include <ESP8266WiFi.h>
 
const char* ssid     = "Galaxy Z Flip3 5G"; // 사용 중 인 와이파이 이름
const char* password = "98051253!!"; // 와이파이 패스워드
int SLAVE[3] = {1, 2, 3}; 
char c=' ';
int i=0;

WiFiServer server(80);
 
void setup() {
  Wire.begin();
  Serial.begin(115200); // 시리얼 통신, 속도 115200
  delay(10);
  Serial.println();
 
  // Connect to WiFi network
  WiFi.mode(WIFI_STA);
  Serial.println();
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);
 
  WiFi.begin(ssid, password);
 
  while (WiFi.status() != WL_CONNECTED) {
    delay(100);
    Serial.print(".");
  }
  
  Serial.println("");
  Serial.println("WiFi connected");
 
  // Start the server
  server.begin();
  Serial.println("Server started");
 
  // Print the IP address
  Serial.println(WiFi.localIP());
} 

void loop() {

  for(i=1;i<4;i++){
    Wire.beginTransmission(i);                
    Wire.write("test ");       
    Wire.write(i);             
    Wire.endTransmission();    
  } 
  delay(500);
  
  Wire.requestFrom(i, 4);   
  while (Wire.available()) {
      c = Wire.read(); 
      Serial.print(c); 
  }
  
  //val+=1;// cds 센서값 저장
  delay(50);
  Serial.println(c);
  WiFiClient client = server.available();
  client.println("HTTP/1.1 200 OK");
  client.println("Content-Type: text/html");
  client.println("Connection: close");
  client.println("Refresh: 3");  // 자동으로 웹페이지 새로고침 (1초 설정)
  client.println();
  client.println("<!DOCTYPE html>");
  client.println("<html xmlns='http://www.w3.org/1999/xhtml'>");
  client.println("<head>\n<meta http-equiv='Content-Type' content='text/html; charset=utf-8' />");
  //client.println("<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\" />");
  //client.println("<head>\n<meta charset='UTF-8'>");
  
  client.println("<title>DIYver tistory blog test</title>"); // 웹 서버 페이지 제목 설정
  client.println("</head>\n<body>");
  client.println("<center>");
  
  client.println("<H4>Sensor Value</H4>");
  client.println(c);
  
  client.println("<br>");
  client.println("<br>");
 
  client.println("<pre>");
  client.print("</body>\n</html>");

  delay(2000);
}
