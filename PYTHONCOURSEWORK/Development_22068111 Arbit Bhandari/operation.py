import read as rd
import write as wr

def laptopstock():
    """
    This function allows the user to sell laptops. The user is prompted to enter whether they 
    want to sell another laptop or not. If the user enters 'y', the function displays available
      laptops and calls the purchase function. If the user enters 'n', the function exits. If the user
        enters an invalid input, an error message is displayed and the user is prompted again.
    """
    while True:
        print()
        another_laptop = input("- Do you want to sell other laptops if yes then press 'y' if no then press 'n' : ")
        print()
        if another_laptop.lower() == "y":
            rd.display()
            print()
            purchase()
            
            break
        elif another_laptop.lower() == "n":
            break
        else:
            print("Invalid input. Please enter 'y' to continue or 'n' to exit.")
            print()


 


laptopname=""
quantity=""
customer_=""
current_time=""
brand_sell=""
processor_=""
graphic_=""
price_=""
netamount=""
total=""
purchase_list=[]
sell_list=[]
money=[]
ship_total=[]
shippingmoney=[] 
def customerr():
    """
    This function prompts the user to enter a customer name and stores it in the global variable `customer_`. 
    The function checks if the entered name is valid (i.e., contains only alphabetic characters). If the name is valid,
      the function exits. If the name is not valid or if it is an empty string, an error message is displayed and the user
        is prompted again.
    """

    global customer_
    while True:
            customer_name = input("- Enter the customer name: ")
            customer_=customer_name
            # check if the customer name contains only alphabetic characters
            if customer_name.replace(" ", "").isalpha():
                print()
                break
            elif customer_name == "":
                print("\n* You can't continue without typing customer.")
                print()
            elif customer_name.isdigit():
                print()
                print("* Please enter customer name correctly")
                print()
            else:
                print()
                print("* Please enter customer name correctly")
                print()
                



def purchase():
    """
    This function prompts the user to enter the name of the laptop they want to sell and stores it in the global variable `laptopname`. The function checks if the entered laptop name is valid (i.e., not a digit, not an empty string, and available in the store). If the laptop name is valid, the function exits. If the laptop name is not valid, an error message is displayed and the user is prompted again.
    """
    global laptopname
    while True:
        laptop_name = input("- Enter the name of the laptop you want to sell: ").lower().strip()
        laptopname=laptop_name
        # check if the entered laptop name is valid
        if laptop_name.isdigit():
            print("\n* Invalid input. Please enter the name of the laptop.\n")
        elif laptop_name == "":
            print("\n* Laptop name can't be empty.\n")
        elif laptop_name not in [b[0].lower() for b in rd.products]:
            print("\n* This laptop is not available in our store.\n")
            print("* Here are the available laptops:")
            print()
            for a in rd.products:
                print(a[0])
            print()
        else:
            break

    check = True
    while check:
        global quantity
        print()
        quantity_required = input("- Enter the required quantity of the laptop: ")
        quantity=quantity_required
        # check if the entered quantity is valid
        if quantity_required.isalpha():
            print("\n* Invalid input. Quantity must be a number.")
            continue
        try:
            quantity_required = int(quantity_required)
        except:
            print("\n* Invalid input. Quantity must be a number.")
            continue
        for i in rd.products:
            for j in i:
                if laptop_name.lower() == j.lower():
                    if quantity_required > int(i[3]):
                        print("\n* We have",i[3]," Laptops right now")
                        print()
                        print("- Here is the list of available laptops with there quantity")
                        rd.display()
                        laptopstock()
                        check=False
                        break
                    elif quantity_required <= 0:
                        print("\n* You need to sell at least 1 laptop.")
                    else:
                        check = False
                        break

    # calculate the total cost for the laptops
    global total_amount_last                   
    total_amount_last = 0
    global withoutshipping
    withoutshipping=0 
    global total_shipping_cost
    total_shipping_cost=0
    # iterate through the list of products
    for a in rd.products:
        # check if the product matches the laptop name and required quantity is available
        if laptop_name in a[0].lower():
            if int(a[3]) >= quantity_required:
                # extract product details
                global brand_sell
                brand_name = a[1]
                brand_sell=brand_name
                global processor_
                processor = a[4]
                processor_=processor
                global graphic_
                graphic = a[5]
                graphic_=graphic
                global price_
                price = int(a[2].replace("$", ""))
                price_=price
                global netamount
                net_amount = quantity_required * price
                netamount=net_amount
                global shipping_cost
                shipping_cost = 50*quantity_required
                # calculate total amount and append to money list
                global total
                total_amount = net_amount + shipping_cost
                total=total_amount
                global current_time
                currenttime=rd.datetime.datetime.now()
                current_time=currenttime
                money.append(total)
                for total in money:
                    total_amount_last=total_amount_last+total
                # calculate total amount without shipping and append to shippingmoney list
                wr.withdraw()
                shippingmoney.append(netamount)
                # calculate total shipping cost and append to ship_total list
                for shipping in shippingmoney:
                    withoutshipping=withoutshipping+shipping
                ship_total.append(shipping_cost)
                for shipped in ship_total:
                    total_shipping_cost=total_shipping_cost+shipped
                
                 


                
                while True:
                    print()
                    user_input = input("Do you want to sell more laptop if yes then enter 'y' if no then enter'n' (y/n): ")
                    if user_input.lower() == "y":
                            # Call purchase function and break out of loop
                            print()
                            rd.display()
                            print()
                            purchase_list.append(f"|{laptopname:18s}|   {brand_sell:11s} |   ${price:<10}| {quantity:^12} |  {processor_:15s}|   {graphic_:7s}   |")
                            sell_list.append(f"\t\t\t\t\t\t|{laptopname:16s}|   {brand_sell:11s} |   ${price:<10}| {quantity:^12} |  {processor_:15s}|   {graphic_:7s}     |\n")
                            # Call purchase function and break out of loop
                            purchase()
                            break
                    elif user_input.lower() == "n":
                        # Calculate and display shipping details, clear lists, and exit loop
                        ship()
                        print()
                        purchase_list.clear()
                        sell_list.clear()
                        shippingmoney.clear()
                        ship_total.clear()
                        money.clear()
                        break
                    else:
                        # Display error message for invalid input and continue loop
                        print("Invalid input. Please enter 'y' to continue or 'n' to exit.")

