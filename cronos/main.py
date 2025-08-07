import uvicorn
import requests
import uuid
from fastapi import FastAPI
from datetime import datetime
from .models import EventoJogador
from pydantic import BaseModel

app = FastAPI(title="API Cronos - O Guardião do Tempo")

# URL da Atena
ATENA_URL = "http://localhost:8003/analisar-evento"


# Modelo de resposta
class RespostaEvento(BaseModel):
    mensagem: str
    id_evento: str


@app.post("/registrar-evento", response_model=RespostaEvento)
def registrar_evento(evento: EventoJogador):
    """
    Recebe a ação do jogador, registra o timestamp e a envia para Atena.
    """
    id_evento = str(uuid.uuid4())  # Gera um ID único para o evento
    print(f"Cronos registrou o evento {id_evento} de {evento.id_player}.")

    # Payload para Atena (não envia tudo)
    payload_para_atena = {
        "id_evento": id_evento,
        "id_player": evento.id_player,
        "tipo_acao": evento.tipo_acao,
        "payload": evento.payload,
    }

    try:
        # Envia o evento para Atena
        response = requests.post(ATENA_URL, json=payload_para_atena)
        response.raise_for_status()

        # Resposta com o ID do evento para Ares
        return RespostaEvento(
            mensagem="Evento registrado com sucesso e enviado para Atena.",
            id_evento=id_evento,
        )

    except requests.exceptions.RequestException as e:
        print(f"Erro ao conectar com Atena: {e}")
        return RespostaEvento(
            mensagem="Falha ao enviar evento para Atena.", id_evento="erro"
        )


# Rodar servidor
if __name__ == "__main__":
    uvicorn.run("cronos.main:app", host="0.0.0.0", port=8002, reload=True)
