#Simple banking system in python

balance = 0.0  #initial account balance

def show_balance():
    """Display the current balance"""
    print(f"\nYour current balance is: ${balance: .2f}\n")
    

while True:
    #Ask user for action
    action = input('Choose an action (deposit / withdraw / check / exit): ').strip().lower()
    
    if action == 'deposit':
        try:
            amount = float(input('Enter amount to deposit: '))
            if amount > 0:
                balance += amount
                print(f'Deposited ${amount: .2f} successfully.')
                show_balance()
            else: 
                print('Please enter a positive amount.')
        except ValueError:
            print('Invalid input. Please enter a number.')
        
    elif action == 'withdraw':
        try: 
            amount = float(input('Enter amount to withdraw: '))
            if amount <= 0:
                print('Amount must be greater than Zero!')
            elif amount <= balance:
                balance -= amount
                print(f'Withdraw ${amount: .2f} successfully')
                show_balance()
            else: 
                print("Insufficient Balance")
        except ValueError:
            print('Invalid input. Please enter a number.')
            
    elif action == 'check':
        show_balance()
        
    elif aciton == 'exit':
        print('Thank you for using the banking system.Goodbye!')
        break

    else: 
        print('Invalid choice. please chooce deposit / withdraw / check or exit')
