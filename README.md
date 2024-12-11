# Jogo do Sapinho

## Descrição
Este é um jogo simples onde o jogador aposta em um sapo tentando atravessar uma estrada. A cada rodada, o jogador faz uma aposta e o sapo tenta atravessar a estrada. Se o sapo for atropelado por um caminhão, o jogador perde o valor da aposta. Se o sapo atravessar com sucesso, o jogador ganha uma recompensa baseada em quantas vezes o sapo já cruzou a estrada. O jogador pode continuar apostando até que o saldo seja zerado ou escolher parar a qualquer momento.

## Padrões de Design Utilizados
- **Singleton Pattern**: Usado para garantir que o saldo do jogador seja gerenciado por uma única instância da classe `PlayerWallet`.
- **Factory Method Pattern**: Utilizado na criação de eventos de estrada (como "Truck" ou "Safe"), variando com base em uma probabilidade.
- **Strategy Pattern**: Define comportamentos do sapo (cruzar ou parar) como estratégias intercambiáveis.
- **Observer Pattern**: Usado para notificar a classe `GameObserver` sobre o progresso do jogo, como o número de travessias do sapo.
- **Decorator Pattern**: Aplica um multiplicador de recompensa ao valor ganho pelo jogador, baseado no número de travessias.

## Funcionalidade
- O jogador começa com um saldo inicial de R$1000.
- A cada rodada, o jogador escolhe quanto deseja apostar.
- Dependendo do evento da estrada (se o sapo atravessa com sucesso ou é atropelado), o saldo do jogador é ajustado.
- O jogador pode continuar apostando ou parar a qualquer momento. Se o saldo for zerado, ele tem a opção de depositar mais dinheiro ou parar de jogar.
- O jogo termina quando o saldo é zerado ou o jogador escolhe parar.

## Como Rodar o Jogo
Clone o repositório:

```bash
git clone https://github.com/seu-usuario/jogo-do-sapo.git
cd jogo-do-sapo
```

Execute o código: O jogo está implementado em Python. Para rodá-lo, basta executar o arquivo principal main.py:
```bash 
python main.py
```

## Interação do Jogo
- A cada rodada, o jogo perguntará ao jogador quanto deseja apostar.
- O jogador pode continuar apostando ou digitar "parar" para encerrar o jogo.

## Como Funciona
- **Criação de Eventos**: O jogo cria um evento de estrada aleatório a cada rodada. O evento pode ser um "Truck" (onde o sapo é atropelado e o jogador perde a aposta) ou "Safe" (onde o sapo atravessa com sucesso e o jogador ganha uma recompensa).

- **Recompensa Baseada nas Travessias**: Cada vez que o sapo atravessa com sucesso, o jogador recebe uma recompensa, que é multiplicada conforme o número de travessias.

- **Saldo do Jogador**: O saldo do jogador é atualizado a cada rodada com base no resultado da aposta. O jogo oferece a opção de depositar mais dinheiro caso o saldo seja zerado.

## Dependências
- Python 3.x
- Nenhuma biblioteca externa é necessária.

## Autores
- Júlio
- Luiz O.
- Rafael S.
