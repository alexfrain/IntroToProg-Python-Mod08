# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# Alex Frain,3.6.2021,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

import pickle

# Data -------------------------------------------------------------------- #
strFileName = 'products.dat'
#lstOfProductObjects = []


class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the product's  name
        product_price: (float) with the product's standard price]
    methods:
        __str__(self): -> self
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Alex Frain,3.6.2021,Modified code to complete assignment 8
    """

    # TODO: Add Code to the Product class
    # --Fields--
    # No Fields in this class

    # --Constructor--
    def __init__(self, product_name, product_price):
        # --Attributes--
        self.__product_name = product_name
        self.__product_price = product_price

    # --Properties--
    @property  # Getter for product_name
    def product_name(self):
        return self.__product_name

    @product_name.setter  # Setter for product_name
    def product_name(self, value):
        if str(value).isnumeric() is False:
            self.__product_name = value
        else:
            raise Exception("Product names cannot be numbers")

    @property  # Getter for product_price
    def product_price(self):
        return self.__product_price

    @product_price.setter  # Setter for product_price
    def product_price(self, value):
        try:
            self.__product_price = float(value)
        except ValueError as e:
            print("You did not enter a number for price")
            print("ERROR: ", e, type(e), "\n")

    # --Methods--
    def __str__(self):
        return self.product_name + ", $" + str(self.product_price)


# Data - END -------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Alex Frain,3.6.2021,Modified code to complete assignment 8
    """

    # TODO: Add Code to process data from a file
    @staticmethod
    def read_data_from_file(file_name):
        """  Read product object list in from file

        :return: list
        """
        list_of_products = []
        try:
            file_obj = open(file_name, 'rb')
            list_of_products = pickle.load(file_obj)
            file_obj.close()

        except FileNotFoundError:
            print(f'ERROR: {file_name} not found')

        return list_of_products

    # TODO: Add Code to process data to a file
    @staticmethod
    def save_data_to_file(file_name, list_of_product_objects):
        """  Save product object list to file

        :return: nothing
        """
        file_obj = open(file_name, 'wb')
        pickle.dump(list_of_product_objects, file_obj)
        file_obj.close()
        print('Product list saved to file')


# Processing - END--------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    # TODO: Add docstring
    """Obtains input from and displays out to the user:

    methods:
        print_menu_products():

        get_user_choice(): --> int choice

        show_current_data_in_list(list_of_products):

        get_product_data_from_user() --> string name, float price
    changelog: (When,Who,What)
        Alex Frain,3.6.2021,Modified code to complete assignment 8
    """

    # TODO: Add code to show menu to user
    @staticmethod
    def print_menu_products():
        """  Display a menu of choices

        :return: nothing
        """
        print('''
        Menu of Options
        1) Add a new Product
        2) Save Data to File
        3) Reload Data from File
        4) Show Current List of Products
        5) Exit Program
        ''')

    # TODO: Add code to get user's choice
    @staticmethod
    def get_user_choice():
        """  Gets the menu choice from the user

        :return: int
        """
        # Use while loop to obtain valid menu input choice from user
        while True:
            try:
                choice = int(input('Which option would you like to perform? [1 to 5] - ').strip())
                if choice in range(1, 6):
                    break
                else:
                    print(f'{choice} is not a valid menu choice. Must be 1 to 5\n')
            except ValueError as e:
                print("You did not enter a number")
                print("ERROR: ", e, type(e), '\n')

        print()  # Add an extra line for looks
        return choice

    # TODO: Add code to show the current data from the file to user
    @staticmethod
    def show_current_data_in_list(list_of_products):
        """  Print current list of product objects

        :return: nothing
        """
        print('*** The current list of products are: ***')
        if not list_of_products:
            print('***       - The list is empty -       ***')
        else:
            for product in list_of_products:
                print(product)
        print('*****************************************')

    # TODO: Add code to get product data from user
    @staticmethod
    def get_product_data_from_user():
        """  Gets product name and price from the user

        :return: string, float
        """
        while True:
            try:
                name = str((input('Enter product name: ').lower()).strip())
                if name.isnumeric():
                    raise Exception('Product names cannot be numbers')
                elif name.islower() is False:
                    raise Exception('Product name must contain a letter')
                elif name == "":
                    print('Product name cannot be blank')
                    continue

            except Exception as e:
                print('ERROR: ', e, type(e), '\n')

            else:
                break

        while True:
            try:
                price = float(input('Enter product price: $'))

            except ValueError as e:
                print('You did not enter a number for price')
                print('ERROR: ', e, type(e), '\n')
            else:
                print()  # Add an extra line for looks
                break

        return name, price

# Presentation (Input/Output) - END --------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body
# Load data from file into a list of product objects when script starts
# Show user a menu of options
# Get user's menu option choice
# Show user current data in the list of product objects
# Let user add data to the list of product objects
# let user save current data to file and exit program

# Load data from file into a list of product objects when script starts
print('\nLoading data from file - unpickle')
lstOfProductObjects = FileProcessor.read_data_from_file(strFileName)
if not lstOfProductObjects:
    print('*** The product list is empty ***')
else:
    IO.show_current_data_in_list(lstOfProductObjects)

while True:
    IO.print_menu_products()    # show user a menu of options
    choice_int = IO.get_user_choice()   # get user's menu choice

    if choice_int == 1:     # Add a new product
        name_str, price_float = IO.get_product_data_from_user()
        prod = Product(name_str, price_float)
        lstOfProductObjects.append(prod)
        IO.show_current_data_in_list(lstOfProductObjects)
        continue

    elif choice_int == 2:   # Save data to file
        FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
        continue

    elif choice_int == 3:   # Reload data from file
        print('Reloading Product List from file\n')
        lstOfProductObjects = FileProcessor.read_data_from_file(strFileName)
        IO.show_current_data_in_list(lstOfProductObjects)
        continue

    elif choice_int == 4:   # Show current list of products
        IO.show_current_data_in_list(lstOfProductObjects)
        continue

    elif choice_int == 5:   # Exit script
        print("Exiting script. Goodbye!")
        break

# Main Body of Script - END------------------------------------------------ #

