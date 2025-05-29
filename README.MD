Climas_do_Mundo
Descrição
Este é um app simples em Python que consulta a API do OpenWeather para mostrar o clima atual de qualquer cidade. A interface gráfica foi criada com Tkinter, permitindo que o usuário digite o nome da cidade e veja informações como temperatura, sensação térmica, umidade e descrição do clima.

Arquivos do projeto
main.py: faz a requisição à API do OpenWeather, salva a resposta no arquivo tempo.json e retorna um dicionário com os dados do clima que serão exibidos.

interface.py: cria a interface gráfica, recebe a cidade digitada pelo usuário, chama a função de busca do main.py e exibe as informações na tela.

tempo.json: arquivo JSON onde a resposta da API é salva localmente, contendo dados detalhados como coordenadas, temperatura, umidade, vento, entre outros.

Exemplo de conteúdo do tempo.json
O arquivo contém dados como:

Coordenadas geográficas (latitude e longitude)

Condições do tempo ("description": "céu limpo")

Temperatura atual, mínima, máxima e sensação térmica

Umidade, pressão, visibilidade e velocidade do vento

Informações de nascer e pôr do sol

Configuração e uso
Tenha o Python 3.8+ instalado.

Instale a biblioteca requests (Tkinter já vem com o Python):

pip install requests

O projeto usa a API do OpenWeather, que necessita de uma chave (API key). No arquivo main.py, substitua o valor da variável chave pela sua chave obtida em https://openweathermap.org/api.

Execute o programa com:

python interface.py

Na janela que abrir, digite o nome da cidade e clique em "Buscar clima" para ver as informações.