def ship():
    """
    This function prompts the user to enter whether they want to ship their laptop or not. 
    If the user enters 'y', the `withship` function is called and then the `bill` function is called.
      If the user enters 'n', the `shipbill` function is called and then the `withoutorderbill` function is called. 
      If the user enters an invalid input, an error message is displayed and the user is prompted again.
    """
    while True:
        print()
        # prompt the user to select whether they want to ship their laptop or not
        shipp = input("Do you want to ship your laptop if yes then enter 'y' if you don't want to ship press 'n': ")
        if shipp.lower() == "y":
            # if the user selects 'y', call the function to print bill with shipping charges
            wr.withship() 
            bill()
            break
        elif shipp.lower() == "n":
            # if the user selects 'n', call the function to print bill without shipping charges and order details
            shipbill()
            wr.withoutorderbill()
            break
        else:
            print("Invalid input. Please enter 'y' to ship or 'n' if you don't want to ship.")
              
def bill():#bill that generate if customer want to ship there laptop
    """
    This function generates and displays a bill for the user's purchase if they want to ship. 
    The bill includes the customer name, date of sell, purchase details
      (laptop name, brand, price, quantity, processor, and graphic), total amount, and total shipping cost. 
      The function also displays a thank you message to the customer.
    """
    print()
    print("Order complete! Your new laptop will be delivered to you soon.")
    print()
    print("Note: The grand total, including the shipping cost")
    print()
    print("|--------------------------------------------------------------------------------------------------|")
    print("| \t\t\t\t  Arbit laptop Shop                                                |")
    print("| \t\t\t\t  Kavresthali, Kathmandu                                           |")
    print("| \t\t\t\t  Phone: 9863935190, 9881224111                                    |")
    print("|--------------------------------------------------------------------------------------------------|")
    customer = f"|{'Customer Name: ' + customer_:40s} \t\t\t\t\t                   |"
    print(customer)
    print("|                                                      " + "Date of Sell: " + str(current_time) + "    |")
    print("|--------------------------------------------------------------------------------------------------|")
    purchase_details = f"|{'Laptops':18s}|    {'Brand':11s}|   {'Price':10s} |  {'Quantity':12s}|  {'Processor':15s}|   {'Graphic':7s}     |"
    print(purchase_details)
    print("|--------------------------------------------------------------------------------------------------|")
    after_purchase = f"|{laptopname:18s}|   {brand_sell:11s} |   ${price_:<9} | {quantity:^12} |  {processor_:15s}|   {graphic_:7s}   |"
    print(after_purchase)
    print("|--------------------------------------------------------------------------------------------------|")
    for purchase_item in purchase_list:
        print(purchase_item)
        print("|--------------------------------------------------------------------------------------------------|")
    total_sell = f"|{'Total Amount : $' + str(total_amount_last):40s} {'Total Shipping Cost :$'+str(total_shipping_cost):9s} \t\t\t\t   |"
    
    print(total_sell)
    print("|--------------------------------------------------------------------------------------------------|")
    print("|                                                                                                  |")
    print("|***************************Thank You For Giving Us Chance to Serve you****************************|")
    print("|                                                                                                  |")
    print("|--------------------------------------------------------------------------------------------------|")

