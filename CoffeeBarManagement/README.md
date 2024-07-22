# CoffeeBarManagement

The `CoffeeBarManagement` class simulates a simple coffee bar management system, handling inventory, customer orders, and coffee suggestions based on customer preferences.

## Preset Data

- **Suggestions**: A dictionary mapping taste preferences to coffee types.
  ```python
  suggestions: Dict[str, str] = {
      "strong": "Espresso",
      "creamy": "Latte",
      "frothy": "Cappuccino",
      "black": "Americano",
      "sweet": "Mocha"
  }

- **Price List**: A dictionary mapping coffee types to their prices
    ```python
    price_list: Dict[str, int] = {
    "Espresso": 300,
    "Latte": 490,
    "Cappuccino": 430,
    "Americano": 339,
    "Macchiato": 424,
    "Mocha": 520 }

## Class Definition
### CoffeeBarManagement
` __init__(self) -> None `
- Initializes the coffee bar with a preset inventory of 10 units for each coffee type and defines the coffee types. It also checks if any inventory item exceeds 10 units,  exiting the program if so.

`display_menu(self) -> None`
 - Displays the coffee menu.

`check_avail(self) -> None`
 - Displays the menu and prompts the user to enter the number of the coffee type to check its availability.

`place_order(self) -> None`
 - Prompts the user to place an order, checking if the selected coffee type is available in the desired quantity. It also calculates and displays the total price for the order.

`get_customer_info(self)` -> str
 - Returns the customer's name.

`add_customer_name(self) -> None`
 - Prompts the user to enter their name and sets it for the current session.

`calculate_total_price(coffee_type: str, quantity: int) -> int`
 - Calculates the total price for the given coffee type and quantity.

`suggest_drink(cls) -> str`
 - Prompts the user to enter their taste preference and suggests a drink based on it.

## Usage
### 1 - Initialize the Coffee Bar Management System 
   ```python
   coffee_bar = CoffeeBarManagement()
   ```
  
### 2 - Add Customer name 
   ```python
   coffee_bar.add_customer_name()
   ```
### 3 - Check Coffee Availability
         coffee_bar.check_avail()
### 4-Place an Order
      coffee_bar.place_order()
### 5-Get Customer Info
     print(coffee_bar.get_customer_info())
### 6-Suggest a Drink Based on Taste Preference
    suggestion = CoffeeBarManagement.suggest_drink()
    print(f"Based on your preference, we suggest: {suggestion}")

## Example
  ```python
  if __name__ == "__main__":
    coffee_bar = CoffeeBarManagement()

    coffee_bar.add_customer_name()
    coffee_bar.check_avail()  
    coffee_bar.place_order()

    print(coffee_bar.get_customer_info())

    suggestion = CoffeeBarManagement.suggest_drink()
    print(f"Based on your preference, we suggest: {suggestion}")
       
