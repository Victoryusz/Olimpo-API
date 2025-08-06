import uvicorn
import requests
import uuid
from fastapi import FastAPI
from datetime import datetime
from .models import EventoJogador

app = FastAPI(title="API Cronos - O Guardião do Tempo")

# Atena's URL
ATENA_URL = "http://localhost:8003/analisar-evento"


@app.post("/registrar-evento")
def registrar_evento(evento: EventoJogador):
    """
    Recebe a ação do jogador, registra o timestamp e a envia para Atena.
    """
    # Aqui, em um cenário real, você salvaria o evento em um banco de dados.
    # para a nossa "linha do tempo".
    id_evento = str(uuid.uuid4())  # Gera um ID único para o evento
    print(f"Cronos registrou o evento {id_evento} de {evento.id_player}.")

    # Agora , encaminhamos para Atena
    try:
        # Criamos o payload para Atena. O Cronos não envia tudo.
        payload_para_atena = {
            "id_evento": id_evento,
            "id_player": evento.id_player,
            "tipo_acao": evento.tipo_acao,
            "payload": evento.payload,
        }

        # Requisição síncrona para Atena.
        response = requests.post(ATENA_URL, json=payload_para_atena)
        response.raise_for_status()

        # Retorna o ID do evento para Ares saber que foi registrado.
        return {"mensagem": "Evento registrado com sucesso e enviado para Atena."}
    except requests.exceptions.RequestException as e:
        print(f"Erro ao conectar com Atena: {e}")
        return {"mensagem": "Falha ao enviar evento para Atena.", "id_evento": "erro"}


# Bloco para rodar o servidor
if __name__ == "__main__":
    import uuid  # Importa aqui para usar no exemplo

    uvicorn.run("cronos.main:app", host="0.0.0.0", port=8002, reload=True)
