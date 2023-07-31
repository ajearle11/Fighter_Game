import random

class Fighter:
    def __init__(self,name, type, health, attack_points, defense_points):
        self.name = name
        self.type = type
        self.health = health
        self.attack_points = attack_points
        self.defense_points = defense_points

    def __str__(self):
        return f"{self.name}"

    def attack(self, type):
        if (self.type == type):
            return f"attack, {self.attack_points}"
        elif (self.type == "water" and type == "fire"):
            return f"attack, {self.attack_points * 2}"
        elif(self.type == "fire" and type == "water"):
            return f"attack, {self.attack_points * 0.5}"
        elif (self.type == "fire" and type == "grass"):
            return f"attack, {self.attack_points * 2}"
        elif(self.type == "grass" and type == "fire"):
            return f"attack, {self.attack_points * 0.5}"
        elif (self.type == "grass" and type == "water"):
            return f"attack, {self.attack_points * 2}"
        elif(self.type == "water" and type == "grass"):
            return f"attack, {self.attack_points * 0.5}"

    def defense(self, type):
        if (self.type == type):
            return f"defend, {self.defense_points}"
        elif (self.type == "water" and type == "fire"):
            return f"defend, {self.defense_points * 2}"
        elif(self.type == "fire" and type == "water"):
            return f"defend, {self.defense_points * 0.5}"
        elif (self.type == "fire" and type == "grass"):
            return f"defend, {self.defense_points * 2}"
        elif(self.type == "grass" and type == "fire"):
            return f"defend, {self.defense_points * 0.5}"
        elif (self.type == "grass" and type == "water"):
            return f"defend, {self.defense_points * 2}"
        elif(self.type == "water" and type == "grass"):
            return f"defend, {self.defense_points * 0.5}"

    def special_attack(self, type):
        random_number = random.randint(0,10)
        if random_number > 5:
            return str(self.attack_points * 3)
        else: 
            return str(0)

    def set_health(self, amount):
        self.health = self.health - amount
        return self.health
    

hydrogodl = Fighter("Hydrogodl", "water", 30, 5, 3)
incinerass = Fighter("Incinerass", "fire", 26, 6, 3)
pilfern = Fighter("Pilfern", "grass", 40, 4, 4)
goblecrie = Fighter("Goblecrie", "water", 34, 6, 2)
firenzeroar = Fighter("Firenzeroar", "fire", 40, 6, 2)
laveniah = Fighter("Laveniah", "grass", 28, 6, 3)

fighters = [hydrogodl, incinerass, pilfern, goblecrie, firenzeroar, laveniah]

player_one = fighters[random.randint(0,5)]
player_two = fighters[random.randint(0,5)]

print(f"{player_one} vs {player_two}")

game = True

while game == True:

    print("\nP1: Which move would you like: Attack (a), Defense (d), Special Attack (s)")
    p1_choice = input() 
    while p1_choice.lower() != 'a' and p1_choice.lower() != 'd' and p1_choice.lower() != 's':
        p1_choice = input() 
        

    print("\nP2: Which move would you like: Attack (a), Defense (d), Special Attack (s)")
    p2_choice = input() 
    while p2_choice.lower() != 'a' and p2_choice.lower() != 'd' and p2_choice.lower() != 's':
        p2_choice = input() 

    if p1_choice.lower() == 'a':
        p1_move = player_one.attack(player_two.type)
    elif p1_choice.lower() == 'd':
        p1_move = player_one.defense(player_two.type)
    else:
        p1_move = player_one.special_attack(player_two.type)

    if p2_choice.lower() == 'a':
        p2_move = player_one.attack(player_one.type)
    elif p2_choice.lower() == 'd':
        p2_move = player_one.defense(player_one.type)
    else:
        p2_move = player_one.special_attack(player_one.type)


    slice_method = slice(8, 10)

    if "attack" in p1_move:
        p1_damage_output = float(p1_move[slice_method])

        if "defend" in p2_move:
            p2_defense_output = float(p2_move[slice_method])
            if (p1_damage_output - p2_defense_output) < 1: 
                player_two.set_health(1)
            else: 
                player_two.set_health(p1_damage_output - p2_defense_output)
        
        if "attack" in p2_move:
            p2_damage_output = float(p2_move[slice_method])
            player_one.set_health(p2_damage_output)
            player_two.set_health(p1_damage_output)

        if "attack"not in p2_move and "defend" not in p2_move: 
            p2_special_damage_output = float(p2_move)
            player_one.set_health(p2_special_damage_output)
            player_two.set_health(p1_damage_output)

    if "attack" not in p1_move and "defend" not in p1_move:
        p1_damage_output = float(p1_move)

        if "defend" in p2_move:
            p2_defense_output = float(p2_move[slice_method])
            if (p1_damage_output - p2_defense_output) < 1: 
                player_two.set_health(1)
            else: 
                player_two.set_health(p1_damage_output - p2_defense_output)
        
        if "attack" in p2_move:
            p2_damage_output = float(p2_move[slice_method])
            player_one.set_health(p2_damage_output)
            player_two.set_health(p1_damage_output)

        if "attack" not in p2_move and "defend" not in p2_move: 
            p2_special_damage_output = float(p2_move)
            player_one.set_health(p2_special_damage_output)
            player_two.set_health(p1_damage_output)

    if "defend" in p1_move:
        p1_defense_output = float(p1_move[slice_method])

        if "attack" in p2_move:
            p2_damage_output = float(p2_move[slice_method])
            if (p2_damage_output - p1_defense_output) < 1: 
                player_one.set_health(1)
            else: 
                player_one.set_health(p2_damage_output - p1_defense_output)

        if "attack" not in p2_move and "defend" not in p2_move:
            p2_special_damage_output = float(p2_move)
            if (p2_special_damage_output == 0):
                pass
            elif (p2_special_damage_output - p1_defense_output) < 1: 
                player_one.set_health(1)
            else: 
                player_one.set_health(p2_special_damage_output - p1_defense_output)

        if "defend" in p2_move:
            pass


    
    print(f"\n{player_one.name} has {player_one.set_health(0)} health points")
    print(f"\n{player_two.name} has {player_two.set_health(0)} health points")

    if player_one.set_health(0) <= 0 or player_two.set_health(0) <= 0:
        if player_one.set_health(0) > player_two.set_health(0):
            print(f"\n{player_one.name} wins!")
        else:
            print(f"\n{player_two.name} wins!")
        game = False


