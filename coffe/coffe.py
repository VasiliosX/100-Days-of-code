from coffe_data import MENU,resources

cont=True
total_money=0
while cont:
    enough=True

    order=input('What would you like? (espresso/latte/cappuccino):')
    if order=='report':
        print(f'Water:{resources["water"]}ml\nMilk:{resources["milk"]}ml\nCoffee:{resources["coffee"]}g')
        print(f'Money:${total_money}')




    if order!='report':
        rem_water = resources['water'] - MENU[order]['ingredients']['water']
        rem_coffee = resources['coffee'] - MENU[order]['ingredients']['coffee']
        if order != 'espresso':
            rem_milk = resources['milk'] - MENU[order]['ingredients']['milk']

            make = True
        if rem_coffee<0:
            print('Sorry, not enough coffee')
            enough=False

        elif rem_milk<0 and order!='espresso':
            print('Sorry, not enough milk')
            enough=False

        elif rem_water < 0:
            print('Sorry, not enough water')
            enough = False
        if enough==True:
            print('Please insert coins')
            quarters=int(input('How may quarters?:'))
            dimes=int(input('How may dimes?:'))
            nickels=int(input('How many nickels?:'))
            pennies=int(input('How many pennies?'))


            total=0.25*quarters+0.1*dimes+nickels*0.05+pennies*0.01

            rest = total - MENU[order]['cost']

            if rest<0:
                print('Sorry, not enough money, money refunded')
                make=False





            if make:
                print(f'Here is ${rest} in change')
                print(f'Here is your {order}')
                resources['water']=rem_water
                resources['coffee']=rem_coffee
                total_money=total-rest
                if order!='espresso':
                 resources['milk']=rem_milk



