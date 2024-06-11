import operation as op
import read as rd



'''This is the invoice bill  after selling laptops if user sell laptop it will make invoice in a folder with customer name it wite the details of laptops like laptop name, brand name,
    processor name, quantity, graphics and total amount with shipping and total amount without shipping cost'''
def withship():
    """
    This function generates a bill for the user's purchase and saves it to a text file. 
    The bill includes the customer name, date of sell, purchase details (laptop name, brand, price, quantity, processor, and graphic),
      total amount, and total shipping cost. The function also displays a thank you message to the customer. 
      The bill is saved to a text file in the `Invoice_Sell` directory with the filename being the customer's name.
    """
    filepath =r"Invoice_Sell\\" + op.customer_ + ".txt"
    with open(filepath, 'a') as w:
        if w.tell() == 0:
            w.write("\t\t\t\t\t\t|--------------------------------------------------------------------------------------------------|\n")
            w.write("\t\t\t\t\t\t| \t\t\t\t  Arbit laptop Shop                                                        |\n")
            w.write("\t\t\t\t\t\t| \t\t\t\t  Kavresthali,Kathmandu                                                    |\n")
            w.write("\t\t\t\t\t\t| \t\t\t\t  Phone:9863935190,9881224111                                              |\n")
            w.write("\t\t\t\t\t\t|--------------------------------------------------------------------------------------------------|\n")
            customer=f"\t\t\t\t\t\t|{'Customer Name :'+op.customer_:40s} \t\t\t\t\t                           |\n"
            w.write(customer)
            w.write("\t\t\t\t\t\t|                                                      "+"Date of Sell:"+str(op.current_time)+"     |\n")
            w.write("\t\t\t\t\t\t|--------------------------------------------------------------------------------------------------|\n")                                                                                                            
            header = f"\t\t\t\t\t\t|{'Laptops':16s}|    {'Brand':11s}|   {'Price':10s} |  {'Quantity':12s}|  {'Processor':15s}|   {'Graphic':7s}       |\n"
            w.write(header)
            w.write("\t\t\t\t\t\t|--------------------------------------------------------------------------------------------------|\n")
        after_purchase = f"\t\t\t\t\t\t|{op.laptopname:16s}|   {op.brand_sell:11s} |   ${op.price_:<10}| {op.quantity:^12} |  {op.processor_:15s}|   {op.graphic_:7s}     |\n"
        w.write(after_purchase)
        w.write("\t\t\t\t\t\t|--------------------------------------------------------------------------------------------------|\n")
        for sell_item in op.sell_list:
                    w.write(sell_item)
                    w.write("\t\t\t\t\t\t|--------------------------------------------------------------------------------------------------|\n") 
        total_sell = f"\t\t\t\t\t\t|{'Total Amount : $' + str(op.total_amount_last):40s} {'Total Shipping Cost :$'+str(op.total_shipping_cost):9s} \t\t\t\t         |\n"
        w.write(total_sell)  
        w.write("\t\t\t\t\t\t|--------------------------------------------------------------------------------------------------|\n")
        w.write("\t\t\t\t\t\t|                                                                                                  |\n")
        w.write("\t\t\t\t\t\t|***************************Thank You For Giving Us Chance to Serve you****************************|\n")
        w.write("\t\t\t\t\t\t|                                                                                                  |\n")
        w.write("\t\t\t\t\t\t|--------------------------------------------------------------------------------------------------|\n") 

