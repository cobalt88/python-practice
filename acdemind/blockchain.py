# Initializing our (empty) blockchain list
blockchain = []


def get_last_blockchain_value():
    """ Returns the last value of the current blockchain. """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]

# This function accepts two arguments.
# One required one (transaction_amount) and one optional one (last_transaction)
# The optional one is optional because it has a default value => [1]


def add_transaction(transaction_amount, last_transaction=[1]):
    """ Append a new value as well as the last blockchain value to the blockchain.

    Arguments:
        :transaction_amount: The amount that should be added.
        :last_transaction: The last blockchain transaction (default [1]).
    """
    if last_transaction == None:
        last_transaction = [1]
    blockchain.append([last_transaction, transaction_amount])


def get_transaction_value():
    """ Returns the input of the user (a new transaction amount) as a float. """
    # Get the user input, transform it from a string to a float and store it in user_input
    user_input = float(input('Enter transaction amount: '))
    return user_input

def get_user_choice():
    user_input = input('Your choice: ')
    return user_input

def print_blockchain_elements():
    for block in blockchain:
        print('outputting block')
        print(block)

#this function will check the validity of the blockchain by comparing the current first element of the current chain against the entirety of the previous block. 
def verify_chain():
    block_index = 0
    is_valid = True

    for block in blockchain:
        if block_index == 0:
            block_index += 1
            continue
        elif block[0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False
            break
        block_index += 1
    return is_valid

# Get the first transaction input and add the value to the blockchain
tx_amount = get_transaction_value()
add_transaction(tx_amount)

# user interface loop, while true the user is prompted to input either a new transaction value or print out the current blockchain 
while True:
    #options for the user
    print('Please Choose an option from below: \n')
    print('1: Add a new transaction value')
    print('2: Output current blockchain')
    print('3: Edit or manipulate the blockchain')
    print('0: Exit \n')

    #function to record input from the user
    user_choice = get_user_choice()
    #conditional statement for user interface questions
    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_transaction(tx_amount, get_last_blockchain_value())
    elif user_choice == '2':
        print_blockchain_elements()
    elif user_choice == '3':
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_choice == '0':
        print('Thank you for using Blockchain.py!')
        break
    else: 
        print('Invalid input. Please choose an option from the list.')
    # verify the chain
    if not verify_chain():
        print('Invalid blockchain!')
        break
        
    
    # Output the blockchain list to the console
    
print('Done!')
