import uvicorn 
import requests
from fastapi import FastAPI
from .models import EventoJogador, RespostaSucesso  # import do ares/models.py


app = FastAPI(title="API Ares - O Mensageiro da Batalha")
CRONOS_URL = "http://localhost:8002/registrar-evento"

@app.post("/enviar-acao", response_model=RespostaSucesso)
def enviar_acao(evento: EventoJogador):
    """
    Recebe a ação do jogador e envia para Cronos.
    """
    print(f"Ares recebeu uma ação de {evento.id_player}: {evento.tipo_acao}")

    try: 
        response = requests.post(CRONOS_URL, json=evento.dict())
        response.raise_for_status() # Lança um erro para status 4xx/5xx

        cronos_resposta = response.json 
        print(f"Cronos respondeu com sucesso. ID do Evento: {cronos_resposta.get('id_evento')}") 
        return RespostaSucesso(mensagem="Ação enviada para Cronos.", id_evento=cronos_resposta.get('id_evento'))
    
    except requests.exceptions.RequestException as e:
        print(f"500 - Erro ao conectar com Cronos: {e}")
        # Em um sistema real, você retornaria um erro 500
        # Ou faria uma fila de retentativas.
        return RespostaSucesso(mensagem="Falha ao enviar ação para Cronos.", id_evento="erro")
    
# Este bloco só será executado se o arquivo for o ponto de entrada
if __name__ == "__main__":
    uvicorn.run("ares.main:app", host="0.0.0.0", port=8001, reload=True)