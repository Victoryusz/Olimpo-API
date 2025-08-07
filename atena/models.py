from pydantic import BaseModel
from datetime import datetime


# ⚠️ ESTE É O MODELO DE ENTRADA QUE ATENA RECEBE DO CRONOS
class EventoParaAnalise(BaseModel):
    id_evento: str
    id_player: str
    tipo_acao: str
    payload: dict


# ⚠️ ESTE É O MODELO DE SAÍDA QUE ATENA CRIA E ENVIA PARA ZEUS
class ResultadoFinalAcao(BaseModel):
    id_evento: str
    id_player_afetado: str
    dano_aplicado: int
    mensagem_log: str
