# Morgan Johnson
# 4/27/2025
# P5LAB
# Program for self-checkout machine that prompts the amount of changed owed based on amount of money placed in by user.
import random



def main():
    amount_owed = round(random.uniform(0.01, 100.00), 2)

    print(f'You owe ${amount_owed}')
    disperse_change(amount_owed)


def disperse_change(owed):

    while True:

        cash_in = round(float(input('How much cash will you put in the self-checkout? ')),2)
        camount = cash_in - owed


        if camount < 0:
            print ('Insufficient Funds')
            pass
        elif camount == 0:
            print ('No Change')
            break
        else:

            print(f'Change is: ${camount:.2f}')
            print()
            camount_int = int(round(camount * 100))

            dollar_amount = int(camount_int/100)
            camount_int = camount_int-(dollar_amount*100)


            Quarter_amount = int(camount_int/25)
            camount_int = camount_int - (Quarter_amount*25)


            Dime_amount = int(camount_int / 10)
            camount_int = camount_int - (Dime_amount * 10)


            Nickel_amount =int(camount_int / 5)

            camount_int = camount_int - (Nickel_amount * 5)

            Penny_amount = (round(camount_int))


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
            break


main()