def shipbill():#bill that generate if customer do not want to ship there laptop
    """
    This function generates and displays a bill for the user's purchase if they don't want to ship.
      The bill includes the customer name, date of sell, purchase details 
      (laptop name, brand, price, quantity, processor, and graphic), and total amount (excluding shipping cost). 
      The function also displays a thank you message to the customer.
    """
    print()
    print("Order complete! Your new laptop will be delivered to you soon.")
    print()
    print("Note: The grand total, doesn't include shipping cost the shipping cost")
    print()
    print("|--------------------------------------------------------------------------------------------------|")
    print("| \t\t\t\t  Arbit laptop Shop                                                |")
    print("| \t\t\t\t  Kavresthali, Kathmandu                                           |")
    print("| \t\t\t\t  Phone: 9863935190, 9881224111                                    |")
    print("|--------------------------------------------------------------------------------------------------|")
    customer = f"|{'Customer Name: ' + customer_:40s} \t\t\t\t\t                   |"
    print(customer)
    print("|                                                      " + "Date of Sell: " + str(current_time) + "    |")
    print("|--------------------------------------------------------------------------------------------------|")
    purchase_details = f"|{'Laptops':18s}|    {'Brand':11s}|   {'Price':10s} |  {'Quantity':12s}|  {'Processor':15s}|   {'Graphic':7s}     |"
    print(purchase_details)
    print("|--------------------------------------------------------------------------------------------------|")
    after_purchase = f"|{laptopname:18s}|   {brand_sell:11s} |   ${price_:<9} | {quantity:^12} |  {processor_:15s}|   {graphic_:7s}   |"
    print(after_purchase)
    print("|--------------------------------------------------------------------------------------------------|")
    for purchase_item in purchase_list:
        print(purchase_item)
        print("|--------------------------------------------------------------------------------------------------|")
    total_sell = f"|{'Total Amount : $' + str(withoutshipping):40s} \t\t\t\t\t                   |"
    print(total_sell)
    print("|--------------------------------------------------------------------------------------------------|")
    print("|                                                                                                  |")
    print("|***************************Thank You For Giving Us Chance to Serve you****************************|")
    print("|                                                                                                  |")
    print("|--------------------------------------------------------------------------------------------------|")




money_order=[] 
vatno=[]                       
distributor_=""          
def disstributor():
    """
    This function prompts the user to enter the name of a distributor (company) and stores it in the global variable
      'distributor_'. The function checks if the entered distributor name is valid 
      (i.e., contains only alphabetic characters and is not an empty string).
        If the distributor name is valid, the function exits. If the distributor name is not valid or if an exception occurs, 
        an error message is displayed and the user is prompted again.
    """
    while True:
        global distributor_  # global variable declaration
        try:
            distributor = input("- Enter the name of distributor (Company): ")
            distributor_=distributor
            if distributor.isalpha(): # check if distributor name is alphabetic
                print()
                break
            elif distributor =="": # check if distributor name is empty
                print()
                print("* Distributor name can't be Empty")
            elif int(distributor): # check if distributor name contains only numeric characters
                print()
                print("* Distributor name can't be number")
            else:
                print()
                print("* Enter distributor name correctly")
                print()
        except:
            print()
            break 
        print()                            

