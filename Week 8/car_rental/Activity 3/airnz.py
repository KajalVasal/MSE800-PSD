"""
Single Inheritance
Air New Zealand Domestic Flight System
Demonstrates: Parent class, Child class, inheritance, method overriding
"""

# ===== Parent Class: General Flight =====
class Flight:
    def __init__(self, flight_no, from_city, to_city):
        """
        Constructor for parent class
        Shared attributes - inherited by all child classes
        """
        self.flight_no = flight_no      # Flight number, e.g. "NZ501"
        self.from_city = from_city      # Origin city
        self.to_city = to_city          # Destination city
        self.airline = "Air New Zealand" # Shared for all flights

    # Shared method - inherited by subclass without changes
    def show_info(self):
        """Display basic flight information - inherited by child"""
        return f"Airline: {self.airline}\nFlight: {self.flight_no}\nRoute: {self.from_city} -> {self.to_city}"

    # Another shared method
    def get_route(self):
        """Return route string - inherited by child"""
        return f"{self.from_city} to {self.to_city}"

# ===== Child Class: Domestic Flight =====
# Single inheritance: DomesticFlight inherits from only 1 parent = Flight
class DomesticFlight(Flight):
    def __init__(self, flight_no, from_city, to_city, baggage_limit):
        """
        Constructor for child class
        super() calls parent __init__ to inherit shared attributes
        """
        super().__init__(flight_no, from_city, to_city)  # Inherit parent attributes
        
        # Additional attributes specific to domestic flights only
        self.is_domestic = True
        self.baggage_limit = baggage_limit  # kg, NZ domestic rule

    # Additional method specific to domestic flight
    def check_baggage(self, weight):
        """Check baggage weight against NZ domestic limit"""
        if weight <= self.baggage_limit:
            return f"Baggage OK. {self.baggage_limit - weight}kg remaining"
        else:
            excess = weight - self.baggage_limit
            return f"Overweight by {excess}kg. Extra fee applies"

    # Method overriding: child extends parent method
    def show_info(self):
        """
        Override parent method to add domestic-specific info
        super().show_info() reuses parent code
        """
        base_info = super().show_info()  # Call parent method
        return f"{base_info}\nType: Domestic Flight\nBaggage Limit: {self.baggage_limit}kg"

# ===== Demo: Show inheritance working =====
if __name__ == "__main__":
    print("=== Air New Zealand - Activity 8 Demo ===\n")
    
    # Create object of child class
    flight1 = DomesticFlight("NZ503", "Auckland", "Wellington", 23)
    
    # 1. Access inherited attributes from parent
    print("1. Inherited attributes from Flight parent:")
    print(f"Airline: {flight1.airline}")      # Inherited
    print(f"Flight No: {flight1.flight_no}")  # Inherited
    
    # 2. Call inherited method from parent
    print("\n2. Inherited method get_route():")
    print(flight1.get_route())
    
    # 3. Call overridden method - child version
    print("\n3. Overridden method show_info():")
    print(flight1.show_info())
    
    # 4. Call new method only in child
    print("\n4. Child-specific method check_baggage():")
    print(flight1.check_baggage(20))
    print(flight1.check_baggage(27))
    
    # 5. Proof of single inheritance
    print(f"\n5. isinstance check: flight1 is Flight = {isinstance(flight1, Flight)}")
    print(f"   isinstance check: flight1 is DomesticFlight = {isinstance(flight1, DomesticFlight)}")