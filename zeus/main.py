import uvicorn
import requests
from fastapi import FastAPI
from .models import ResultadoFinalAcao, EstadoAtualizado  # import do model/final - Zeus

app = FastAPI(title="API Zeus - A verdade absoluta")

##ZEUS_URL = "http://localhost:8004/estado-atual" ## Zeus nao vai precisar disto.
# ⚠️ AQUI ESTÁ O "BANCO DE DADOS" DO ZEUS. Por enquanto, uma variável na memória.
estado_do_jogo = {
    "player_A": {"vida": 100, "status": "normal"},
    "player_B": {"vida": 100, "status": "normal"},
}


@app.post("/estado-final", response_model=EstadoAtualizado)
def estado_final(resultado: ResultadoFinalAcao):
    """
    RECEBE o resultado do cálculo de Atena, atualiza o estado do jogo e RETORNA.
    """
    print(
        f"Zeus recebeu o resultado do evento {resultado.id_evento} com dano de {resultado.dano_aplicado}"
    )

    # ----------- AQUI COMEÇA A LÓGICA DE ATUALIZAÇÃO DO ZEUS -----------

    player_afetado_id = resultado.id_player_afetado
    dano = resultado.dano_aplicado

    # ⚠️ A LÓGICA DE ATUALIZAÇÃO DO ESTADO DO JOGO. O Zeus "baterá o martelo" aqui. ⚠️
    if player_afetado_id in estado_do_jogo:
        estado_do_jogo[player_afetado_id]["vida"] -= dano
        if estado_do_jogo[player_afetado_id]["vida"] <= 0:
            estado_do_jogo[player_afetado_id]["status"] = "derrotado"

    print(f"Estado do jogo atualizado: {estado_do_jogo}")

    # Agora, Zeus CRIA o MODELO DE SAÍDA
    resposta_final = EstadoAtualizado(
        status="sucesso", mensagem=resultado.mensagem_log, estado_jogo=estado_do_jogo
    )
    # ⚠️----------- FIM DA LÓGICA DE ATUALIZAÇÃO DO ZEUS ----------- ⚠️

    # Zeus retorna o modelo de SAÍDA para a Atena
    return resposta_final


if __name__ == "__main__":
    uvicorn.run("zeus.main:app", host="0.0.0.0", port=8004, reload=True)
