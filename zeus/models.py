# zeus/models.py
from pydantic import BaseModel


class EstadoAtualizado(BaseModel):
    status: str
    mensagem: str
    estado_jogo: dict

class ResultadoFinalAcao(BaseModel):
    id_evento: str
    id_player_afetado: str
    dano_aplicado: int
    mensagem_log: str