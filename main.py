import random

def display_sapo():
    print("""
                             .-----.
                            /7  .  (
                           /   .-.  \\
                          /   /   \\  \\
                         / `  )   (   )
                        / `   )   ).  \\
                      .'  _.   \\_/  . |
     .--.           .' _.' )`.        |
    (    `---...._.'   `---.'_)    ..  \\
     \\            `----....___    `. \\  |
      `.           _ ----- _   `._  )/  |
        `.       /"  \\   /"  \\`.  `._   |
          `.    ((O)` ) ((O)` ) `.   `._\\
            `-- '`---'   `---' )  `.    `-.
               /                  ` \\      `-.
             .'                      `.       `.
            /                     `  ` `.       `-.
     .--.   \\ ===._____.======. `    `   `. .___.--`     .''''.
    ' .` `-. `.                )`. `   ` ` \\          .' . '  )
   (  .  ` `-.`.               ( .  ` `  .`\\      .'  '    ' /
    \\  `. `    `-.               ) ` .   ` ` \\  .'   ' .  '  /
     \\ ` `.  ` . \\`.    .--.     |  ` ) `   .``/   '  // .  /
      `.  ``. .   \\ \\   .-- `.  (  ` /_   ` . / ' .  '/   .'
        `. ` \\  `  \\ \\  '-.   `-'  .'  `-.  `   .  .'/  .'
          \\ `.`.  ` \\ \\    ) /`._.`       `.  ` .  .'  /
           |  `.`. . \\ \\  (.'               `.   .'  .'
        __/  .. \\ \\ ` ) \\                     \.' .. \\__
 .-._.-'     '"  ) .-'   `.                   (  '"     `-._.--.
(_________.-====' / .' /\\_)`--..__________..-- `====-. _________)
                 (.'(.
       
   $$$$$\                                           $$\                 
   \__$$ |                                          $$ |                
      $$ | $$$$$$\   $$$$$$\   $$$$$$\         $$$$$$$ | $$$$$$\        
      $$ |$$  __$$\ $$  __$$\ $$  __$$\       $$  __$$ |$$  __$$\       
$$\   $$ |$$ /  $$ |$$ /  $$ |$$ /  $$ |      $$ /  $$ |$$ /  $$ |      
$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |      $$ |  $$ |$$ |  $$ |      
\$$$$$$  |\$$$$$$  |\$$$$$$$ |\$$$$$$  |      \$$$$$$$ |\$$$$$$  |      
 \______/  \______/  \____$$ | \______/        \_______| \______/       
                    $$\   $$ |                                          
                    \$$$$$$  |                                          
                     \______/                                           
   $$\                        $$\           $$\                         
 $$$$$$\                      \__|          $$ |                        
$$  __$$\  $$$$$$\   $$$$$$\  $$\ $$$$$$$\  $$$$$$$\   $$$$$$\          
$$ /  \__| \____$$\ $$  __$$\ $$ |$$  __$$\ $$  __$$\ $$  __$$\         
\$$$$$$\   $$$$$$$ |$$ /  $$ |$$ |$$ |  $$ |$$ |  $$ |$$ /  $$ |        
 \___ $$\ $$  __$$ |$$ |  $$ |$$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |        
$$\  \$$ |\$$$$$$$ |$$$$$$$  |$$ |$$ |  $$ |$$ |  $$ |\$$$$$$  |        
\$$$$$$  | \_______|$$  ____/ \__|\__|  \__|\__|  \__| \______/         
 \_$$  _/           $$ |                                                
   \ _/             $$ |                                                
                    \__|""")
    print("Bem-vindo ao jogo do sapinho atravessando a estrada! Boa sorte!\n")

"""
1. Singleton Pattern

Definição: O padrão Singleton garante que uma classe tenha somente uma instância e fornece um ponto de acesso global
a essa instância.

Objetivo: No código, a classe PlayerWallet usa o padrão Singleton para garantir que o jogador tenha apenas um saldo 
de conta durante o jogo. Isso evita a criação de múltiplas instâncias para o saldo do jogador, tornando o 
gerenciamento de recursos mais controlado.
"""
class PlayerWallet:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.balance = 1000  # Saldo inicial fictício
        return cls._instance

    def add_balance(self, amount):
        self.balance += amount

    def subtract_balance(self, amount):
        self.balance -= amount

"""
2. Factory Method Pattern

Definição: O Factory Method é um padrão de criação que define uma interface para criar um objeto, mas permite que as
subclasses decidam qual classe instanciar. Ele permite que você crie objetos sem especificar a classe exata do objeto 
que será criado.

Objetivo: A classe RoadEventFactory utiliza o padrão Factory Method para criar diferentes tipos de eventos na estrada
(como "Truck" ou "Safe"), dependendo de uma probabilidade aleatória.
"""
class RoadEventFactory:
    @staticmethod
    def create_event(probability):
        return "Truck" if random.random() > probability else "Safe"

