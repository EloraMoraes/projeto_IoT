# projeto_IoT
Este projeto utiliza um sensor de temperatura LM35 conectado a um Arduino UNO para medir a temperatura corporal e enviar os dados via protocolo MQTT para um broker. O sistema permite a monitorização remota da temperatura através de um servidor MQTT, ideal para aplicações de saúde e monitoramento em tempo real.

# IoT Temperature Monitor

Este projeto visa monitorar a temperatura corporal utilizando um sensor LM35, um Arduino UNO e comunicação via MQTT.

## Funcionalidades

- Medição da temperatura corporal utilizando um sensor LM35.
- Envio das leituras de temperatura para um broker MQTT.
- Comunicação em tempo real com uma plataforma MQTT.

## Estrutura do Repositório

- `src/`: Contém o código fonte do Arduino e o script Python para publicação MQTT.
- `hardware/`: Descrição e datasheets do hardware utilizado.
- `documentation/`: Documentação detalhada do projeto, incluindo descrição do hardware, interfaces e protocolos, e resultados de testes.

## Como Reproduzir

1. Clone este repositório:
    ```bash
    git clone https://github.com/EloraMoraes/projeto_IoT
    ```
2. Siga as instruções em `documentation/project_description.md` para configurar o hardware e software.
3. Carregue o código Arduino em `src/arduino_code/temperature_monitor.ino` no seu Arduino UNO.
4. Execute o script Python `src/python_code/mqtt_publisher.py` para publicar as leituras no broker MQTT.

## Licença

Este projeto é licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
