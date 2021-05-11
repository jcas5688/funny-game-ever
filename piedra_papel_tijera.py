import random 
# usuario advina el numero 
def guess(x):

    randon_number= random.randint(1,x)
    guess = 0
    while guess != randon_number:
        guess = int(input('adivina el numero: '))
        if guess > randon_number:
            print('tu numero es muy alto')
        elif guess < randon_number:
            print('tu numero es muy bajo')
    print(f"Excelente adivinaste el numero correcto el cual era {randon_number}")

# pc advina el numero 

def pc_guess(x):
    low= 1
    high= x
    feedback = ''
    
    while feedback != 'c':
        if low != high:
            randon = random.randint(low, high)
        else:
            randon = low
        feedback = input(f" Is {randon} to high (H) or too low (L) or is is correct (C): ").lower()
        if feedback == 'h':
            high = randon - 1
        elif feedback == 'l':
            low = randon + 1
    print("the pc has guess our number correctly")


# piedra papel o tijera 

def play():
    user = input ('Que eliges?, Piedra (R), Papel (P), Tijera (T): ').lower()
    pc = random.choice(['r', 'p', 't'])
    if user == pc:
        return 'Its a tie' 
    
    if fuct(user, pc):
        return 'you win!'
    
    return 'you lost!'



def fuct(player, oponent):

    if (player == 'r' and oponent == 't') or (player == 't' and oponent == 'p') or (player == 'p' and oponent == 'r'):
        return True



print (play())