"""
3. Strategy Pattern

Definição: O padrão Strategy define uma família de algoritmos, coloca cada um deles em uma classe separada e faz com
que elas sejam intercambiáveis. O padrão Strategy permite que o algoritmo varie independentemente dos clientes que o
utilizam.

Objetivo: No código, temos as classes Cross e Stop, que representam estratégias diferentes para o comportamento do 
sapo. Dependendo do evento, o sapo pode escolher "cruzar a estrada" ou "parar".
"""
class CrossingStrategy:
    def execute(self):
        raise NotImplementedError("Subclasses devem implementar o método execute.")

class Cross(CrossingStrategy):
    def execute(self):
        return True  # Sapo continua atravessando

class Stop(CrossingStrategy):
    def execute(self):
        return False  # Sapo para

"""
4. Observer Pattern

Definição: O Observer Pattern define uma dependência de um para muitos entre objetos, de forma que quando um objeto
(sujeito) muda de estado, todos os seus dependentes (observadores) são notificados e atualizados automaticamente.

Objetivo: O padrão Observer é utilizado no código pela classe GameObserver, que mantém o controle do número de 
travessias do sapo. Quando o evento é notificado, o GameObserver é atualizado e pode modificar o comportamento do 
jogo, como calcular a recompensa.
"""
class GameObserver:
    def __init__(self):
        self.crossings = 0

    def notify(self, event):
        if event == "Safe":
            self.crossings += 1
            return True
        elif event == "Truck":
            return False

"""
5. Decorator Pattern

Definição: O padrão Decorator permite adicionar comportamentos a objetos individuais, dinamicamente, sem afetar o 
comportamento de outros objetos da mesma classe.

Objetivo: O Decorator Pattern é utilizado no código para modificar a recompensa do jogador dependendo de quantas 
travessias ele fez. O decorador reward_multiplier aumenta a recompensa com base nas travessias.
"""
def reward_multiplier(func):
    def wrapper(crossings, bet):
        return func(crossings, bet) * (1 + crossings * 0.05)
    return wrapper

@reward_multiplier
def calculate_reward(crossings, bet):
    return bet

# Função para variar as probabilidades
def adjust_probability(probability, round_number):
    # Aumenta a probabilidade de perder a cada rodada
    shift = random.uniform(-0.15, 0.15)
    probability += shift

    # Tendência a favorecer a casa (máxima dificuldade)
    house_bias = random.uniform(-0.05, 0.05)
    probability += house_bias

    # Limita a probabilidade entre 0.1 e 0.85
    return max(0.1, min(probability, 0.85))

# Jogo principal
def main():
    display_sapo()
    print("O saldo inicial é R$1000. Boa sorte!")

    wallet = PlayerWallet()
    observer = GameObserver()
    bet = 0
    round_number = 1
    probability = 0.6  # Início com 60% de chance de ganhar

    while True:
        print(f"\nSaldo atual: ${wallet.balance:.2f}")

        if wallet.balance <= 0:
            print("Saldo zerado!")
            print("Deseja depositar mais dinheiro ou parar de jogar?")
            print("1 - Depositar mais")
            print("2 - Parar de jogar")
            choice = input("Escolha uma opção: ")

            if choice == "1":
                amount = float(input("Quanto você quer depositar? "))
                wallet.add_balance(amount)
                print(f"Você depositou ${amount}. Saldo atual: ${wallet.balance:.2f}")
            elif choice == "2":
                print("Obrigado por jogar! Até a próxima.")
                break
            else:
                print("Opção inválida. Tente novamente.")
                continue

        bet = float(input("Quanto você deseja apostar? R$ "))
        
        if bet <= 0:
            print("Aposta inválida, tente novamente.")
            continue
        
        if bet > wallet.balance:
            print("Saldo insuficiente para essa aposta.")
            continue

        # Ajusta a probabilidade de sucesso
        probability = adjust_probability(probability, round_number)
        round_number += 1

        # Cria o evento da estrada
        event = RoadEventFactory.create_event(probability)
        print(f"\nRodada {round_number}: O sapo está tentando atravessar a estrada...")

        if event == "Safe":
            print("O sapo conseguiu atravessar a estrada com sucesso!")
            wallet.add_balance(calculate_reward(observer.crossings, bet))  # Calcula o prêmio
        else:
            print("Oh não! Um caminhão atropelou o sapo!")
            wallet.subtract_balance(bet)  # Perde a aposta

        observer.notify(event)  # Atualiza o estado do jogo

        # Opção de continuar ou parar
        print(f"\nSaldo atual: ${wallet.balance:.2f}")
        if wallet.balance > 0:
            continue_choice = input("Você quer continuar jogando? (s/n): ")
            if continue_choice.lower() != 's':
                print("Obrigado por jogar! Até a próxima.")
                break
        else:
            print("Você perdeu tudo!")
            print("Deseja depositar mais dinheiro ou parar de jogar?")
            print("1 - Depositar mais")
            print("2 - Parar de jogar")
            choice = input("Escolha uma opção: ")
            if choice == "1":
                amount = float(input("Quanto você quer depositar? "))
                wallet.add_balance(amount)
                print(f"Você depositou ${amount}. Saldo atual: ${wallet.balance:.2f}")
            elif choice == "2":
                print("Obrigado por jogar! Até a próxima.")
                break

if __name__ == "__main__":
    main()