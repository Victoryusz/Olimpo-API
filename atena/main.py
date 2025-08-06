import uvicorn
import requests
from fastapi import FastAPI
from .models import (
    EventoParaAnalise,
    ResultadoFinalAcao,
)  # ⚠️ IMPORTANTE: AQUI IMPORTAMOS O QUE ATENA RECEBE E O QUE ELA ENVIA

app = FastAPI(title="API Atena - A Estrategista")
ZEUS_URL = "http://localhost:8004/estado-final"  # ⚠️ A URL DO ZEUS É PARA O ENDPOINT /estado-final


@app.post("/analisar-evento", response_model=ResultadoFinalAcao)
def analisar_evento(evento: EventoParaAnalise):
    print(f"Atena recebeu o evento {evento.id_evento} de {evento.id_player}")

    # ----------- AQUI COMEÇA A LÓGICA DE CÁLCULO DA ATENA -----------
    dano_calculado = 0

    # Exemplo de lógica de cálculo mais "complexa"
    if evento.payload.get("poder") == "ataque_forte":

        dano_calculado = 50
    else:
        dano_calculado = 20

    mensagem_para_zeus = f"{evento.id_player} usou {evento.payload.get('poder')} e causou {dano_calculado} de dano em {evento.payload.get('alvo')}"

    # Agora, Atena CRIA o MODELO DE SAÍDA (o resultado do cálculo)
    resultado = ResultadoFinalAcao(
        id_evento=evento.id_evento,
        id_player_afetado=evento.payload.get("alvo"),
        dano_aplicado=dano_calculado,
        mensagem_log=mensagem_para_zeus,
    )
    # ----------- FIM DA LÓGICA DE CÁLCULO DA ATENA -----------

    # Enviando o RESULTADO DO CÁLCULO para Zeus
    try:
        # AQUI, Atena envia o modelo que ela acabou de CRIAR para Zeus.
        response = requests.post(ZEUS_URL, json=resultado.dict())
        response.raise_for_status()

        # A Atena retorna o modelo de saída para Cronos
        return resultado
    except requests.exceptions.RequestException as e:
        print("Erro ao conectar com Zeus: {e}")
        # Retorno de erro
        return ResultadoFinalAcao(
            id_evento=evento.id_evento,
            id_player_afetado="N/A",
            dano_aplicado=0,
            mensagem_log=f"Erro ao enviar para Zeus: {e}",
        )


if __name__ == "__main__":
    uvicorn.run("atena.main:app", host="0.0.0.0", port=8003, reload=True)
