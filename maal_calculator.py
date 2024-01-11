from os import system


def main():
    system('cls')

    print("*** THE MARRIEGE MAAL CALCULATOR ***")
    print("")
    print("")

    run = False
    while not run:
        num_of_plyers = int(input("Number of Players: "))
        if 1 <= num_of_plyers <= 5:
            run = True

    player = [0] * num_of_plyers
    for i in range(num_of_plyers):
        player[i] = input("Player" + str(i) + ": ").upper()

    a = False
    while not a:
        shower = input("Shown by: ").upper()

        for i in range(num_of_plyers):
            if shower == player[i]:
                shower = player[i]
                a = True

    player_status = [0] * num_of_plyers
    for i in range(num_of_plyers):
        if player[i] != shower:
            a = input(player[i] + "seen? (y/anykey): ").upper()
            if a == "Y":
                player_status[i] = True
            else:
                player_status[i] = False
        else:
            player_status[i] = True

    player_point = [0] * num_of_plyers
    for i in range(num_of_plyers):
        if player_status[i]:
            player_point[i] = int(input(player[i] + "Point:"))

    game_point = int(input("Rs per Point? "))

    total_point = 0
    for i in range(num_of_plyers):
        total_point = total_point + player_point[i]

    player_profit = [0] * num_of_plyers
    for i in range(num_of_plyers):
        if player[i] != shower:
            if player_status[i]:
                player_profit[i] = (player_point[i] * num_of_plyers - total_point - 3) * game_point
            else:
                player_profit[i] = 0 - (total_point + 10) * game_point

    print("")
    print("")

    for i in range(num_of_plyers):
        if player[i] != shower:
            if player_status:
                if player_profit[i] > 0:
                    print(f"{shower} to {player[i]} : Rs.{player_profit[i]}")
                if player_profit[i] < 0:
                    print(f"{player[i]} to {shower} : Rs.{abs(player_profit[i])}")
            else:
                print(f"{player[i]} to {shower} : Rs.{abs(player_profit[i])}")

    print("")
    print("")

    print("Would you like to continue?")
    reuse_input = input("Yes(Y)/Quit(Any-key)").upper()
    if reuse_input == "Y":
        main()


if __name__ == '__main__':
    main()
