// Define o pino do sensor
#define LM35 A0

void setup() {
  // Inicia a comunicação serial
  Serial.begin(9600);
}

void loop() {
  float soma = 0;
  for(int i = 0; i < 10; i++) {
    // Faz a leitura da temperatura 10 vezes
    soma += analogRead(LM35);
    delay(100);
  }
  // Calcula a média das leituras
  float media = soma / 10.0;
  // Converte a leitura para temperatura em Celsius
  float tempc = (media * 5.0 * 100.0) / 1024.0;
  if(tempc >= 20 && tempc <= 40) { // Verifica se a temperatura está entre 20 e 40 graus
    Serial.print("Temperatura: ");
    Serial.print(tempc);
    Serial.println(" C");
  }
  delay(1000); // Aguarda 1 segundo para nova leitura
}