'''this is the invoice bill after user sell laptop its is diffrent than first because it doesn't show shipping cost it is for the user who doesn't want to ship the laptop'''
def withoutorderbill():# no shipping function bill
    """
    This function generates a bill for the user's purchase and saves it to a text file.
      The bill includes the customer name, date of sell, purchase details (laptop name, brand, price, quantity, processor, and graphic), 
      and total amount (excluding shipping cost). The function also displays a thank you message to the customer.
        The bill is saved to a text file in the `Invoice_Sell` directory with the filename being the customer's name.
    """
    filepath = r"Invoice_Sell\\" + op.customer_ + "_no_ship.txt"
    with open(filepath, 'a') as w:
        if w.tell() == 0:
            w.write("\t\t\t\t\t\t|--------------------------------------------------------------------------------------------------|\n")
            w.write("\t\t\t\t\t\t| \t\t\t\t  Arbit laptop Shop                                                        |\n")
            w.write("\t\t\t\t\t\t| \t\t\t\t  Kavresthali,Kathmandu                                                    |\n")
            w.write("\t\t\t\t\t\t| \t\t\t\t  Phone:9863935190,9881224111                                              |\n")
            w.write("\t\t\t\t\t\t|--------------------------------------------------------------------------------------------------|\n")
            customer=f"\t\t\t\t\t\t|{'Customer Name :'+op.customer_:40s} \t\t\t\t\t                           |\n"
            w.write(customer)
            w.write("\t\t\t\t\t\t|                                                      "+"Date of Sell:"+str(op.current_time)+"     |\n")
            w.write("\t\t\t\t\t\t|--------------------------------------------------------------------------------------------------|\n")                                                                                                            
            header = f"\t\t\t\t\t\t|{'Laptops':16s}|    {'Brand':11s}|   {'Price':10s} |  {'Quantity':12s}|  {'Processor':15s}|   {'Graphic':7s}       |\n"
            w.write(header)
            w.write("\t\t\t\t\t\t|--------------------------------------------------------------------------------------------------|\n")
        after_purchase = f"\t\t\t\t\t\t|{op.laptopname:16s}|   {op.brand_sell:11s} |   ${op.price_:<10}| {op.quantity:^12} |  {op.processor_:15s}|   {op.graphic_:7s}     |\n"
        w.write(after_purchase)
        w.write("\t\t\t\t\t\t|--------------------------------------------------------------------------------------------------|\n")
        for sell_item in op.sell_list:
               w.write(sell_item)
               w.write("\t\t\t\t\t\t|--------------------------------------------------------------------------------------------------|\n") 
        total_sell = f"\t\t\t\t\t\t|{'Total Amount :$ ' + str(op.withoutshipping):40s} \t\t\t\t\t                           |\n"
        w.write(total_sell)    
        w.write("\t\t\t\t\t\t|--------------------------------------------------------------------------------------------------|\n")
        w.write("\t\t\t\t\t\t|                                                                                                  |\n")
        w.write("\t\t\t\t\t\t|***************************Thank You For Giving Us Chance to Serve you****************************|\n")
        w.write("\t\t\t\t\t\t|                                                                                                  |\n")
        w.write("\t\t\t\t\t\t|--------------------------------------------------------------------------------------------------|\n")



def withdraw():
                    """
    This function updates the quantity of a laptop in the `products` list and saves the updated list to a text file.
      The function searches for the laptop with the name stored in the `laptopname` variable and subtracts the quantity stored in the 
      `quantity` variable from its quantity. The updated `products` list is then saved to a text file named `laptop.txt`.
    """
                    with open("laptop.txt", "w") as file:
                        for line in rd.products:
                            if line[0].lower() == op.laptopname:
                                line[3] =(" ")+str(int(line[3]) - int(op.quantity))
                            file.write(",".join(line)+ "\n")


