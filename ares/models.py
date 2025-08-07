# Contrato Ares -> Cronos
from pydantic import BaseModel, ValidationError
from datetime import datetime


class EventoJogador(BaseModel):
    id_player: str
    tipo_acao: str
    timestamp: datetime
    payload: dict  ##dicionario genérico


# Resposta (Output)
class RespostaSucesso(BaseModel):
    mensagem: str
    id_evento: str
