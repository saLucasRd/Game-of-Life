import os
import random
import time

width:int = 30
height:int = 30

def dead_state(height:int, width:int):
    return [[0] * width for _ in range(height)]

def random_state(height:int, width:int):
    state = dead_state(height, width)

    for i in range(height): #linhas

        for j in range(width): #colunas
            random_number = random.random()
            if random_number >= 0.2:
                state[i][j] = 0
            else:
                state[i][j] = 1

    return state

def render(state):
    os.system("clear")
    for row in state:
        print(" ".join("■" if cell else "□" for cell in row))
    print()


def next_board_state(state:list, height:int, width:int):
    new_state = dead_state(height, width)

    for i in range(height):
        for j in range(width):
            live_neighbours = count_neighbours(state, i, j, height, width)

            if state[i][j] == 1:
                #underpop overpop check
                if live_neighbours in [2, 3]:
                    new_state[i][j] = 1
            else:
                if live_neighbours == 3:
                    new_state[i][j] = 1


    return new_state

def count_neighbours(state:list, i:int, j:int, height:int, width:int):
    # faz a checagem dos vizinhos nessa referencia
    # (-1,-1)  (-1,0)  (-1,+1)
    # (0,-1)   ( i,j )  (0,+1)
    # (+1,-1)  (+1,0)  (+1,+1)

    neighbors = [(-1, -1), (-1, 0), (-1, +1), (0, -1), (0, +1), (+1, -1), (+1, 0), (+1, +1)]


    live_neighbors = 0

    for di, dj in neighbors:
        ni, nj = i + di, j + dj

        if 0 <= ni < height and 0 <= nj < width:
            live_neighbors += state[ni][nj]



    return live_neighbors


def game_of_life(height, width, generations=10, delay=0.7):
    state = random_state(height, width)

    for _ in range(generations):
        render(state)
        state = next_board_state(state, height, width)
        time.sleep(delay)

game_of_life(height, width, generations = 20)