#include <Wire.h>
// #include <Adafruit_ADS1X15.h>


// Adafruit_ADS1115 ads1115;
int datarate;
int myTime;
bool didLog;



  void AdcBooster()
  {
  ADC->CTRLA.bit.ENABLE = 0;                     // Disable ADC
  while( ADC->STATUS.bit.SYNCBUSY == 1 );        // Wait for synchronization
  ADC->CTRLB.reg = ADC_CTRLB_PRESCALER_DIV64 |   // Divide Clock by 64.
                   ADC_CTRLB_RESSEL_12BIT;       // Result on 12 bits
  ADC->AVGCTRL.reg = ADC_AVGCTRL_SAMPLENUM_1 |   // 1 sample
                     ADC_AVGCTRL_ADJRES(0x00ul); // Adjusting result by 0
  ADC->SAMPCTRL.reg = 0x00;                      // Sampling Time Length = 0
  ADC->CTRLA.bit.ENABLE = 1;                     // Enable ADC
  while( ADC->STATUS.bit.SYNCBUSY == 1 );        // Wait for synchronization
  } // AdcBooster

int temp_array[5];
void setup() {
  AdcBooster();
  // SerialUSB.begin(115200);
  Serial.begin(115200);
  // analogReadResolution(12);
  /*
  ads1115.setGain(GAIN_FOUR);
  ads1115.setDataRate(RATE_ADS1115_860SPS);
  datarate = 0;
  myTime = millis();
  didLog = false;
  ads1115.begin();
  // Serial.print(DIV);
  */
}

void loop() {
  // Serial.println(ads1115.getLastConversionResults());
  // for (int i = 0; i < 100; i++)
  // {
    // temp_array[i][0] = micros();
    // temp_array[i][0] = 0;
    //          temp_array[i][0] = analogRead(A0);
    //          temp_array[i][1] = analogRead(A1);
    //          temp_array[i][2] = analogRead(A2);
    //          temp_array[i][3] = analogRead(A3);
    // temp_array[0] = ads1115.readADC_SingleEnded(0);
    // temp_array[1] = ads1115.readADC_SingleEnded(1);
    // temp_array[2] = ads1115.readADC_SingleEnded(2);
    // temp_array[3] = ads1115.readADC_SingleEnded(3);
  // }
  // for (int i = 0; i < 100; i++)
  // {
    // for (int j = 0; j < 4; j++)
    // {
      // SerialUSB.print(temp_array[i][j]);SerialUSB.print(",");
      
    // }
    temp_array[0] = analogRead(A0);
    temp_array[1] = analogRead(A1);
    temp_array[2] = analogRead(A2);
    temp_array[3] = analogRead(A3);
    
    
    // SerialUSB.println(temp_array[0] >> 8);
    // SerialUSB.println(temp_array[0] >> 8);
    // SerialUSB.println(temp_array[0] >> 8);
    SerialUSB.write(temp_array[0] >> 8);
    SerialUSB.write(temp_array[0] & 0x00ff);
    SerialUSB.write(temp_array[1] >> 8);
    SerialUSB.write(temp_array[1] & 0x00ff);
    SerialUSB.write(temp_array[2] >> 8);
    SerialUSB.write(temp_array[2] & 0x00ff);
    SerialUSB.write(temp_array[3] >> 8);
    SerialUSB.write(temp_array[3] & 0x00ff);
    // SerialUSB.println();
    SerialUSB.write((byte)0x00);
    // Serial.flush();
    // datarate++;
    
    // if ((int)millis() - myTime >= 10000 && !didLog)
    // {
      // didLog = true;
      // Serial.println(datarate);
    // }
      // else if (!didLog)Serial.println((int)millis() - myTime);
  // }
}
