import requests 
import json
from tkinter import *




def clima(cidade):
        chave = '98aa04dae87ee9ff1135a71b64fc07f2'
        url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chave}&lang=pt_br&units=metric"
        call = requests.get(url)
        json_resposta = call.json()

        with open('tempo.json', 'w', encoding='utf-8') as f:
                json.dump(json_resposta, f, ensure_ascii=False, indent=4)

        #pegando dados
        descricao = json_resposta.get('weather', [{}])[0].get("description")
        sense_termina = json_resposta.get('main', {}).get("feels_like")
        max_temp =int( json_resposta.get('main', {}).get("temp_max"))
        min_temp =int( json_resposta.get('main', {}).get("temp_min"))
        humidade = int(json_resposta.get('main', {}).get("humidity"))
        temp =int( json_resposta.get('main', {}).get("temp"))
        #retorna os dados como dicionario
        return {
                "descricao": descricao,
                "sensacao_termica": sense_termina,
                "temp_max": max_temp,
                "temp_min": min_temp,
                "humidade": humidade,
                "temp": temp
        }
        


