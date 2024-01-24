# Vending Machine Program

This Python program simulates a vending machine. Users can interact with the machine by inserting coins, selecting products, and making purchases. The program is organized into a class called `Maquina_expendedora` (Vending Machine in Spanish), which encapsulates the functionality of the vending machine.

# Class Attributes

- `_Moneda_existente`: List containing valid coin denominations for the vending machine.
- `_Dinero_total`: User's total amount of money.
- `_Dinero_ingresado`: String representing the money to be entered by the user.
- `_Productos`: Dictionary containing information about products, including their prices, names, quantities, and positions.
- `_Producto_elegido`: String representing the user's selected product.
- `_Dinero_falta`: Variable to keep track of the remaining amount of money needed for a purchase.

# Class Methods

# `__init__(self)`

- Initializes the vending machine with default values.
- Sets up the list of valid coins, initializes the user's money total, and defines the product dictionary.

# `ingreso_de_dinero(self)`

- Allows the user to input coins.
- Displays available products and their details.
- Accepts user input for coins until the user presses 'F' to finish.
- Validates the input coins and updates the total money accordingly.

# `producto(self)`

- Asks the user to input the position of the desired product or 'R' to get a refund.
- Handles cases where the entered product is unavailable or incorrectly written.
- Provides the user with options to re-enter the product or get a refund.

# `compra(self)`

- Processes the purchase based on the user's selected product and available money.
- Handles scenarios where the user has insufficient funds or the product is out of stock.
- Prompts the user to add more money ('F') or get a refund ('R') in case of insufficient funds.
- Completes the purchase and updates the product quantity and user's total money.

# How to Use

1. Instantiate the `Maquina_expendedora` class: `me = Maquina_expendedora()`.
2. Run the vending machine loop: `while True: me.ingreso_de_dinero()`, `me.producto()`, `me.compra()`.

Follow the prompts to insert money, select products, and complete purchases. The program will continue running until manually stopped.

Note: This program is written in Spanish. If you prefer an English version, you may consider translating the user prompts and comments.
