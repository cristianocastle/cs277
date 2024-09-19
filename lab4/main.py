# cris padilla, Naithen Ramirez
# sep 19, 2024
# treasure hunt game

def read_map():
    hiddenmap = open("map.txt")
    map2d = []
    for row in hiddenmap:
        list = []
        for item in row:
            if item != " " and item != '\n':
                list.append(item)
        map2d.append(list)
    return map2d


def display_map(map, player):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if i == player[0] and j == player[1]:
                print("P", end = " ")
            else:
                print(map[i][j], end = " ")
        print()

    
def move_player(player, dir, upper_bound):
    if dir == 'W' and player[0] > 0:
        player[0] -= 1
    elif dir == 'A' and player[1] > 0:
        player[1] -= 1
    elif dir == 'S' and player[0] < upper_bound:
        player[0] += 1
    elif dir == 'D' and player[1] < upper_bound:
        player[1] += 1
    else:
        print("You cannot move that direction.")


def count_treasure_traps(map, player, upper_bound):
    treasures = 0
    traps = 0
    for i in range(max(0, player[0] - 1), min(upper_bound + 1, player[0] + 2)):
        for j in range(max(0, player[1] - 1), min(upper_bound + 1, player[1] + 2)):
            if [i, j] != player:
                if map[i][j] == 'T':
                    treasures += 1
                elif map[i][j] == 'X':
                    traps += 1
    return treasures, traps


def main():
    map = read_map()
    player = [0, 0]
    upper_bound = 6
    user_map = [['.' for _ in range(7)] for _ in range(7)]
    treasures_found = 0
    
    while True:
        display_map(user_map, player)
        move = input("Enter Direction (WASD or L to look around, or Q to quit):").upper()
        
        if move in ['W', 'A', 'S', 'D']:
            move_player(player, move, upper_bound)
            if map[player[0]][player[1]] == 'T':
                print("You found a treasure!")
                user_map[player[0]][player[1]] = 'T'
                treasures_found += 1
                print(f"There are {7 - treasures_found} treasures remaining.")
                if treasures_found == 7:
                    print("You found all treasures! You win!")
                    break
            elif map[player[0]][player[1]] == 'X':
                print("You were caught in a trap!")
                print(f"You found {treasures_found} treasures.")
                break
        elif move == 'L':
            treasures, traps = count_treasure_traps(map, player, upper_bound)
            print(f"You detect {treasures} treasures nearby.")
            print(f"you detect {traps} traps nearby.")
            user_map[player[0]][player[1]] = str(traps)
        elif move == 'Q':
            print("Game quit!")
            break
        else:
            print("Invalid input!")
    
if __name__ == "__main__":
    main()