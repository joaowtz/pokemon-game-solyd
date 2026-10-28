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
        print('----------------------------------------------')
        escolha = input('Digite sua escolha (1, 2 ou 3):')
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
            print('Jogo carregado com sucesso!')
            return player
    except Exception as error:
        print('Nenhum jogo salvo encontrado. Iniciando um novo jogo...')
        
if __name__ == '__main__':

    player = carregar_jogo()

print('----------------------------------------------')
print('Bem-vindo ao jogo Pokémon de terminal!')
print('----------------------------------------------')

if not player:
        nickname = input('Digite seu nickname:')
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

        escolha = input('Agora que voce está pronto, tem uma pessoa te encarando! OBS: com más intenções... Deseja batalhar com ele? (s/n)')
        if escolha == 's':
            inimigo1 = Enemy(pokemons=[PokemonAgua('squirtle', level=5), PokemonFogo('growlithe', level=3)])
            time.sleep(1)
            print('----------------------------------------------') 
            print('Legal, ele aceitou a batalha!')
            print('Seu inimigo é um treinador chamado {} e ele possui os seguintes pokemons:'.format(inimigo1.nome))
            time.sleep(1)
            print('----------------------------------------------')
            inimigo1.mostrar_pokemons()
            print('----------------------------------------------')
            player.batalhar(inimigo1)
        else:
            print('Sábia decisão, mas lembre-se que o mundo Pokémon é cheio de desafios e batalhas!')
            salvar_jogo(player)

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
    escolha = input('Digite sua escolha (1, 2, 3, 4 ou 5):')
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
    else:
        print('Escolha inválida. Por favor, digite 1, 2, 3, 4 ou 5.')


