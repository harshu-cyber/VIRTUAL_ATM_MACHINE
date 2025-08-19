def main():
    # Get the input from the user
    pin = int(input("Enter your pin:"))
    bal = 5000
    
    if pin == 112233:
        print("Welcome to the RR ATM")
        print("Your balance is: ", bal)
        print("Enter 1 for Depsoit...")
        print("Enter 2 for Withdrawal...")
        print("Enter 3 for Balance Enquiry...")
        ch = int (input())
        
        if ch == 1:
            # deposit code
            amt = int(input("Enter your Deposit amount:"))
            bal = bal + amt
            print("Your new balance is: ", bal)
            
        elif ch == 2:
            #withdrawl code
            amt = int(input("Enter Your Withdrawl Amount:"))
            if amt <= bal:
                bal = bal - amt
                print("Your available balance  is: ", bal)
            else:
                print("Insufficient balance")
                
        
        elif ch == 3:
            #balance enquiry code
            print("Your balance is: ", bal)
        
        else:
            print("Please enter a valid number....")
            
    else:
        print("Invalid Pin")
            
if __name__ == "__main__":
    main()
                
            
    
        