# zeus/models.py
from pydantic import BaseModel


class EstadoAtualizado(BaseModel):
    status: str
    mensagem: str
    estado_jogo: dict
