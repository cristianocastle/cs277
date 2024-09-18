# cris padilla, Naithen Ramirez
#



def read_map():
    with open('map.txt', 'r') as file:
        map2d = []
        for line in file:
            row = [char for char in line.strip() if char]
            map2d.append(row)
    return map2d


def display_map(map, player):
    for i, row in enumerate(map):
        for j, item in enumerate(row):
            if [i, j] == player:
                print('P', end=' ')
            else:
                print(item, end=' ')
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
        print("Move out of bounds!")


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
        move = input("Enter move (W/A/S/D), look around (L), or quit (Q): ").upper()
        
        if move in ['W', 'A', 'S', 'D']:
            move_player(player, move, upper_bound)
            if map[player[0]][player[1]] == 'T':
                print("You found a treasure!")
                user_map[player[0]][player[1]] = 'T'
                treasures_found += 1
                if treasures_found == 7:
                    print("You found all treasures! You win!")
                    break
            elif map[player[0]][player[1]] == 'X':
                print("You hit a trap! Game over!")
                break
        elif move == 'L':
            treasures, traps = count_treasures_traps(map, player, upper_bound)
            print(f"Treasures nearby: {treasures}, Traps nearby: {traps}")
            user_map[player[0]][player[1]] = str(traps)
        elif move == 'Q':
            print("Game quit!")
            break
        else:
            print("Invalid input!")
    
    
if __name__ == "__main__":
    main()