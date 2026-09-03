# AlexaBot

Assistente virtual controlado por voz, desenvolvido em Python, com reconhecimento de fala, síntese de voz, inteligência artificial local, reconhecimento facial e integração com serviços externos.

O projeto foi desenvolvido como um assistente pessoal inspirado em assistentes virtuais como a Alexa, sendo capaz de interpretar comandos em linguagem natural e executar ações específicas.

---

## 📋 Sumário

* [Sobre o projeto](#-sobre-o-projeto)
* [Funcionalidades](#-funcionalidades)
* [Tecnologias utilizadas](#-tecnologias-utilizadas)
* [Estrutura do projeto](#-estrutura-do-projeto)
* [Pré-requisitos](#-pré-requisitos)
* [Instalação](#-instalação)
* [Configuração do ambiente virtual](#-configuração-do-ambiente-virtual)
* [Instalação das dependências](#-instalação-das-dependências)
* [Configuração do reconhecimento facial](#-configuração-do-reconhecimento-facial)
* [Treinamento do reconhecimento facial](#-treinamento-do-reconhecimento-facial)
* [Execução](#-execução)
* [Comandos disponíveis](#-comandos-disponíveis)
* [Como funciona o processamento](#-como-funciona-o-processamento)
* [Módulos do sistema](#-módulos-do-sistema)
* [YouTube](#-youtube)
* [Previsão do tempo](#-previsão-do-tempo)
* [Agenda](#-agenda)
* [Reconhecimento facial](#-reconhecimento-facial)
* [Data e hora](#-data-e-hora)
* [Inteligência artificial](#-inteligência-artificial)
* [Solução de problemas](#-solução-de-problemas)
* [Possíveis melhorias](#-possíveis-melhorias)

---

# 🤖 Sobre o projeto

O **AlexaBot** é um assistente virtual desenvolvido em Python com interação predominantemente por voz.

O sistema utiliza uma palavra de ativação, como **"Alexa"**, para identificar quando o usuário deseja enviar um comando.

Após detectar a palavra de ativação, o sistema interpreta o restante da frase e verifica se ela corresponde a alguma funcionalidade específica.

Quando o comando corresponde a uma funcionalidade programada, o módulo responsável executa a ação.

Caso o comando não corresponda a uma funcionalidade específica, a solicitação pode ser encaminhada para um modelo de inteligência artificial executado localmente através do **Ollama**.

A arquitetura foi organizada em módulos independentes para facilitar a manutenção e a expansão do projeto.

---

# ✨ Funcionalidades

Atualmente, o AlexaBot possui suporte para:

* 🎤 Reconhecimento de voz
* 🔊 Resposta por voz
* 🧠 Integração com inteligência artificial através do Ollama
* 👤 Reconhecimento facial
* 📅 Cadastro de eventos na agenda
* 📖 Consulta da agenda
* 🗑️ Limpeza da agenda
* ▶️ Pesquisa e reprodução de vídeos no YouTube
* 🌤️ Consulta da previsão do tempo
* 🕐 Consulta da hora atual
* 📆 Consulta da data atual
* 🚪 Comando para encerrar a conversa
* 🔎 Interpretação de comandos em linguagem natural

---

# 🛠️ Tecnologias utilizadas

## Linguagem

* Python 3.11

## Inteligência artificial

* Ollama

## Reconhecimento facial

* OpenCV
* OpenCV Contrib
* EigenFace
* Haar Cascade

## Áudio

* Biblioteca de reconhecimento de fala utilizada pelo projeto
* Pygame para reprodução de áudio

## Navegação automatizada

* Playwright
* Chromium

## APIs externas

* Open-Meteo para previsão do tempo
* Geocoding API do Open-Meteo para localização de cidades

## Outras bibliotecas

* Requests
* NumPy

---

# 📁 Estrutura do projeto

A estrutura atual do projeto é organizada da seguinte maneira:

```text
AlexaBot/
│
├── bot/
│   │
│   ├── main.py
│   │
│   ├── ai/
│   │   └── ollama.py
│   │
│   ├── audio/
│   │   ├── microphone.py
│   │   └── speaker.py
│   │
│   ├── commands/
│   │   └── detector.py
│   │
│   ├── agenda/
│   │   ├── manager.py
│   │   └── data/
│   │       └── agenda.txt
│   │
│   ├── face/
│   │   └── recognizer.py
│   │
│   ├── weather/
│   │   └── weather.py
│   │
│   ├── youtube/
│   │   └── youtube.py
│   │
│   └── utils/
│       └── haarcascade_frontalface_default.xml
│
├── models/
│   └── classificadoreigen.yml
│
├── capturas.py
│
├── treinamento.py
│
└── .venv/
```

### Principais arquivos

| Arquivo                         | Responsabilidade                           |
| ------------------------------- | ------------------------------------------ |
| `bot/main.py`                   | Controla o fluxo principal do assistente   |
| `bot/commands/detector.py`      | Identifica e classifica comandos           |
| `bot/audio/microphone.py`       | Captura áudio do microfone                 |
| `bot/audio/speaker.py`          | Reproduz as respostas da Alexa             |
| `bot/ai/ollama.py`              | Comunicação com o modelo de IA             |
| `bot/agenda/manager.py`         | Gerenciamento da agenda                    |
| `bot/face/recognizer.py`        | Reconhecimento facial                      |
| `bot/weather/weather.py`        | Consulta do clima                          |
| `bot/youtube/youtube.py`        | Pesquisa e abertura de vídeos              |
| `capturas.py`                   | Captura imagens para reconhecimento facial |
| `treinamento.py`                | Treina o modelo facial                     |
| `models/classificadoreigen.yml` | Modelo treinado de reconhecimento facial   |

---

# 💻 Pré-requisitos

Antes de executar o projeto, é necessário ter instalado:

* Python 3.11
* Ollama
* Webcam (Apenas para reconhecimento facial)
* Microfone (Opcional)
* Conexão com a internet para recursos que utilizam APIs externas e YouTube

---

# 📥 Instalação

Clone o projeto ou copie seus arquivos para uma pasta local.

Exemplo:

```powershell
git clone <URL_DO_REPOSITORIO>
cd AlexaBot
```

Caso o projeto já esteja no computador:

```powershell
cd C:\Users\labsfiap\Desktop\AlexaBot
```

---

# 🐍 Configuração do ambiente virtual

É recomendado utilizar um ambiente virtual para evitar conflitos entre bibliotecas.

Dentro da pasta do projeto:

```powershell
python -m venv .venv
```

Ative o ambiente virtual:

```powershell
.\.venv\Scripts\Activate.ps1
```

Se a ativação funcionar, o terminal deverá mostrar algo semelhante a:

```text
(.venv) PS C:\Users\labsfiap\Desktop\AlexaBot>
```

---

# 📦 Instalação das dependências

Com o ambiente virtual ativado:

```powershell
python -m pip install --upgrade pip
```

Instale as principais dependências:

```powershell
python -m pip install -r requirements.txt
```

> É importante utilizar `opencv-contrib-python` porque o projeto utiliza `cv2.face`, necessário para o reconhecimento facial com EigenFace.

---

# 🧠 Configuração do Ollama

O AlexaBot utiliza o Ollama para executar o modelo de inteligência artificial localmente.

Após instalar o Ollama, é necessário ter um modelo disponível.

Exemplo:

```powershell
ollama pull llama3
```

Verifique se o modelo está disponível:

```powershell
ollama list
```

O serviço do Ollama deve estar funcionando antes de executar o AlexaBot.

Teste:

```powershell
ollama run llama3
```

Caso o projeto utilize outro modelo, o nome configurado em `bot/ai/ollama.py` deve corresponder ao modelo instalado.

---

# 👤 Configuração do reconhecimento facial

O reconhecimento facial utiliza:

* OpenCV
* Haar Cascade para detectar rostos
* EigenFace para reconhecer a pessoa

O projeto foi configurado para reconhecer especificamente o indivíduo **Pedro**.

A identificação utilizada pelo modelo é:

```text
1 = Pedro
0 = Desconhecido
```

---

# 📸 Captura de imagens

O arquivo `capturas.py` pode ser utilizado para capturar imagens através da webcam.

Execute:

```powershell
python capturas.py
```

A webcam será aberta.

O sistema foi configurado para:

* manter a câmera aberta;
* pressionar **T** para realizar uma captura;
* pressionar **Q** para sair.

As imagens capturadas são utilizadas posteriormente no treinamento.

---

# 🧪 Treinamento do reconhecimento facial

Depois de colocar as imagens nas pastas especificadas, execute:

execute:

```powershell
python treinamento.py
```

O treinamento utiliza o algoritmo:

```text
EigenFaceRecognizer
```

O modelo gerado será salvo em:

```text
models/classificadoreigen.yml
```

Esse arquivo é carregado pelo sistema durante o reconhecimento facial.

Sempre que novas imagens forem adicionadas, é recomendado executar novamente:

```powershell
python treinamento.py
```

---

# ▶️ Execução

Com todas as configurações concluídas:

```powershell
python bot\main.py
```

Ou:

```powershell
python -m bot.main
```

O segundo formato é recomendado quando o projeto está estruturado como pacote Python.

Ao iniciar, o sistema carrega os módulos necessários e começa a aguardar comandos.

---

# 🗣️ Comandos disponíveis

## Palavra de ativação

O sistema reconhece:

```text
Alexa
Alexia
Alex
```

Exemplo:

```text
Alexa, que horas são?
```

A palavra de ativação é removida antes do processamento do comando.

---

## 🕐 Hora

Exemplos:

```text
Alexa, que horas são?
Alexa, qual a hora?
Alexa, me diga as horas.
```

A hora é obtida diretamente do relógio do computador através do Python.

---

## 📆 Data

Exemplos:

```text
Alexa, que dia é hoje?
Alexa, qual a data de hoje?
Alexa, me diga a data.
```

A data atual também é obtida diretamente do sistema operacional.

---

## 🌤️ Previsão do tempo

Exemplos:

```text
Alexa, qual a previsão do tempo para São Paulo?
```

Ou:

```text
Alexa, previsão do tempo para Rio de Janeiro.
```

O sistema:

1. identifica a cidade;
2. consulta o serviço de geocodificação;
3. obtém latitude e longitude;
4. consulta a previsão;
5. transforma os dados em uma resposta falada.

A implementação utiliza a API do Open-Meteo.

---

## ▶️ YouTube

Exemplo:

```text
Alexa, abra YouTube e rode um vídeo sobre Bitcoin.
```

O sistema:

1. identifica o comando;
2. extrai o assunto;
3. abre o YouTube;
4. pesquisa o assunto;
5. identifica o primeiro resultado;
6. abre o vídeo.

A automação é realizada através do Playwright.

---

## 📅 Agenda

Para adicionar um evento:

```text
Alexa, cadastrar evento na agenda.
```

Para consultar:

```text
Alexa, ler agenda.
```

Para apagar:

```text
Alexa, limpar agenda.
```

Os eventos são armazenados em:

```text
bot/agenda/data/agenda.txt
```

---

## 👤 Reconhecimento facial

Exemplo:

```text
Alexa, quem sou eu?
```

Ou:

```text
Alexa, reconheça meu rosto.
```

O sistema ativa a webcam e utiliza o modelo treinado para determinar se a pessoa é Pedro ou desconhecida.

---

## 🚪 Encerrar conversa

Exemplos:

```text
Alexa, sair.
Alexa, tchau.
Alexa, encerrar conversa.
```

Esses comandos encerram o loop principal do assistente.

---

# ⚙️ Como funciona o processamento

O fluxo principal do AlexaBot pode ser representado da seguinte maneira:

```text
             ┌───────────────┐
             │   Microfone   │
             └───────┬───────┘
                     │
                     ▼
             ┌───────────────┐
             │ Reconhecimento│
             │    de voz     │
             └───────┬───────┘
                     │
                     ▼
             ┌───────────────┐
             │CommandDetector│
             └───────┬───────┘
                     │
            ┌────────┴─────────┐
            │                  │
            ▼                  ▼
      Comando específico    Ollama
            │                  │
      ┌─────┼─────┬────┐      │
      │     │     │    │      │
      ▼     ▼     ▼    ▼      ▼
    Clima  Agenda Face YouTube IA
      │     │     │    │      │
      └─────┴─────┴────┴──────┘
                    │
                    ▼
             ┌───────────────┐
             │    Resposta   │
             └───────┬───────┘
                     │
                     ▼
             ┌───────────────┐
             │    Speaker    │
             └───────────────┘
```

A prioridade é dada aos comandos específicos.

Por exemplo, quando o usuário fala:

```text
Alexa, qual a previsão do tempo para São Paulo?
```

o sistema não envia imediatamente a frase para o Ollama.

Primeiro o `CommandDetector` verifica se a frase corresponde a um comando de clima.

Se corresponder, o módulo `weather.py` é executado.

Isso torna o comportamento mais previsível e evita que a IA tente executar tarefas que possuem uma implementação específica.

---

# 🧩 Módulos do sistema

## `main.py`

É o ponto central da aplicação.

Responsável por:

* inicializar os serviços;
* capturar comandos;
* verificar a palavra de ativação;
* direcionar comandos;
* executar respostas;
* controlar o loop principal.

---

## `detector.py`

Contém a classe:

```python
CommandDetector
```

É responsável por identificar comandos conhecidos.

Entre as categorias existentes estão:

```text
Wake Word
Agenda
Reconhecimento facial
YouTube
Previsão do tempo
Data
Hora
Saída
```

Isso mantém a lógica de identificação separada do restante do sistema.

---

# 🎤 Áudio

O módulo:

```text
bot/audio/microphone.py
```

é responsável pela captura do áudio.

O módulo:

```text
bot/audio/speaker.py
```

é responsável pela reprodução das respostas.

A separação permite substituir posteriormente a tecnologia de reconhecimento ou síntese de voz sem precisar alterar toda a aplicação.

---

# 🧠 Inteligência artificial

O módulo:

```text
bot/ai/ollama.py
```

é responsável pela comunicação com o Ollama.

A IA funciona como uma camada de conversação geral.

Por exemplo, perguntas que não correspondem a comandos específicos podem ser encaminhadas para o modelo.

Isso cria uma divisão entre:

```text
Comandos determinísticos
        +
Conversação com IA
```

---

# 📺 YouTube

O módulo:

```text
bot/youtube/youtube.py
```

utiliza Playwright para controlar o navegador Chromium.

O processo é:

```text
Comando
   ↓
Extrai o tema
   ↓
Abre YouTube
   ↓
Preenche pesquisa
   ↓
Pressiona Enter
   ↓
Aguarda resultados
   ↓
Seleciona primeiro vídeo
   ↓
Abre vídeo
```

O Playwright foi utilizado em vez de simplesmente abrir uma URL de pesquisa porque o objetivo é permitir que o AlexaBot interaja diretamente com os resultados da página.

---

# 🌤️ Previsão do tempo

O módulo:

```text
bot/weather/weather.py
```

utiliza o Open-Meteo.

O sistema primeiro converte o nome da cidade em coordenadas geográficas e depois utiliza essas coordenadas para obter a previsão.

A resposta final é transformada em linguagem natural para ser reproduzida pelo sistema de voz.

---

# 📅 Agenda

O módulo:

```text
bot/agenda/manager.py
```

controla os eventos.

Atualmente os dados são armazenados em um arquivo:

```text
bot/agenda/data/agenda.txt
```

Essa implementação é simples e adequada para o protótipo.

Uma futura evolução poderia utilizar SQLite ou outro banco de dados.

---

# 👤 Reconhecimento facial

O reconhecimento facial possui duas etapas:

### 1. Detecção

O Haar Cascade:

```text
bot/utils/haarcascade_frontalface_default.xml
```

identifica regiões da imagem que provavelmente contêm rostos.

### 2. Reconhecimento

O EigenFace compara o rosto detectado com os rostos utilizados durante o treinamento.

O modelo:

```text
models/classificadoreigen.yml
```

é carregado pelo `recognizer.py`.

O projeto utiliza:

```text
ID 1 → Pedro
ID 0 → Desconhecido
```

Existe um limiar de distância utilizado para determinar se o resultado é confiável.

---

# 🕐 Data e hora

A consulta de data e hora não depende de API externa.

O Python utiliza:

```python
datetime.now()
```

para obter a data e hora do computador.

Exemplo:

```python
from datetime import datetime

agora = datetime.now()

hora = agora.strftime("%H:%M")
data = agora.strftime("%d/%m/%Y")
```

Isso permite que comandos como:

```text
Alexa, que horas são?
```

sejam respondidos imediatamente.

---

# 📄 Licença

Projeto desenvolvido para fins acadêmicos e experimentais.

Caso o projeto seja publicado, recomenda-se adicionar uma licença específica, como MIT, conforme a necessidade do projeto.
