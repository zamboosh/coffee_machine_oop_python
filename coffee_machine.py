class CoffeeMachine:

    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.paper_cups = 9
        self.money = 550
        self.interact()

    def __str__(self):
        return f"""
The coffee machine has:
{self.water} of water
{self.milk} of milk
{self.beans} of coffee beans
{self.paper_cups} of disposable cups
${self.money} of money\n"""

    def interact(self):
        while True:
            action = str(input('Write action (buy, fill, take, remaining, exit):\n'))
            if action == 'exit':
                break
            elif action == 'remaining':
                print(self.__str__())
            elif action == 'buy':
                order = input('\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n')

                def make_the_right_coffee(water, milk, beans, money):
                    if self.water >= water and milk >= milk and beans >= beans and self.paper_cups > 0:
                        self.water -= water
                        self.milk -= milk
                        self.beans -= beans
                        self.money += money
                        self.paper_cups -= 1
                        print('I have enough resources, making you a coffee!\n')
                    else:
                        if water > self.water:
                            print('Sorry, not enough water!\n')
                        elif milk > self.milk:
                            print('Sorry, not enough milk!\n')
                        elif beans > self.beans:
                            print('Sorry, not enough beans!\n')
                        elif self.paper_cups <= 0:
                            print('Sorry, not enough cups!\n')

                if order == '1':
                    make_the_right_coffee(250, 0, 16, 4)
                elif order == '2':
                    make_the_right_coffee(350, 75, 20, 7)
                elif order == '3':
                    make_the_right_coffee(200, 100, 12, 6)
            elif action == 'fill':
                self.water += int(input('\nWrite how many ml of water do you want to add:\n'))
                self.milk += int(input('Write how many ml of milk do you want to add:\n'))
                self.beans += int(input('Write how many grams of coffee beans do you want to add:\n'))
                self.paper_cups += int(input('Write how many disposable cups of coffee do you want to add:\n'))
                print()
            elif action == 'take':
                print(f'\nI gave you ${self.money}\n')
                self.money = 0

lavazza = CoffeeMachine()