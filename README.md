# 🤖 Vision-Arduino-Control: Controle de Hardware por Gestos em Tempo Real

Este projeto demonstra a integração prática entre visão computacional (software) e eletrônica (hardware). Utilizando uma câmera comum, o sistema detecta as articulações da mão do usuário em tempo real, interpreta os gestos e envia comandos via comunicação serial para ligar ou desligar um LED em uma placa Arduino.

💡 **Destaque:** Desenvolvido de ponta a ponta de forma autônoma em apenas dois dias como um desafio pessoal de portfólio.

---

## 🚀 Como Funciona a Lógica

1. **Captura e Conversão:** O script em Python captura o vídeo da webcam através do `OpenCV` e converte os frames para o espaço de cores RGB.
2. **Processamento e Mapeamento:** O framework `MediaPipe` processa a imagem e extrai as coordenadas estruturais (landmarks) da mão detectada.
3. **Análise de Gestos:** O algoritmo analisa as posições dos eixos verticais (`y`) das pontas dos dedos em relação às suas respectivas bases para determinar quantos dedos estão levantados.
4. **Decisão e Comunicação:** Se forem detectados **3 ou mais dedos levantados**, o Python envia o byte `b'1'` via porta Serial (PySerial) para o Arduino e exibe "LED LIGADO" na tela. Caso contrário, envia `b'0'` e exibe "LED DESLIGADO".
5. **Ação Física:** O microcontrolador Arduino processa o caractere recebido no buffer serial e altera o estado elétrico do pino analógico, ativando ou desativando o componente físico (LED).

---

## 🔧 Tecnologias e Bibliotecas Utilizadas

- **Python 3** (Lógica principal de controle)
- **OpenCV** (Captura, manipulação de frames de vídeo e interface gráfica)
- **MediaPipe** (Solução de Machine Learning de alta fidelidade para rastreio e detecção de mãos)
- **PySerial** (Protocolo de comunicação serial entre PC e Arduino)
- **C++ / Linguagem Arduino** (Programação do microcontrolador)

---

## 📁 Estrutura do Repositório

- `mao_led.py`: Script principal que unifica a visão computacional e o envio de comandos serial.
- `control_led.ino`: Código C++ carregado na placa Arduino para ler a porta serial.
- `requirements.txt`: Lista de dependências e versões exatas para replicação do ambiente.
- `teste_camera.py` & `teste_mao.py`: Scripts de validação inicial do hardware de vídeo e mapeamento de landmarks.
- `controle_led.py`: Script de teste de comunicação para validação dos comandos via terminal numérico.

---

## 🛠️ Como Executar o Projeto

### 1. Configuração do Hardware
1. Conecte a sua placa Arduino ao computador via USB.
2. Certifique-se de que o pino do LED (ou o pino padrão 13) está configurado corretamente.
3. Abra a Arduino IDE, carregue o código contido no arquivo `control_led.ino` para a placa e verifique em qual porta COM o seu dispositivo foi alocado (ex: `COM3`).

### 2. Configuração do Software
1. Clone este repositório para a sua máquina local:
   ```bash
   git clone [https://github.com/Thamy00Vic/Vision-Arduino-Control.git](https://github.com/Thamy00Vic/Vision-Arduino-Control.git)
