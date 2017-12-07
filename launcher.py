import random
import time

#Pokemon Clone Made By Hunter Levinger 

class Monster(object):
    def __init__(self, name, attack, defense, poketype, lvl):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.poketype = poketype
        self.max_health = lvl * 65
        self.health = self.max_health
        self.lvl = lvl
    
    @property
    def get_name(self):
      return self.name
    @property
    def get_attack(self):
      return self.poketype
    
    @property
    def get_defense(self):
      return self.defense
    
    @property
    def get_type(self):
      return self.poketype

    @property
    def get_lvl(self):
      return self.lvl
    
    @property
    def get_health(self):
      return self.health

    @property
    def get_max_health(self):
      return self.get_max_health

    @property
    def take_damage(self, damage_dealt):
      if self.health - damage_dealt < 0:
        self.health = 0
      else:
        self.health -= damage_dealt

    def attack_monster(self, monster):
      variance = random.randint(1, 10)
      damage_dealt = random.randint(1, self.attack)
      damage_blocked = random.randint(1, monster.get_defense())
      net_damage = abs((damage_dealt - damage_blocked) * 10)
      monster.take_damage(net_damage)
      return net_damage

    @staticmethod
    def create_monster(player=None):
      attack, defense, poketype,lvl = 0,0,0,0
      
      if player is None:
        lvl = random.randint(1, 100)
        attack = random.randint(1 + lvl, 100 + lvl)
        defense = random.randint(1 + lvl, 100 + lvl)
        poketype = random.randint(1 + lvl, 100 + lvl)
      else:
        variance = random.randint(1, 20)
        lvl = random.randint(player.get_lvl() - variance, player.get_lvl() + variance)
        attack = random.randint(lvl - variance, lvl + variance)
        defense = random.randint(lvl - variance, lvl + variance)
        poketype = random.randint(lvl - variance, lvl + variance)

      return Monster("random_monster", attack, defense, poketype, lvl)

def battle(player_pokemon, enemy_pokemon):
  in_battle = True
  choices = {1,2,3,4}
  victor = None
  turn = 0

  while in_battle:
    print("-----", turn, "turn-----\n")
    print("Enemy Health: ", enemy_pokemon.get_health())
    print("Player Health: ", player_pokemon.get_health())
    print("\nWhat do you want to do? \n1. attack\n2. capture\n3. Use Item \n4. Run\n")
    selected_choice = 0
    
    while True:
      choice = int(input('-> '))

      if choice in choices:
        selected_choice = choice
        break
      else:
        print("Not a valid choice!")
        continue

    print()

    if selected_choice == 1:
      dmg_dealt = player_pokemon.attack_monster(enemy_pokemon)
      
      print("You attacked " + enemy_pokemon.get_name())
      print("Damage done: ", dmg_dealt)
      print("their new health: ", enemy_pokemon.get_health())
      print()
      
      if enemy_pokemon.get_health() == 0:
        in_battle = False
        victor = player_pokemon.get_name()

    elif selected_choice == 2:
      pass
    elif selected_choice == 3:
      pass
    elif selected_choice == 4:
      in_battle = False

    
    dmg_dealt = enemy_pokemon.attack_monster(player_pokemon)
    
    print(enemy_pokemon.get_name() + " attacked you!")
    print("Damage done: ", str(dmg_dealt))
    print("Your new health: " + str(player_pokemon.get_health()))
    print()

    if player_pokemon.get_health() == 0:
        in_battle = False
        victor = enemy_pokemon.get_name()
    turn += 1

  if victor is not None:
    print("The battle is over! Your victor is: " + victor)
  else:
    print("You have fled...")

if __name__ == "__main__":
  player_pokemon = Monster("player", 65, 32, 4, 23)
  enemy_pokemon = Monster.create_monster(player_pokemon)
  battle(player_pokemon, enemy_pokemon)
