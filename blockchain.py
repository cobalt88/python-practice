blockchain = [[1]]

def get_last_block_value():
  return blockchain[-1]

def add_value(transaction_amount, last_transaction=[1]):
  blockchain.append([last_transaction, transaction_amount])

def get_user_input():
  return float(input("Your transaction amount please:"))

tx_amount=get_user_input()
add_value(tx_amount)

tx_amount=get_user_input()
add_value(last_transaction=get_last_block_value(), transaction_amount=9)

tx_amount=get_user_input()
add_value(tx_amount) 

print (blockchain)