def invorder():
        """
    This function updates the quantity of a laptop in the `products` list and saves the updated list to a text file.
      The function searches for the laptop with the name, brand, processor, and graphic stored in the `orderlaptop`,
        `brand_order`, `processor_order`, and `graphic_order` variables, respectively. If the laptop is found, its quantity 
        is increased by the quantity stored in the `quantity_order` variable. If the laptop is not found, a new laptop with 
        the entered details is added to the `products` list. The updated `products` list is then saved to a text file named `laptop.txt`.
    """
        lines=[]
        found=False
        with open("laptop.txt", "w") as file:
                    for line in rd.products:
                        if line[0].strip().lower() == op.orderlaptop.strip().lower():
                                if line[1].strip().lower() == op.brand_order.strip().lower():
                                  if line[4].strip().lower() == op.processor_order.strip().lower():
                                    if line[5].strip().lower() == op.graphic_order.strip().lower():
                                      line[3] =" "+str(int(line[3]) + int(op.quantity_order))
                                      found = True
                        file.write(",".join(line)+ "\n") 

        if not found:
            i = 1
            new_laptop_name = op.orderlaptop
            while any(neww[0].strip().lower() == new_laptop_name.strip().lower() for neww in rd.products):
                new_laptop_name = op.orderlaptop + str(i)
                i += 1
            lines.append(", ".join([new_laptop_name, op.brand_order, "$"+str(op.total_order), str(op.quantity_order), op.processor_order, op.graphic_order]))
            rd.products.append(lines)
            with open("laptop.txt", "a") as o:
                o.write("\n".join(lines)+"\n")


            rd.products=[]
            with open(rd.product)as f:
                for line in f:
                    line=line.strip().split(",")
                    rd.products.append(line)
            


def order_invoice():
    filepath = r"Invoice_order\\" + op.distributor_+ ".txt"
    with open(filepath, 'a') as w:
        if w.tell() == 0:
            w.write("\t\t\t\t\t\t|--------------------------------------------------------------------------------------------------|\n")
            w.write("\t\t\t\t\t\t| \t\t\t\t  Arbit laptop Shop                                                        |\n")
            w.write("\t\t\t\t\t\t| \t\t\t\t  Kavresthali,Kathmandu                                                    |\n")
            w.write("\t\t\t\t\t\t| \t\t\t\t  Phone:9863935190,9881224111                                              |\n")
            w.write("\t\t\t\t\t\t|--------------------------------------------------------------------------------------------------|\n")
            customer=f"\t\t\t\t\t\t|{'Customer Name :'+op.distributor_:40s} \t\t\t\t\t                           |\n"
            w.write(customer)
            w.write("\t\t\t\t\t\t|                                                      "+"Date of Sell:"+str(op.current_time)+"     |\n")
            w.write("\t\t\t\t\t\t|--------------------------------------------------------------------------------------------------|\n")                                                                                                            
            header = f"\t\t\t\t\t\t|{'Laptops':16s}|    {'Brand':11s}|   {'Price':10s} |  {'Quantity':12s}|  {'Processor':15s}|   {'Graphic':7s}       |\n"
            w.write(header)
            w.write("\t\t\t\t\t\t|--------------------------------------------------------------------------------------------------|\n")
            after_purchase = f"\t\t\t\t\t\t|{op.orderlaptop:16s}|   {op.brand_order:11s} |   ${int(op.total_order):<10}| {op.quantity_order:^12} |  {op.processor_order:15s}|   {op.graphic_order:14}|\n"
            w.write(after_purchase)
            w.write("\t\t\t\t\t\t|--------------------------------------------------------------------------------------------------|\n")
            for order_item in op.sell_order_list:
                        w.write(order_item)
                        w.write("\t\t\t\t\t\t|--------------------------------------------------------------------------------------------------|\n") 
            orderfinish = f"\t\t\t\t\t\t|{'Total Amount :$ ' + str(op.total_order_last):40s} {'Total Amount without Vat : $' + str(op.novatt):40s}      \t         |\n"
            w.write(orderfinish)
            w.write("\t\t\t\t\t\t|                                                                                                  |\n")
            w.write("\t\t\t\t\t\t|***************************Thank You For Giving Us Chance to Serve you****************************|\n")
            w.write("\t\t\t\t\t\t|                                                                                                  |\n")
            w.write("\t\t\t\t\t\t|--------------------------------------------------------------------------------------------------|\n")
