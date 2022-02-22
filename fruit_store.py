apple_price = 20
apple_quantity = 100
orange_price = 10
orange_quantity = 120
pineapple_price = 40
pineapple_quantity = 80
grape_price = 80
grape_quantity = 95
banana_price = 25
banana_quantity = 50

choice = ''
fruit_choice = ''
quantity_choice = 0
money = 500


def display_menu():
    print("[1] (" + str(apple_quantity) + ")pcs. Apple(/s) = P20\n"
          "[2] (" + str(orange_quantity) + ")pcs. Orange(/s) = P10\n"
          "[3] (" + str(pineapple_quantity) +
          ")pcs.  Pineapple(/s) = P40 \n"
          "[4] (" + str(grape_quantity) + ")pcs.  Grape(/s) = P80 \n"
          "[5] (" + str(banana_quantity) + ")pcs.  Banana(/s) = P25")


def apple():
    global apple_quantity
    global money

    if apple_quantity > 0:
        if(money < apple_price):
            print("You don't have enough money! Try another fruits!")
        else:
            print("How many apples do you want?")
            quantity_choice = int(input())
            while (apple_quantity - quantity_choice) < 0:
                print("Insufficient stocks! Try another quantity!")
                quantity_choice = int(input())
            if (money - (apple_price * quantity_choice)) < 0:
                print("Not enough money!")
            else:
                money -= apple_price * quantity_choice
                apple_quantity -= quantity_choice
                print("\nThank you for purchasing!")
                print("Your current money is now P"+str(money)+"")
    else:
        print("Out of stock!")


def orange():
    global orange_quantity
    global money

    if orange_quantity > 0:
        if (money < orange_price):
            print("You don't have enough money! Try another fruits!")
        else:
            print("How many oranges do you want?")
            quantity_choice = int(input())
            while (orange_quantity - quantity_choice) < 0:
                print("Insufficient stocks! Try another quantity!")
                quantity_choice = int(input())
            if (money - (orange_price * quantity_choice)) < 0:
                print("Not enough money!")
            else:
                money -= orange_price * quantity_choice
                orange_quantity -= quantity_choice
                print("\nThank you for purchasing!")
                print("Your current money is now P"+str(money)+"")
    else:
        print("Out of stock!")


def pineapple():
    global pineapple_quantity
    global money

    if pineapple_quantity > 0:
        if (money < pineapple_price):
            print("You don't have enough money! Try another fruits!")
        else:
            print("How many pineapples do you want?")
            quantity_choice = int(input())
            while (pineapple_quantity - quantity_choice) < 0:
                print("Insufficient stocks! Try another quantity!")
                quantity_choice = int(input())
            if (money - (pineapple_price * quantity_choice)) < 0:
                print("Not enough money!")
            else:
                money -= pineapple_price * quantity_choice
                pineapple_quantity -= quantity_choice
                print("\nThank you for purchasing!")
                print("Your current money is now P"+str(money)+"")
    else:
        print("Out of stock!")


def grape():
    global grape_quantity
    global money

    if grape_quantity > 0:
        if (money < grape_price):
            print("You don't have enough money! Try another fruits!")
        else:
            print("How many grapes do you want?")
            quantity_choice = int(input())
            while (grape_quantity - quantity_choice) < 0:
                print("Insufficient stocks! Try another quantity!")
                quantity_choice = int(input())
            if (money - (grape_price * quantity_choice)) < 0:
                print("Not enough money!")
            else:
                money -= grape_price * quantity_choice
                grape_quantity -= quantity_choice
                print("\nThank you for purchasing!")
                print("Your current money is now P"+str(money)+"")
    else:
        print("Out of stock!")


def banana():
    global banana_quantity
    global money

    if banana_quantity > 0:
        if (money < banana_price):
            print("You don't have enough money! Try another fruits!")
        else:
            print("How many bananas do you want?")
            quantity_choice = int(input())
            while (banana_quantity - quantity_choice) < 0:
                print("Insufficient stocks! Try another quantity!")
                quantity_choice = int(input())
            if (money - (banana_price * quantity_choice)) < 0:
                print("Not enough money!")
            else:
                money -= banana_price * quantity_choice
                banana_quantity -= quantity_choice
                print("\nThank you for purchasing!")
                print("Your current money is now P"+str(money)+"")
    else:
        print("Out of stock!")


while choice != '3':
    print("\nWelcome to the fruit shop!")
    print("[1] Order\n[2] Show List\n[3] No Thanks")
    print("What will you do?")
    choice = input()
    if choice == '1':
        if (money > 0):
            display_menu()
            print("[6] No thanks!")

            print("\nYour current money is P"+str(money)+"")
            print("What you would like to order?")
            fruit_choice = input()
            if fruit_choice == '1':
                apple()
            elif fruit_choice == '2':
                orange()
            elif fruit_choice == '3':
                pineapple()
            elif fruit_choice == '4':
                grape()
            elif fruit_choice == '5':
                banana()
            else:
                print("Not available in the list!")
        else:
            print("You don't have enough money to order!")

    elif choice == '2':
        display_menu()

    elif choice == '3':
        print("Thank you and come again!")

    else:
        print("Not in the choices!")
