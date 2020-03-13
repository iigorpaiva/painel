#define A A0
#define FAROIS 9

int volts = 0;
String cod;

void setup() {
  Serial.begin(9600);
  pinMode(A, INPUT);
  pinMode(FAROIS, OUTPUT);

}

void loop() {
  
// -------------------------- ESCRITA PARA O PYTHON ---------------------------

  volts = analogRead(A);
    //Serial.println(volts);

  if(Serial.availableForWrite()){
    
    if(volts < 300)
      Serial.print("D");

    else if(volts >= 600)
      Serial.print("L");

    else
      Serial.print("F");
  }
// ------------------------- LEITURA DO PYTHON --------------------------------------------------

  if(Serial.available()){
    char aux = Serial.read();
    cod += aux;
  }

  if(cod == "ligar farois")
    digitalWrite(FAROIS, HIGH);
    cod = "";

  if(cod == "desligar farois")
    digitalWrite(FAROIS, LOW);
    cod = "";

  
  Serial.flush();
}
