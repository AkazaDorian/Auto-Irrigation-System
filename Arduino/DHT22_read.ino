#include <DHT.h>

#define DATA_SIZE 16
#define VERI_SIZE 8
#define uint unsigned int

#define SENSOR_PIN 7
#define SENSOR_TYPE DHT22

DHT dht(SENSOR_PIN, SENSOR_TYPE);

int verify;
float hum;
float temp;

void setup()
{
    Serial.begin(9600);
    dht.begin();
}

void loop()
{ 
    delay(100);
    if(Serial.available())
    {
        char key = Serial.read();
        if(key == 'h')
            Serial.println(dht.readHumidity());
        else if(key == 't')
            Serial.println(dht.readTemperature());
    }
}