orderlaptop=""
brand_order=""
processor_order=""
graphic_order=""
quantity_order=""
total_order=""
order_list=[]
sell_order_list=[]

def order():
    """
    This function prompts the user to enter the name of the laptop they want to order and stores it in the global variable
      'orderlaptop'. The function checks if the entered laptop name is valid 
      (i.e., contains at least one alphabetic character and is not an empty string). 
      If the laptop name is valid, the function exits. If the laptop name is not valid or 
      if an exception occurs, an error message is displayed and the user is prompted again.
    """
    while True:
        global orderlaptop # declaring global variable
        try:
            # prompt the user to enter the name of the laptop
            order_laptop = input("- Enter the name of the laptop you want to order: ").lower().strip()
            orderlaptop=order_laptop
            print()
            # check if the entered name contains only alphabetic characters
            if any(char.isalpha() for char in order_laptop):
                break # exit the loop if the name is valid
            elif order_laptop == "":
                print("* Please enter laptop name.") # display an error message if the name is empty
            elif int(order_laptop):
                print("* Laptop name can't be number") # display an error message if the name contains a number
            else:
                print("* Enter Laptop name correctly") # display an error message if the name is invalid
  
        except:
           print("* Enter Laptop name correctly")# display an error message if an exception occurs
        print()


    while True:
        global brand_order
        try:
            # Prompt user to enter brand name of the laptop they want to order
            brand_name = input("- Enter the brand of laptop: ").strip()
            brand_order=brand_name
            print()
            # Check if brand name contains only alphabetic characters
            if any(char.isalpha() for char in brand_order):
                break
            # Check if brand name is empty
            elif brand_name == "":
                print("* Please enter brand name")
                print()
            else:
                print("Plesae enter Brand name correctly")
                print()
        except:
            print("Enter brand name correctly")
            print()

            
    while True:
        global processor_order
        try:
            # Prompt user to enter processor name and store it in 'processor'
            processor = input("- Enter the Processor of laptop: ").strip()
            processor_order=processor
            print()
            # Check if processor name contains only alphabetic characters
            if any(char.isalpha() for char in processor):
                break
            # Check if processor name is an empty string
            elif processor=="":
                print("* Please enter processor name")
                print()
            # If processor name is not valid, display an error message and prompt user again
            else:
                print("* Please enter processor name correctly")
                print()
        except:
           print("* Please enter processor name correctly")
           print()


    while True:
        global graphic_order
        try:
            # Prompt user to enter the graphics name and store it in the 'graphics' variable
            graphics = input("- Enter the graphic of laptop: ").strip()
            graphic_order=graphics
            print()
            # Check if the entered graphics name is valid, if yes break the loop.
            if any(char.isalpha() for char in graphics):
                break
            # Check if the entered graphics name is empty, if yes display an error message.
            elif graphics=="":
                print("* Enter graphic name correctly")
                print()
            # Display an error message if the entered graphics name contains digits or special characters.
            else:
                print("* Enter graphic name correctly")
                print()
        except:
            break


    while True:
        global quantity_order
        try:
            # Prompt user to enter the required quantity of the laptop
            quantity_required =int(input("- Enter the required quantity of the laptop: "))
            quantity_order=quantity_required
            print()
            # Check if the entered quantity is valid (i.e. greater than 0)
            if int(quantity_required) <=0:
                print("* Invalid input. Quantity must be at least 1.")
                print()
            else:
                break
        except:
            print()
            print("* Enter required quantity correctly")
            print()

    while True:
        global net_amount_order
        try:
         # Prompt the user to enter the net amount of the laptop and store it in the global variable 'net_amount_order'   
         net_amount = int(input("- Enter the net amount of the laptop: "))
         net_amount_order=net_amount
         print()

         # Check if the net amount entered is a valid value (greater than 0)
         if net_amount <= 0:
            print("* Invalid input. Net amount must be at least 0.")
            print()

         # If the net amount entered is valid, exit the loop
         else:
            break

        except :
          print()
          print("* Enter a valid net amount.")
          print()

    '''Calculate vat amount total amount without vat total amount with vat'''
    global total_order_last                   
    total_order_last = 0   
    global novatt
    novatt=0 
    global vat
    vat_amount = int(net_amount*13/100)
    vat=vat_amount
    global total_order
    total_amount = net_amount+vat_amount
    total_order=total_amount
    total_order_final=total_order*quantity_required
    global current_time
    currenttime=rd.datetime.datetime.now()
    current_time=currenttime
    global withvatt
    withvatt=net_amount*quantity_order
    withnovat=net_amount*quantity_required
    money_order.append(total_order_final)
    for total in money_order:
        total_order_last=total_order_last+total
    wr.invorder()
    vatno.append(withnovat)
    for currentvat in vatno:
        novatt=novatt+currentvat
        
    while True:
        print()
        user_input = input("Do you want to continue order laptop if yes enter 'y' in no enter 'n' (y/n): ")
        if user_input.lower() == "y": 
            print()
            rd.display()
            print()
            order_list.append(f"|{orderlaptop:16s}|    {brand_order:11s}|   ${net_amount:<9} | {quantity_order:^12} |  {processor_order:15s}|   {graphic_order:14s}|")
            sell_order_list.append(f"\t\t\t\t\t\t|{order_laptop:16s}| {brand_order:^11s}   |   ${int(total_order):<10}| {quantity_order:^12} |  {processor_order:15s}|   {graphic_order:14s}|\n")
            order()
            break
        elif user_input.lower() == "n":
            wr.order_invoice()
            print()
            orderbill()
            order_list.clear()
            sell_order_list.clear()
            money_order.clear()
            vatno.clear()
            
            break
        else:
            print("Invalid input. Please enter 'y' to continue or 'n' to exit.")





