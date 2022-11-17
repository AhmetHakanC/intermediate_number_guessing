def number_controller(number, digit):
    temp = 0
    for i in range(digit):
        temp = number % 10
        number -= temp
        number /= 10
    return int(temp)


def game():
    print("Welcome to number guessing game!")
    flag = False
    while True:
        if flag:
            break
        digit1 = 0
        digit2 = 0
        digit3 = 0
        first_guess = input("Enter your 3 digit guess--> ")
        try:
            first_guess = int(first_guess)
        except:
            print("Try again!")
            continue
        if 99 < first_guess < 1000:
            digit1 = number_controller(first_guess, 3)
            digit2 = number_controller(first_guess, 2)
            digit3 = number_controller(first_guess, 1)
            print(digit1, digit2, digit3)
            print("Guess successfully received. Player 2's turn.")
            while True:
                correct_points = incorrect_points = 0
                guess = input("Your guess--> ")
                try:
                    guess = int(guess)
                except:
                    print("Try again!")
                    continue

                if 99 < guess < 1000:
                    for i in range(1, 4):
                        if number_controller(guess, 4 - i) == digit1:
                            if i == 1:
                                correct_points += 1
                                break
                            else:
                                incorrect_points += 1
                    for i in range(1, 4):
                        if number_controller(guess, 4 - i) == digit2:
                            if i == 2:
                                correct_points += 1
                                break
                            else:
                                incorrect_points += 1
                    for i in range(1, 4):
                        if number_controller(guess, 4 - i) == digit3:
                            if i == 3:
                                correct_points += 1
                                break
                            else:
                                incorrect_points += 1

                    print("correct place--> ", correct_points, "digits")
                    print("incorrect place--> ", incorrect_points, "digits")

                    if correct_points == 3:
                        flag = True
                        print("You won")
                        break

                else:
                    print("Try again!")
                    continue

        else:
            print("Try again!")
            continue

game()

