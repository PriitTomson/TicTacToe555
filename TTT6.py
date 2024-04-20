import random

tic_tac_toe = [' '] * 9


def start_game():
    git tic_tac_toe
    for i in range(9):
        tic_tac_toe[i] = ' '


def who_goes_first():
    if random.randint(0, 1) == 0:
        return "computer"
    else:
        return "player"


def print_game():
    tic_tac_toe
    print("------------------------------------")
    print("")
    print(" [{}] [{}] [{}]     [1] [2] [3]".
          format(tic_tac_toe[0], tic_tac_toe[1], tic_tac_toe[2]))
    print(" [{}] [{}] [{}]     [4] [5] [6]".
          format(tic_tac_toe[3], tic_tac_toe[4], tic_tac_toe[5]))
    print(" [{}] [{}] [{}]     [7] [8] [9]".
          format(tic_tac_toe[6], tic_tac_toe[7], tic_tac_toe[8]))
    print("")


def machine_move():
    tic_tac_toe
    while True:
        r = random.randint(0, 8)
        if tic_tac_toe[r] == ' ':
            tic_tac_toe[r] = 'O'
            break


def check_end(p):
    tic_tac_toe
    t = tic_tac_toe

    # rows
    if t[0] == p and t[1] == p and t[2] == p:
        return True
    if t[3] == p and t[4] == p and t[5] == p:
        return True
    if t[6] == p and t[7] == p and t[8] == p:
        return True
    # columns
    if t[0] == p and t[3] == p and t[6] == p:
        return True
    if t[1] == p and t[4] == p and t[7] == p:
        return True
    if t[2] == p and t[5] == p and t[8] == p:
        return True
    # diagonals
    if t[0] == p and t[4] == p and t[8] == p:
        return True
    if t[2] == p and t[4] == p and t[6] == p:
        return True

    return False


def tie_conditions():
    tic_tac_toe
    for i in range(9):
        if tic_tac_toe[i] == ' ':
            return False
    return True


who = who_goes_first()
while True:

    print("====WELCOME TO TIC-TAC-TOE====")
    start_game()

    if who == "computer":
        machine_move()
        print("Computer made the first move")
    else:
        print("You made the first move")
    while True:
        print_game()
        user_input = int(input("Place X in specific coordinate: "))

        if user_input < 1 or user_input > 9:
            print("Please insert number from 1 to 9")
            continue
        if tic_tac_toe[user_input - 1] != ' ':
            print("serious??")
            continue

        tic_tac_toe[user_input - 1] = 'X'
        if check_end('X'):
            print_game()
            print("palyer wins .. ")
            break
        machine_move()
        if check_end('O'):
            print_game()
            print("computer wins .. ")
            break
        if tie_conditions():
            print_game()
            print("TIE .. ")
            break

        continue

    user_choice_continue_game = input("Do you want to continue the game? y/n ")
    if user_choice_continue_game == "n":
        print("Bye!")
        break
