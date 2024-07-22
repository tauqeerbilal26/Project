from typing import Optional, Tuple, Dict


suggestions: Dict[str, str] = {
    "strong": "Espresso",
    "creamy": "Latte",
    "frothy": "Cappuccino",
    "black": "Americano",
    "sweet": "Mocha"
}

price_list: Dict[str, int] = {
    "Espresso": 300,
    "Latte": 490,
    "Cappuccino": 430,
    "Americano": 339,
    "Macchiato": 424,
    "Mocha": 520
}

class CoffeeBarManagement:
    def __init__(self) -> None:
        self._inventory: Dict[str, int] = {
            "Espresso": 10,
            "Latte": 10,
            "Cappuccino": 10,
            "Americano": 10,
            "Macchiato": 10,
            "Mocha": 10
        }
        self._coffee_types: Dict[int, str] = {
            1: "Espresso",
            2: "Latte",
            3: "Cappuccino",
            4: "Americano",
            5: "Macchiato",
            6: "Mocha"
        }
        self._customer_name: Optional[str] = None
        self._order: Optional[Tuple[str, int]] = None

        
        for coffee, quantity in self._inventory.items():
            if quantity > 10:
                print(f"Error: The quantity of {coffee} exceeds 10. Exiting program.")
                exit(1)

    def display_menu(self) -> None:
        print("Menu:")
        for number, coffee_type in self._coffee_types.items():
            print(f"{number}. {coffee_type}")

    def check_avail(self) -> None:
        self.display_menu()
        try:
            choice = int(input("Enter the number of the coffee type to check availability: "))
            if choice in self._coffee_types:
                coffee_type = self._coffee_types[choice]
                if self._inventory[coffee_type] > 0:
                    print(f"{coffee_type} is available in our coffee bar.")
                else:
                    print(f"{coffee_type} is not available in our coffee bar.")
            else:
                print("Invalid choice. Please select a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def place_order(self) -> None:
        if self._customer_name is None:
            print("Please enter your name first.")
            return

        self.display_menu()
        
        try:
            choice = int(input("Select the number of the coffee you want to drink: "))
            if choice not in self._coffee_types:
                print("Invalid choice. Please select a valid number.")
                return
            
            coffee_type = self._coffee_types[choice]
            quantity = int(input(f"How many cups of {coffee_type} would you like to order? "))
            
            if self._inventory[coffee_type] >= quantity:
                self._inventory[coffee_type] -= quantity
                self._order = (coffee_type, quantity)
                print(f"Order placed: {quantity} x {coffee_type}.")
                
                total_price = self.calculate_total_price(coffee_type, quantity)
                print(f"The total price for the order is: PKR.{total_price}")
            else:
                print(f"Sorry, we only have {self._inventory[coffee_type]} cups of {coffee_type} left.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def get_customer_info(self) -> str:
        return f"Customer Name: {self._customer_name}"

    def add_customer_name(self) -> None:
        self._customer_name = input("Please enter your name: ")
        print(f"Customer name set to {self._customer_name}.")

    @staticmethod
    def calculate_total_price(coffee_type: str, quantity: int) -> int:
        price_per_unit = price_list.get(coffee_type, 0)
        total_price = price_per_unit * quantity
        return total_price

    @classmethod
    def suggest_drink(cls) -> str:
        pref = input("If you want any suggestions according to your taste, enter your preference (Strong, Creamy, Frothy, Black, Sweet): ").lower()
        drink = suggestions.get(pref, "Sorry, we don't have a suggestion for that preference.")
        return drink

if __name__ == "__main__":
    coffee_bar = CoffeeBarManagement()

    coffee_bar.add_customer_name()
    coffee_bar.check_avail() 
    coffee_bar.place_order()

    print(coffee_bar.get_customer_info())

    suggestion = CoffeeBarManagement.suggest_drink()
    print(f"Based on your preference, we suggest: {suggestion}")
