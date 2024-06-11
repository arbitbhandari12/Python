import read as rd
import operation as op

 
def start():
    """
    This function displays a menu of options for the user to choose from. The options include selling a laptop,
      ordering a laptop, seeing available laptops, and closing the program. If the user chooses to sell a laptop, 
      the `display` function is called to show available laptops and then the 'customerr' and 'purchase' functions are called. 
      If the user chooses to order a laptop, the 'display' function is called to show available laptops and then the 'distributor' and
      'order' functions are called. If the user chooses to see available laptops, the 'display' function is called. If the user 
      chooses to close the program, the 'exit' function is called. If the user enters an invalid input, an error message is displayed
      and the user is prompted again.
    """
    while True:
        print("+--------+-------------+")
        print("| Option | Description |")
        print("+--------+-------------+")
        print("| 1      | Sell        |")
        print("| 2      | Order       |")
        print("| 3      | See Laptops |")
        print("| 4      | Close       |")
        print("+--------+-------------+")
        print()
        #Prompt the user to enter a choice and store it in the variable 'user'
        user = input("- Please Choose The Given Option :")
        #Check which option the user chose and execute the appropriate code block
        if user == "1":
            print()
            print("Here is the list of available laptops:")
            rd.display()#Display the available laptops using a method from the 'rd' module
            print()
            op.customerr()# Prompt the user to enter their details as a customer
            op.purchase()# Allow the user to purchase a laptop using a method from the 'op' module
            print()
            
            
        
        elif user == "2":# Option 2: Order
            rd.display()# Display the available laptops using a method from the 'rd' module
            print()
            op.disstributor()# Prompt the user to enter their details as a distributor
            op.order()# Allow the user to place an order using a method from the 'op' module
           
        
        elif user == "3":# Option 3: See Laptops
            print()
            rd.display() # Display the available laptops using a method from the 'rd' module
            print()
            
        elif user == "4":# Option 4: Close
            exit()# Exit the program
            
        else:# If the user entered an invalid option
            print()
            print("* Please Choose Between 1,2,3 and 4 ")
            print()



start()
op.purchase()