def orderbill():
    """
    This function generates and displays a bill for the user's order. 
    The bill includes the distributor name, date of sell, order details (laptop name, brand, price, quantity, processor, and graphic),
    total amount with VAT, and total amount without VAT. The function also displays a thank you message to the customer.
    """
    print()
    print("Order complete! Your new laptop will be delivered to you soon.")
    print()
    print("Note: The grand total, includes the vat amount")
    print()
    print("|--------------------------------------------------------------------------------------------------|")
    print("| \t\t\t\t  Arbit laptop Shop                                                |")
    print("| \t\t\t\t  Kavresthali, Kathmandu                                           |")
    print("| \t\t\t\t  Phone: 9863935190, 9881224111                                    |")
    print("|--------------------------------------------------------------------------------------------------|")
    distributor_order = f"|{'Customer Name: ' + distributor_:40s} \t\t\t\t\t                   |"
    print(distributor_order)
    print("|                                                      " + "Date of Sell: " + str(current_time) + "    |")
    print("|--------------------------------------------------------------------------------------------------|")
    order_details = f"|{'Laptops':16s}|    {'Brand':11s}|   {'Price':10s} |  {'Quantity':12s}|  {'Processor':15s}|   {'Graphic':7s}       |"
    print(order_details)
    print("|--------------------------------------------------------------------------------------------------|")
    after_order = f"|{orderlaptop:16s}|    {brand_order:11s}|   ${net_amount_order:<9} |  {quantity_order:^12}|  {processor_order:15s}|   {graphic_order:14}|"
    print(after_order)
    print("|--------------------------------------------------------------------------------------------------|")
    for order_item in order_list:
        print(order_item)
        print("|--------------------------------------------------------------------------------------------------|")
    total_order_ok = f"|{'Total Amount With Vat : $' + str(total_order_last):40s} {'Total Amount without Vat : $' + str(novatt):40s}      \t   |"
    print(total_order_ok)
    print("|--------------------------------------------------------------------------------------------------|")
    print("|                                                                                                  |")
    print("|***************************Thank You For Giving Us Chance to Serve you****************************|")
    print("|                                                                                                  |")
    print("|--------------------------------------------------------------------------------------------------|")


                        
    
        
    
    ''' Update the list of products by reading the contents of the product file and appending each line as a new item in the list.
    This will reflect any changes in the purchase or sell quantities of laptops.'''
    rd.products=[]
    with open(rd.product)as f:
        for line in f:
            line=line.strip().split(",")
            rd.products.append(line)

