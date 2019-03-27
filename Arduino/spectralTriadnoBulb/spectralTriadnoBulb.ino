// Code works in Arduino and on Teensy (first I2C=19,20)
#include "SparkFun_AS7265X.h" //Get the Library with the Librarymanager !
AS7265X sensor;

#include <Wire.h>

void setup() {
  Serial.begin(115200);

  if(sensor.begin() == false)
  {
    Serial.println("Sensor does not appear to be connected. Please check wiring. Freezing...");
    while(1);
  }

  sensor.disableIndicator(); //Turn off the blue status LED
  //put some triple ductttape over the red diode, or use a bit of play dough to cover it !!!

}

void loop() {
  //sensor.takeMeasurementsWithBulb();
  
  Serial.print(sensor.getCalibratedA());
  Serial.print(",");
  Serial.print(sensor.getCalibratedB());
  Serial.print(",");
  Serial.print(sensor.getCalibratedC());
  Serial.print(",");
  Serial.print(sensor.getCalibratedD());
  Serial.print(",");
  Serial.print(sensor.getCalibratedE());
  Serial.print(",");
  Serial.print(sensor.getCalibratedF());
  Serial.print(",");

  Serial.print(sensor.getCalibratedG());
  Serial.print(",");
  Serial.print(sensor.getCalibratedH());
  Serial.print(",");
  Serial.print(sensor.getCalibratedI());
  Serial.print(",");
  Serial.print(sensor.getCalibratedJ());
  Serial.print(",");
  Serial.print(sensor.getCalibratedK());
  Serial.print(",");
  Serial.print(sensor.getCalibratedL());
  Serial.print(",");

  Serial.print(sensor.getCalibratedR());
  Serial.print(",");
  Serial.print(sensor.getCalibratedS());
  Serial.print(",");
  Serial.print(sensor.getCalibratedT());
  Serial.print(",");
  Serial.print(sensor.getCalibratedU());
  Serial.print(",");
  Serial.print(sensor.getCalibratedV());
  Serial.print(",");
  Serial.print(sensor.getCalibratedW());

  Serial.println();
}
