# Morgan Johnson
# 3/21/2025
# P3LAB
# Program to enter money amount as a float and convert money entered into exact change.


Money_amount = int(100 * float(input('Enter the amount of money as a float: $')))

if Money_amount <= 0:
    print ('No change')
else:

    dollar_amount = int(Money_amount//100)
    Money_amount = Money_amount-(dollar_amount*100)

    Quarter_amount = int(Money_amount//25)
    Money_amount = Money_amount - (Quarter_amount*25)

    Dime_amount = int(Money_amount // 10)
    Money_amount = Money_amount - (Dime_amount * 10)

    Nickel_amount =int(Money_amount // 5)
    Money_amount = Money_amount - (Nickel_amount * 5)

    Penny_amount = int(Money_amount // 1)
    Money_amount = Money_amount - (Penny_amount * 1)

    if dollar_amount == 1:
        print('1 Dollar')
    elif dollar_amount > 1:
        print(f"{dollar_amount} Dollars")
    else:
        pass

    if Quarter_amount == 1:
        print('1 Quarter')
    elif Quarter_amount > 1:
        print(f"{Quarter_amount} Quarters")
    else:
        pass

    if Dime_amount == 1:
        print('1 Dime')
    elif Dime_amount > 1:
        print(f"{Dime_amount} Dimes")
    else:
        pass

    if Nickel_amount == 1:
        print('1 Nickel')
    elif Nickel_amount > 1:
        print(f"{Nickel_amount} Nickels")
    else:
        pass

    if Penny_amount == 1:
        print('1 Penny')
    elif Penny_amount > 1:
        print(f"{Penny_amount} Pennies")
    else:
        pass
