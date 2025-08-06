# Reutilizando os mesmos modelos da comunicação entre APIs
from pydantic import BaseModel
from datetime import datetime

class EventoJogador(BaseModel):
    id_player: str
    tipo_acao: str
    timestamp: datetime
    payload: dict