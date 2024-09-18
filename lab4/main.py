# cris padilla, Naithen Ramirez
#


import check_input



def read_map():
    hiddenmap = open("map.txt")
    list2d = []
    for row in hiddenmap:
        list = []
        for item in row:
            if item != "" and item != '\n':
                list.append(item)
        list2d.append(list)
    return list2d


def display_map(map, player):
    pass
    map = open("shownmap.txt")
    shownmap2d = []
    for row in map:
        list = []
        for item in row:
            if item != "" and item != '\n':
                list.append(item)
        shownmap2d.append(list)
    return showmap2d

    
def move_player(player, dir, upper_bound):
    pass 


    if dir == 'W': 
        player[1] += 1
    if dir == 'A':
        player[0] -= 1
    if dir == 'S':
        player[1] -= 1
    if dir == 'D':
        player[0] += 1


def count_treasure_traps(map, player, upper_bound):
    pass


def main():
    
    player = [0,0]