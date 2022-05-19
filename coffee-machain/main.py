
print("start")
menu = {
    'espresso': {
        'ingredients': {
            'water': 50,
            'coffee': 18,
        },
        'cost': 1.5,
    },
    'latte': {
        'ingredients': {
            'water': 200,
            'milk': 150,
            'coffee': 24,
        },
        'cost': 2.5,
    },
    'cappuccino': {
        'ingredients': {
            'water': 250,
            'milk': 100,
            'coffee': 24,
        },
        'cost': 3.0,
    },
}
resources = {
    'water': 3000,
    'milk': 400,
    'coffee': 250,
}


def check_resources(customer_order):
    """ check resource is enough for make a cup of coffee"""
    for i in resources:
        if resources[i] <= customer_order[i]:
            return False

    return True


def check_price(price):
    """ check customer money is enough for buy a cup of coffee"""
    t_coin = int(input("how many 0.25 coins:  ")) * 0.25
    f_coin = int(input("how many 0.5 coins:  ")) * 0.5
    o_coin = int(input("how many 0.1 coins:  ")) * 0.1
    customer_money = t_coin + f_coin + o_coin
    print(f'sum is {customer_money}')
    if price <= customer_money:
        print(f"your money is {customer_money} . price is {price}")
        print(f"get your change: {customer_money - price}")
        return True
    else:
        return False


def make_coffee(ingredients):
    print('make coffee')
    for i in resources:
        resources[i] -= ingredients[i]


def recharge():
    global resources
    resources = {
        'water': 3000,
        'milk': 400,
        'coffee': 250,
    }

is_finish = False
while not is_finish:
    choose = input(" choose one of menu item.(espresso/latte/cappuccino): ").lower()
    order = menu[choose]
    print(order['ingredients'])
    is_enough = check_resources(order['ingredients'])
    if is_enough:
        enough_money = check_price(order['cost'])
        if enough_money:
            make_coffee(order["ingredients"])
            print(resources)
        else:
            print('you do not hove enough money')
    else:
        print("sorry. there is no enough resources.")
    answer = input("'n' to exit: ")
    if answer == 'n':
        is_finish = True
    elif answer == 'off':
        recharge()
    print(f"is enough {is_enough}")
