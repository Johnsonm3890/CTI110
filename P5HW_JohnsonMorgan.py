# Morgan Johnson
# 4/27/2025
# P5LAB
# Program for simple character creation and combat.
import random


def create_character():
    name = input('Enter Characters Name: ') #name of character
    health = int(input(f"Enter {name}'s health: ")) #health of character
    strength = int(input(f"Enter {name}'s strength: ")) #strength of character
    defense = int(input(f"Enter {name}'s defense: ")) #defense of character
    character = {'n': name, 'h': health, 's': strength, 'd': defense} #character card
    return character

def display_characters(characters):

    for char in characters:
        print(f'Name: {char['n']}, Health: {char['h']}, Strength: {char['s']}, Defense: {char['d']}') #print all characters in the list passed.

def attack(atk, defend):

    damage = random.randint(0, atk['s']) + int(atk['s']*0.60) #damage is a fixed 60% of strength plus a random amount from 0 to character strength
    damage_mit = int(defend['d']*0.60) + random.randint(0, defend['d']) #defense is a fixed 60% of defense plus a random amount from 0 to character defense
    atk_dam = damage - damage_mit #attack damage is attack roll minus defense roll

    if atk_dam > 0: #if attack is a value above 0 deal damage, prevents healing on high defense
        defend['h'] -= atk_dam
    else:
        atk_dam = 0 #else do no damage
        pass

    print(f"{atk['n']} is attacking {defend['n']} for {damage}, {defend['n']} blocks {damage_mit} damage." ) #call out the attack
    print(f'Total damage delivered is {atk_dam} points') #call out total damage done

    if defend['h'] > 0: #if character is still alive
        print(f"{defend['n']}'s health is now {defend['h']}") #state new health amount
        return defend['h'] #return health amount to character card
    else: #character died
        print(f'{defend['n']} is dead') #pronuce character dead
        defend['h'] = 0 #set health to 0
        return defend['h'] #return 0 health

def main():

    print(f'Please create your first character.') #game requires a minimum of 2 characters to start
    temp = create_character()
    char_list = [temp]
    print(f'{temp['n']} has been created') #build first character

    while True:
        print(f'Please create your second character.')
        temp = create_character()
        if any(d['n'] == temp['n'] for d in char_list): #if any char in the list has the same name as the one just created, reject the character.
            print(f'Characters can not share names')
            pass
        else:
            char_list.append(temp) #else add the character to the list
            print(f'{temp['n']} has been created')
            break


    while True:

        creation = input("Would you like to create another character? (Y/N)") #prompt the user to generate more than 2 characters if desired
        if creation == "Y":
            while True:

                temp = create_character()
                if any(d['n'] == temp['n'] for d in char_list): #check for names in existing list of character cards, only non-duplicate names permitted
                    print(f'Characters can not share names')
                    pass
                else:
                    char_list.append(temp)
                    print(f'{temp['n']} has been created')
                    break

        elif creation == 'N': #character creation complete
            break
        else:
            print(f'Please enter a valid input') #Y or N only accepted inputs

    while True: #Game over/ Win condition only 1 character left standing Main Game Loop

        if len(char_list) > 1: #check for win condition 1 character left
            pass
        else:
            print(f'{char_list[0]['n']} is the winner!')
            print(f'Thanks for Playing')
            break

        print(f'Please select an action:') #User input, what do they want to do
        print(f'C for creation of another character, D for displaying all characters, A for attacking characters, and Q to quit') #Create additional characters from main loop, display all created characters, have characters attack each other, or quit game
        user_action = input("action: ")



        if user_action == 'C': #create an additional character
            while True:
                temp = create_character()
                if any(d['n'] == temp['n'] for d in char_list): #make sure character name is not already in the list of characters
                    print(f'Characters can not share names')
                    pass
                else:
                    char_list.append(temp)
                    print(f'{temp['n']} has been created')
                    break
        elif user_action == 'D': #display all characters and current stats
            display_characters(char_list) #calls function to print out all character cards
        elif user_action == 'A': #make two characters attack each other

            while True:
                attacker = input(f"Please select an attacker.")
                valid_input = any(d['n'] == attacker for d in char_list) #checks if attacker input is a valid input, That is that the attacker is a character on the list of characters
                if not valid_input:
                    print(f'Attacker does not exist.') #if attacker does not exist
                    pass
                else:
                    break #valid attacker selected
            while True:
                defender = input(f'Please select a defender.')
                valid_input = any(d['n'] == defender for d in char_list) #checks if defender is valid
                if not valid_input:
                    print(f'Defender does not exist.')
                    pass
                else:
                    break

            def_index = char_list.index(next(filter(lambda n: n.get('n') == defender, char_list))) #parsing character list, we need to first filter the dictionaries to find our match character, then use the iterator to figure out how to call the index of said character card in our list of character cards
            atk_index = char_list.index(next(filter(lambda n: n.get('n') == attacker, char_list))) #Filter returns iterator to point to matching character dictionary, next provides the index function the full dictionary we are looking for, index provides the index of the list that this dictionary lives in.

            char_list[def_index]['h'] = attack(char_list[atk_index],char_list[def_index]) # have the characters attack each other. output the new health of the defending character

            if char_list[def_index]['h'] == 0: #if defending character is now dead remove them from the list
                char_list.pop(def_index)
            else:
                pass



        elif user_action == 'Q': #allows user to quit game early
            print("Thanks for Playing")
            break
        else: #any none called for input returns an invalid
            print(f'Invalid Input')

main() #calling main function