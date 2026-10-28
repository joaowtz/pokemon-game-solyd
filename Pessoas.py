import time
import random
from Pokemon import *

NOMES = ['Joao', 'Maria', 'Pedro', 'Ana', 'Lucas', 'Julia', 'Rafael', 'Beatriz',
         'Gabriel', 'Camila'
         ]

POKEMONS = [PokemonEletrico('Pikachu'), PokemonFogo('Charmander'), PokemonAgua('Squirtle'),
            PokemonEletrico('Raichu'), PokemonFogo('Charizard'), PokemonAgua('Blastoise'),
            PokemonEletrico('Jolteon'), PokemonFogo('Flareon'), PokemonAgua('Vaporeon')]


class Pessoa:
    def __init__(self, nome=None, pokemons=[], dinheiro=100):
        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(NOMES)
        self.pokemons = pokemons

        self.dinheiro = dinheiro

    def __str__(self):
        return self.nome

    def mostrar_pokemons(self):
        if self.pokemons:
            print('Pokemons de {}:' .format(self))
            for index,pokemon in enumerate(self.pokemons):
                print('{} - {}' .format(index, pokemon))
        else:
            print('{} nao possui pokemons' .format(self))

    def escolher_pokemon(self):
            if self.pokemons:
                pokemon_escolhido = random.choice(self.pokemons)
                print('{} escolheu {}' .format(self, pokemon_escolhido))
                return pokemon_escolhido
            else:
                print('{} nao possui pokemons para batalhar' .format(self))
                return None

    def mostrar_dinheiro(self):
        print('{} possui {} moedas' .format(self, self.dinheiro))

    def ganhar_dinheiro(self, quantia):
        self.dinheiro += quantia
        print('Voce ganhou {} moedas! Agora possui {} moedas' .format(quantia, self.dinheiro))

    def batalhar(self, Pessoa):
        print('{} esta batalhando com {}' .format(self, Pessoa))

        Pessoa.mostrar_pokemons()
        pokemon_inimigo = Pessoa.escolher_pokemon()
        print('----------------------------------------------')
        self.mostrar_pokemons()
        pokemon_player = self.escolher_pokemon()

        if pokemon_player and pokemon_inimigo:
            while True:
                vitoria = pokemon_player.atacar(pokemon_inimigo)
                time.sleep(1)
                if vitoria:
                    print('{} venceu a batalha contra {}' .format(self, Pessoa))
                    self.ganhar_dinheiro(pokemon_inimigo.level * 100)
                    break
                
                vitoria_inimiga = pokemon_inimigo.atacar(pokemon_player)
                time.sleep(1)
                if vitoria_inimiga:
                    print('Não foi dessa vez...')
                    print('{} venceu a batalha contra {}' .format(Pessoa, self))
                    break
        else:
            print('Batalha nao pode ser realizada...')


class Player(Pessoa):
    tipo = 'Player'

    def capturar(self, pokemon):
        self.pokemons.append(pokemon)
        print('{} capturou o pokemon {}!'.format(self, pokemon))


    def escolher_pokemon(self):
            
            if self.pokemons:
                while True:
                    escolha = input('Escolha um pokemon para batalhar:')
                    try:
                        escolha = int(escolha)
                        pokemon_escolhido = self.pokemons[escolha]
                        print('{} Eu escolho voce' .format(pokemon_escolhido))
                        return pokemon_escolhido
                    except:
                        print('Escolha inválida. Por favor, digite um número válido.')
            else:
                print('{} nao possui pokemons para batalhar' .format(self))

    def explorar(self):
        print('{} esta explorando...' .format(self))
        time.sleep(1)

        if random.random() <= 0.3:
            pokemon = random.choice(POKEMONS)
            print('{} encontrou um pokemon selvagem: {}' .format(self, pokemon))

            escolha = input('Deseja capturar o pokemon {}? (s/n)' .format(pokemon))
            if escolha == 's':
                if random.random() >= 0.5:
                    self.capturar(pokemon)
                else:
                    print('O pokemon {} fugiu!' .format(pokemon))
            else:
                print('ok boa viagem')

        else:
            print('essa exploracao nao deu em nada...')
            return None
        
        
class Enemy(Pessoa):
    tipo = 'Enemy'

    def __init__(self, nome=None, pokemons=None):
        if not pokemons:
            pokemons_aleatorios = []
            for i in range(random.randint(1,6)):
                pokemons_aleatorios.append(random.choice(POKEMONS))

            super().__init__(nome, pokemons=pokemons_aleatorios)
        else:    
            super().__init__(nome, pokemons=pokemons)


class NPC(Pessoa):
    tipo = 'NPC'







