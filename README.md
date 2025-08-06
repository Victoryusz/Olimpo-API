## OLIMPO-API ##
Um projeto de microserviços em Python (FastAPI) com temática de mitologia grega, projetado para simular o fluxo de uma ação em um sistema de jogo online. Cada API representa uma entidade com uma responsabilidade única, demonstrando uma arquitetura desacoplada e escalável.

**Arquitetura e Tecnologias**
Este projeto foi construído para explorar e aplicar conceitos de arquitetura de software, utilizando as seguintes tecnologias e boas práticas:

Python e FastAPI

Arquitetura de Microserviços: O sistema é composto por quatro APIs independentes que se comunicam entre si.
Contratos de API (Pydantic): Uso de modelos de dados robustos para validar e estruturar a comunicação entre os serviços.
Comunicação Síncrona entre APIs: Implementação de chamadas HTTP sequenciais para processar uma única ação do início ao fim.
Separação de Responsabilidades (SRP): Cada API possui uma função bem definida, o que facilita a manutenção e o desenvolvimento em equipe.

**Fluxo do Sistema**
O projeto simula a seguinte cadeia de eventos, partindo de uma ação do jogador:

API Ares: Recebe a entrada do jogador (ex: um ataque) e a encaminha para o próximo serviço.
API Cronos: Atua como o "guardião do tempo," registrando o evento e mantendo um histórico antes de passá-lo para a análise.
API Atena: Recebe o evento e aplica a lógica de negócio (cálculo de dano, validação de regras).
API Zeus: Atua como a "fonte da verdade," atualiza o estado final do jogo e retorna a resposta completa para o jogador.