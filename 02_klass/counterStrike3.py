from crosshair import Crosshair
from player import Player
from weapon import Weapon, m4a4, ak47

player1=Player(x=0, y=0, health=100, weapon=m4a4)
player2=Player(x=3, y=5, health=100, weapon=ak47)

while player1.health > 0 and player2.health > 0:
    print(f"Player1 position: x={player1.x}, y={player1.y},{player1.health}HP")
    print(f"Player1 crosshair: x={player1.crosshair.x}, y={player1.crosshair.y}")

#Player 1 move
    move = input("Move player1? (y/n)")
    if move == "y":
        direction = input("Move player1 (left/right/forward/backwards): ")
        player1.step(direction)
        print(f"Player1 position: x={player1.x}, y={player1.y},{player1.health}HP")
        print(f"Player1 crosshair: x={player1.crosshair.x}, y={player1.crosshair.y}")

#Player 1 aim
    aim = input("Move the crosshair? (y/n)")
    if aim == "y":
        aim_direction = input("Move player1 crosshair (left/right/up/down): ")
        player1.crosshair.move_crosshair(aim_direction)
        print(f"Player1 crosshair: x={player1.crosshair.x}, y={player1.crosshair.y}")

#Player 1 attack
    shoot = input("Pull the trigger? (y/n): ")
    if shoot == "y":
        if player1.crosshair.x == player2.x and player1.crosshair.y == player2.y:
            player2.take_damage(player1.weapon.damage)
            print(f"Hit! Player2 health: {player2.health}")
        else:
            print("Miss!")

#Player 2 move            
    print(f"Player2 position: x={player2.x}, y={player2.y},{player2.health}HP")
    print(f"Player2 crosshair: x={player2.crosshair.x}, y={player2.crosshair.y}")        
    move = input("Move player2? (y/n)")
    if move == "y":        
        direction = input("Move player2 (left/right/forward/backwards): ")
        player2.step(direction)
        print(f"Player2 position: x={player2.x}, y={player2.y}, {player2.health}HP")
        print(f"Player2 crosshair: x={player2.crosshair.x}, y={player2.crosshair.y}")

#Player 2 aim
    aim = input("Move the crosshair? (y/n)")
    if aim == "y":
        aim_direction = input("Move player2 crosshair (left/right/up/down): ")
        player2.crosshair.move_crosshair(aim_direction)
        print(f"Player2 crosshair: x={player2.crosshair.x}, y={player2.crosshair.y}")

#Player 2 attack
    shoot = input("Pull the trigger? (y/n): ")
    if shoot == "y":
        if player2.crosshair.x == player1.x and player2.crosshair.y == player1.y:
            player1.take_damage(player2.weapon.damage)
            print(f"Hit! Player1 health: {player1.health}")
        else:
            print("Miss!")

if player1.health <= 0:
    print("Game over! Player2 won!")
else:
    print("Game over! Player1 won!")