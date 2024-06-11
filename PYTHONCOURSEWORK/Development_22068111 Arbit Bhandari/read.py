import datetime

# Define the name of the file containing product information
product=("laptop.txt")
# Create an empty list to store product information
products=[]
# Open the product file and read each line
with open(product,'r')as f:
    # Split each line into a list of strings using the comma as a separator
    for i in f:
        i=i.strip().split(',')
        # Add the list of strings to the products list
        products.append(i)
def display():
       """
        This function displays a table of available laptops. The table includes the laptop name, brand, price, quantity,
          processor, and graphic for each laptop in the `products` list.
        """
       # Loop through each laptop in the products list
       print('-------------------------------------------------------------------------------------------------------------')
       print ( "| {:15s} | {:15s} | {:15s} | {:14s} | {:16s} | {:15s} |".format('Laptops', 'Brand', 'Price', 'Quantity', 'Processor', 'Graphic'))
       print('-------------------------------------------------------------------------------------------------------------')
       for b in products:
                    if len(b) == 6:
                        print("| {:15s} | {:15s} | {:15s} | {:14s} | {:16s} | {:15s} |".format(b[0],b[1],b[2],b[3],b[4],b[5]))
                        print('-------------------------------------------------------------------------------------------------------------')

