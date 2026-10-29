from Pokemon import *
from Pessoas import *
import time
import pickle


def escolher_pokemon_inicial(player):
    pikachu = PokemonEletrico('Pikachu', level=1)
    charmander = PokemonFogo('Charmander', level=1)
    squirtle = PokemonAgua('Squirtle', level=1)

    print('Voce possui 3 escolhas de Pokémon iniciais: ')
    print('1 - {}'.format(pikachu.nome))
    print('2 - {}'.format(charmander.nome))
    print('3 - {}'.format(squirtle.nome))

    while True:  
        escolha = input('Digite sua escolha (1, 2 ou 3): ').strip()
        print('----------------------------------------------')
        if escolha == '1':
            player.capturar(pikachu)
            print('Voce escolheu {} como seu pokemon inicial!'.format(pikachu.nome))
            break

        elif escolha == '2':
            player.capturar(charmander)
            print('Voce escolheu {} como seu pokemon inicial!'.format(charmander.nome))
            break

        elif escolha == '3':
            player.capturar(squirtle)
            print('Voce escolheu {} como seu pokemon inicial!'.format(squirtle.nome))
            break

        else:
            print('Escolha inválida. Por favor, digite 1, 2 ou 3.')

    print('----------------------------------------------')

def salvar_jogo(player):
    try:
        with open('database.db', 'wb') as arquivo:
            pickle.dump(player, arquivo)
            print('Jogo salvo com sucesso!')
    except Exception as error:
        print('Erro ao salvar o jogo: {}'.format(error))

def carregar_jogo():
    try:
        with open('database.db', 'rb') as arquivo:
            player = pickle.load(arquivo)
            if player:
                print('Jogo carregado com sucesso!')
                time.sleep(1)
                print('Seja bem-vindo de volta, {}!'.format(player.nome))
                time.sleep(1)
                return player
            else:
                print('Nenhum jogo salvo encontrado. Iniciando um novo jogo...')
                return None
    except Exception as error:
        print('Nenhum jogo salvo encontrado. Iniciando um novo jogo...')
        return None

def apagar_jogo():
    try:
        with open('database.db', 'wb') as arquivo:
            pickle.dump(None, arquivo)
            print('Jogo apagado com sucesso!')
    except Exception as error:
        print('Erro ao apagar o jogo: {}'.format(error))
        
if __name__ == '__main__':

    print('----------------------------------------------')
    print('Bem-vindo ao jogo Pokémon de terminal!')
    print('----------------------------------------------')


player = carregar_jogo()

if not player:
    nickname = input('Digite seu nickname: ')
    player = Player(nickname)
    print('Olá {}, seja bem-vindo ao mundo Pokémon!'.format(nickname))
    
    if player.pokemons:
        print('Vejo que você já possui pokemons!')
        time.sleep(1)
        player.mostrar_pokemons()
    else:
        print('-----------------------------------------------')
        print('Você ainda não possui pokemons, vamos escolher um!')
        time.sleep(1)
        escolher_pokemon_inicial(player)
        time.sleep(1)

    while True:
        escolha = input('Agora que você está pronto, tem uma pessoa te encarando! OBS: com más intenções... Deseja batalhar com ele? (s/n): ').strip().lower()
        if escolha == 's':
            inimigo1 = Enemy(pokemons=[PokemonAgua('squirtle', level=5), PokemonFogo('growlithe', level=3)])
            time.sleep(1)
            print('----------------------------------------------') 
            print('Legal, ele aceitou a batalha!')
            print('Seu inimigo é um treinador chamado {}, Boa sorte!'.format(inimigo1.nome))
            time.sleep(1)
            print('----------------------------------------------')
            player.batalhar(inimigo1)
            break
        elif escolha == 'n':
            print('Sábia decisão, mas lembre-se que o mundo Pokémon é cheio de desafios e batalhas!')
            break
        else:
            print('Escolha inválida. Por favor, digite "s" para sim ou "n" para não.')

        time.sleep(1)
        print('----------------------------------------------')

while True:
    print('----------------------------------------------')
    print('O que deseja fazer agora?')
    print('1 - Explorar')
    print('2 - Batalhar com um inimigo')
    print('3 - Mostrar pokemons')
    print('4 - Mostrar dinheiro')
    print('5 - Salvar e sair do jogo')
    print('6 - Apagar jogo salvo')
    escolha = input('Digite sua escolha (1, 2, 3, 4, 5 ou 6):').strip()
    print('----------------------------------------------')
    if escolha == '1':
        player.explorar()
    elif escolha == '2':
        time.sleep(1)
        inimigo_aleatorio = Enemy()
        player.batalhar(inimigo_aleatorio)
    elif escolha == '3':
        player.mostrar_pokemons()
    elif escolha == '4':
        player.mostrar_dinheiro()
        time.sleep(2)
    elif escolha == '5':
        print('Obrigado por jogar! Até a próxima!')
        salvar_jogo(player)
        break
    elif escolha == '6':
        time.sleep(1)
        desejar = input('Tem certexa que deseja apagar o jogo salvo? (s/n): ').strip().lower()
        if desejar == 's':
            print('Apagando jogo salvo...')
            time.sleep(1)
            apagar_jogo()
            time.sleep(1)
            print('Saindo do jogo...')
            time.sleep(1)
            break
        else:
            print('Jogo salvo mantido.')
    else:
        print('Escolha inválida. Por favor, digite 1, 2, 3, 4, 5 ou 6.')


