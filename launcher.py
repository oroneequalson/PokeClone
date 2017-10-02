import random
import time

#Pokemon Clone Made By Hunter Levinger 

class monster:
    def __init__(self, attack, defence, type, lvl):
        self.type = type
        self.attack = attack
        self.defence = defence
        self.maxHealth = lvl * 65
        self.health = self.maxHealth
        self.lvl = lvl
    def manageHealth(self,amount):
      self.health += amount
    def fight(self, monster):
        print("Enemy Health: {}".format(monster.health))
        print("Player Health {}".format(self.health))
        print("What do you want to do? \n	1. attack\n	2. capture\n	3. Use Item \n	4. Run")
        choice = int(input('-> '))
        if choice == 1:
          #attack code
          damage = (self.attack / enemy.defence) * 10
          enemyDmg = (enemy.attack / self.defence) * 10
          enemy.manageHealth(-damage)
          self.manageHealth(-enemyDmg)
          if enemy.health <= 0:
            print("you won")
            self.health = self.maxHealth
          elif enemy.health <= 0:
            print("you lost")
            self.health = self.maxHealth
          else:
            print("Enemy Health: {}\nPlayer Health: {}".format(enemy.health, self.health))
            self.fight(enemy)
        elif choice == 2:
          #capture code
          print('capture')
        elif choice == 3:
          #item code
          print("items")
        elif choice == 4:
          #running code
          print('code')
player = monster(5,5,3,2)
while True:
  attackRand = random.randint(player.attack - 2, player.attack + 3)
  defenceRand =random.randint(player.defence - 2, player.defence + 3)
  lvlRand = random.randint(player.lvl -1, player.lvl + 2)
  enemy = monster(attackRand, defenceRand, 3, lvlRand)
  player.fight(enemy)
